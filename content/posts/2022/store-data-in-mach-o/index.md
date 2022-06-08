---
title: "在 Mach-O 中读写数据"
date: 2022-06-08T18:02:34+08:00
categories: [iOS, Mach-O]
tags: []
---

## 背景

我们有时会遇到这种需求：在程序启动时立即需要知道某些数据。

一个例子是，我们在解耦时会定义一些协议，用于模块间沟通，这些协议与实现类的关联关系就是这样一种数据，如果通过本地文件读写可能来不及，因为这个协议的反射调用可能非常早。如果不及时获取映射数据，会导致调用失败。

## 原理

之前在 [app 启动过程](/posts/2021/app-launch-process/) 一文中提过，main 函数之前系统会让 `dyld` 去加载 app 依赖的各种动态库，
这里系统提供了一个回调方法，可以让我们获知这些库被加载进内存的时机。

在 `<mach-o/dyld.h>` 中

```objc
/*
 * The following functions allow you to install callbacks which will be called   
 * by dyld whenever an image is loaded or unloaded.  During a call to _dyld_register_func_for_add_image()
 * the callback func is called for every existing image.  Later, it is called as each new image
 * is loaded and bound (but initializers not yet run).  The callback registered with
 * _dyld_register_func_for_remove_image() is called after any terminators in an image are run
 * and before the image is un-memory-mapped.
 */
extern void _dyld_register_func_for_add_image(void (*func)(const struct mach_header* mh, intptr_t vmaddr_slide))    __OSX_AVAILABLE_STARTING(__MAC_10_1, __IPHONE_2_0);
extern void _dyld_register_func_for_remove_image(void (*func)(const struct mach_header* mh, intptr_t vmaddr_slide)) __OSX_AVAILABLE_STARTING(__MAC_10_1, __IPHONE_2_0);
```

在这个回调方法中，我们可以拿到 `mach_header` 的指针，就可以读写 `section` 中的数据，具体实现在下一节介绍。

解决了读的时机问题，那么我们怎么写数据呢？

我们知道静态变量是存储在 `Mach-O` 的静态存储区，比如定义一个 `NSString`：

```objc
static NSString * const s_myStr = @"The quick brown fox jumps over the lazy dog";
```

通过 `MachOView` 可以发现，具体是存储在 `section` 段的 `__TEXT,__cstring` 区块中。

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-06-08-9S6mTb.png)

### 存储数据

所以，我们有没有办法在 `section` 中存储自定义的数据呢？有！

```objc
__attribute((used, section("__DATA,_my_pre_data"))) static const char *quote = "Practice makes perfect.";
```

声明这样一个静态变量之后，会发现 `__DATA` 中多了一个区块，但是定义的字符串并不在这里。这里只存储了字符串的地址，数据仍然存储在
`__TEXT,__cstring` 区块中。

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-06-08-nfdlgP.png)

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-06-08-vrntAl.png)

## 实现

有了上述的背景知识，我们就可以读写自己的数据了。

假如我们有这样一个数据结构：

```c
typedef struct {
    char *key;
    char *val;
    int idx;
} my_data_t;
```

那么，写入 `section` 段就是：

```c
__attribute((used, section("__DATA,_my_pre_data"))) static my_data_t dt1 = {
   "kkk1",
   "vvv1",
   1,
};
```

为了便于通用，我们可以定义一个宏，方便自动创建这样的静态变量：

```cpp
#define _PRELD_SECNAME "_my_pre_data"

#define _STR(name) (#name)

#define _PRELD_DATA(_k, _v, _i)\
__attribute((used, section("__DATA," _PRELD_SECNAME))) static my_data_t _dt##_k = \
{\
    _STR(_k),\
    _STR(_v),\
    _i,\
};\
```

用起来非常方便：

`_PRELD_DATA(kkk, vvv, 1)`

### 读取数据

前面说过，注册 `dyld` 加载的回调即可读取 `section` 中存储的数据：

```cpp
__attribute__((constructor)) void preMainMethod() {
    _dyld_register_func_for_add_image(dyld_func);
}
```

`__attribute__((constructor))` 使用这种描述的 C 方法就可以在 main 之前执行。

那么 `dyld_func` 如何实现呢？

```objc
static void dyld_func(const struct mach_header *header, intptr_t slide) {
    unsigned long size = 0;
#if defined(__LP64__) && __LP64__
    const struct mach_header_64 *mhp64 = (const struct mach_header_64 *)header;
    uintptr_t *memory = (uintptr_t *)getsectiondata(mhp64, SEG_DATA, _PRELD_SECNAME, &size);
#else
    uintptr_t *memory = (uintptr_t *)getsectiondata(header, SEG_DATA, _PRELD_SECNAME, &size);
#endif
    unsigned long n = size / sizeof(my_data_t);
    my_data_t *data = (my_data_t *)memory;
    for (int i = 0; i < n; i++) {
        my_data_t tmp = data[i];
        std::cout << tmp.key << ": " << tmp.val << "(" << tmp.idx << ")" << std::endl;
    }
}
```

这里可能会有一个疑问，既然这个回调方法是每次加载 image 时都会调用，这个读取不是会多次执行吗？

是的，但是只有 image 是 app 本身时才能读取到数据。因为我们写入数据的 `section` 是在 app 本身的 `Mach-O` 中的。

### 副产品

那么能不能获取到 app 启动到底加载了哪些库呢？

在 `#include <dlfcn.h>` 中，有这样一个数据结构：

```c
/*
 * Structure filled in by dladdr().
 */
typedef struct dl_info {
        const char      *dli_fname;     /* Pathname of shared object */
        void            *dli_fbase;     /* Base address of shared object */
        const char      *dli_sname;     /* Name of nearest symbol */
        void            *dli_saddr;     /* Address of nearest symbol */
} Dl_info;
```

我们可以使用 `dladdr()` 获取它：

```objc
Dl_info  DlInfo;
dladdr(header, &DlInfo);
const char* image_name = DlInfo.dli_fname;
std::cout << image_name << std::endl;
```

搞定！


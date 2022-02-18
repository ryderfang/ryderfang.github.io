# Meta Class


Meta 这个词在 2021 年下半年开始火爆，而后 Facebook 改名 Meta 引发各大科技公司跟风押注。似乎全球资本都在追逐“元宇宙”的概念，但什么是“元宇宙”，各家有各家的说法，没有一个统一的标准。

<!--more-->

> 我个人感觉，元宇宙就是个伪概念。除了一堆跟风炒概念准备割韭菜的老庄家和引颈待收割的韭菜外，各个公司在做的与“元宇宙”相关的事，似乎都是一些“复古网络游戏”。

> 历史是一个轮回，唯有资本逐利是永恒的。不出三年，这个概念应该就不会有人提了，一如 VR 的喧嚣与沉寂。

## Meta 的起源

以上只是个引子，与本文无关 <生硬的转折 😅>。本文继续讨论 Runtime，聚焦 OC 中的 MetaClass。

Greg Parker 经典图

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2021-12-23-class-diagram.png)

## 为什么要这么设计

由于 OC 是 Smalltalk 语言哲学的一种实践，“在 Smalltalk 中，所有的值都是对象”。因此一个实例是对象，它的类也是一个对象。

实例中的 isa 指针指向了它的类对象，那么类对象的 isa 指针指向谁呢？—— 指向它的元类对象 MetaClass！

> Since a class is an object, it must be an instance of some other class: a metaclass. [^1]

那么能不能不这么设计呢？

当然能，但是这样就不那么 “Smalltalk” 了。非 Smalltalk 语言如 C++，与 OC 的一个重要区别是：

> C++ 支持多重继承

## Meta 与 继承关系

定义一对父类与子类：

```
@interface Person : NSObject
@end

@interface Student : Person
@end
```

### isa 链

定义一个子类的实例 `Student *stu`，根据之前的文章 [class-object-isa](./class-object-isa/)，实例本质上是一个 `objc_object` 结构体，内部存在一个 isa 指针，指向的是 `Student` 这个类对象。

而类对象 `Student` 本质上是一个 `objc_class` 结构体，继承自 `objc_object`，所以内部也有一个 isa 指针，类对象的 isa 指针指向的是它的元类对象。

所以，这条链，也就是上图中最下面一行虚线所示：

> 实例 --> 类 --> 元类

那么元类的 isa 又指向谁呢，图中显示的是 **根元类**，通过代码来获取一下这条链：

```
Student *stu = [Student new];
NSLog(@"Student instance addr: %p", stu);
Class cls = [stu class];
NSLog(@"Student class addr: %p", cls);
id rootMetaClass = nil;
while (cls) {
    NSLog(@"isa: %s addr: %p", object_getClassName(cls), cls);
    Class tmp = object_getClass(cls);
    if (tmp == cls) {
        rootMetaClass = cls;
        break;
    }
    cls = tmp;
}
NSLog(@"root MetaClass: %p", rootMetaClass);
```

-->

```
Student instance addr: 0x100668810
Student class addr: 0x10000e7b8
isa: Student addr: 0x10000e7b8
isa: NSObject addr: 0x10000e790
isa: NSObject addr: 0x7fff806e7060
root MetaClass: 0x7fff806e7060
```

可以看出来，元类对象最终指向的是根元类对象，但它的名字也叫 `NSObject`，同时根元类的 isa 是指向自身的，所以最终形成了闭环。

> 实例 --> 类 --> 元类 --> 根元类 ↩️

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-02-18-hlCbiY.png)

### 继承链

再来看一下继承关系，

```
Class cls = [stu class];
id rootClass = nil;
    while (cls) {
        NSLog(@"class: %s addr: %p", object_getClassName(cls), cls);
        if (!class_getSuperclass(cls)) {
            rootClass = cls;
        }
        cls = class_getSuperclass(cls);
    }
    NSLog(@"rootClass: %p", rootClass);
```

-->

```
class: Student addr: 0x10000e7b8
class: Person addr: 0x10000e768
class: NSObject addr: 0x7fff806e7088
rootClass: 0x7fff806e7088
```

继承链比较简单：

> 子类 -> 父类 -> 根类 -> 空

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-02-18-3DVEXQ.png)

可以看出来根类没有父类，顺便我们看一下根类的 isa 指向哪里？

```
NSLog(@"rootClass'isa: %p", object_getClass(rootClass));

// rootClass'isa: 0x7fff806e7060
```

地址 `0x7fff806e7060` 与前面根元类 `rootMetaClass` 一样，这也证实了 `根类 --> 根元类`。

## 题外话

在研究这个图的过程中，有一些容易混淆的点，这里记录一下

### 获取类对象

有好几种获取类对象的方法：

#### class 方法

有两种 class 方法，一个是实例方法，一个是类方法：

@interface NSObject <NSObject>

`- (Class)class OBJC_SWIFT_UNAVAILABLE("use 'type(of: anObject)' instead");`

`+ (Class)class OBJC_SWIFT_UNAVAILABLE("use 'aClass.self' instead");`

@end

查看 runtime 的源码：[NSObject.mm](https://opensource.apple.com/source/objc4/objc4-750/runtime/NSObject.mm.auto.html)

可以看到它们的实现：

```
+ (id)self {
    return (id)self;
}

- (id)self {
    return self;
}

+ (Class)class {
    return self;
}

- (Class)class {
    return object_getClass(self);
}
```

所以，说给类对象发 `class` 消息，得到的是类本身 `self`，也就是 

> [NSObject class] == [NSObject self]

给实例对象发 `class` 消息，相当于调用了 `object_getClass`

#### object_getClass

那么这个方法的实现是怎么样的呢？

同样查看 runtime 源码：[objc-class.mm](https://opensource.apple.com/source/objc4/objc4-750/runtime/objc-class.mm.auto.html)

`Class _Nullable object_getClass(id _Nullable obj)`

```
Class object_getClass(id obj)
{
    if (obj) return obj->getIsa();
    else return Nil;
}
```

调用了 类的 `getIsa()` 方法

// [objc-object.h](https://opensource.apple.com/source/objc4/objc4-750/runtime/objc-object.h.auto.html)
```
inline Class 
objc_object::getIsa() 
{
    if (!isTaggedPointer()) return ISA();

    uintptr_t ptr = (uintptr_t)this;
    if (isExtTaggedPointer()) {
        uintptr_t slot = 
            (ptr >> _OBJC_TAG_EXT_SLOT_SHIFT) & _OBJC_TAG_EXT_SLOT_MASK;
        return objc_tag_ext_classes[slot];
    } else {
        uintptr_t slot = 
            (ptr >> _OBJC_TAG_SLOT_SHIFT) & _OBJC_TAG_SLOT_MASK;
        return objc_tag_classes[slot];
    }
}
```

#### objc_getClass

这个方法和上面的 `object_getClass` 长得很像，但还是有一些区别：

* 参数不一样，一个是 `id`，一个是 `const char *`，也就是一个传入是个类对象，一个是类名

* 实现不一样，一个调用的是 `obj->getIsa()`，一个调用的是 `loop_up_class()`

// [objc-runtime.mm](https://opensource.apple.com/source/objc4/objc4-750/runtime/objc-runtime.mm.auto.html)
```
Class objc_getClass(const char *aClassName)
{
    if (!aClassName) return Nil;

    // NO unconnected, YES class handler
    return look_up_class(aClassName, NO, YES);
}
```

调用了 `look_up_class`:

// [objc-runtime-new.mm](https://opensource.apple.com/source/objc4/objc4-787.1/runtime/objc-runtime-new.mm.auto.html)
```
Class 
look_up_class(const char *name, 
              bool includeUnconnected __attribute__((unused)), 
              bool includeClassHandler __attribute__((unused)))
{
    if (!name) return nil;

    Class result;
    bool unrealized;
    {
        runtimeLock.lock();
        result = getClassExceptSomeSwift(name);
        unrealized = result  &&  !result->isRealized();
        if (unrealized) {
            result = realizeClassMaybeSwiftAndUnlock(result, runtimeLock);
            // runtimeLock is now unlocked
        } else {
            runtimeLock.unlock();
        }
    }

    if (!result) {
        // Ask Swift about its un-instantiated classes.

        // We use thread-local storage to prevent infinite recursion
        // if the hook function provokes another lookup of the same name
        // (for example, if the hook calls objc_allocateClassPair)

        auto *tls = _objc_fetch_pthread_data(true);

        // Stop if this thread is already looking up this name.
        for (unsigned i = 0; i < tls->classNameLookupsUsed; i++) {
            if (0 == strcmp(name, tls->classNameLookups[i])) {
                return nil;
            }
        }

        // Save this lookup in tls.
        if (tls->classNameLookupsUsed == tls->classNameLookupsAllocated) {
            tls->classNameLookupsAllocated =
                (tls->classNameLookupsAllocated * 2 ?: 1);
            size_t size = tls->classNameLookupsAllocated *
                sizeof(tls->classNameLookups[0]);
            tls->classNameLookups = (const char **)
                realloc(tls->classNameLookups, size);
        }
        tls->classNameLookups[tls->classNameLookupsUsed++] = name;

        // Call the hook.
        Class swiftcls = nil;
        if (GetClassHook.get()(name, &swiftcls)) {
            ASSERT(swiftcls->isRealized());
            result = swiftcls;
        }

        // Erase the name from tls.
        unsigned slot = --tls->classNameLookupsUsed;
        ASSERT(slot >= 0  &&  slot < tls->classNameLookupsAllocated);
        ASSERT(name == tls->classNameLookups[slot]);
        tls->classNameLookups[slot] = nil;
    }

    return result;
}
```

最后，做个试验：

```
Student *stu = [Student new];
Class cls = [stu class];
NSLog(@"%p %p %p %p", cls, [Student class], objc_getClass("Student"), object_getClass(stu));
```

```
0x10000e7b8 0x10000e7b8 0x10000e7b8 0x10000e7b8
```

可以看出来，这四种方法拿到的结果是一样的。






[^1]: http://www.sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html










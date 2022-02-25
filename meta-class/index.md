# 从 Meta 说起


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

```objc
@interface Person : NSObject
@end

@interface Student : Person
@end
```

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello, World!")
}
```

### isa 链

定义一个子类的实例 `Student *stu`，根据之前的文章 [class-object-isa](./class-object-isa/)，实例本质上是一个 `objc_object` 结构体，内部存在一个 isa 指针，指向的是 `Student` 这个类对象。

而类对象 `Student` 本质上是一个 `objc_class` 结构体，继承自 `objc_object`，所以内部也有一个 isa 指针，类对象的 isa 指针指向的是它的元类对象。

所以，这条链，也就是上图中最下面一行虚线所示：

> 实例 --> 类 --> 元类

那么元类的 isa 又指向谁呢，图中显示的是 **根元类**，通过代码来获取一下这条链：

```objc
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

```r
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

```objc
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

```r
class: Student addr: 0x10000e7b8
class: Person addr: 0x10000e768
class: NSObject addr: 0x7fff806e7088
rootClass: 0x7fff806e7088
```

继承链比较简单：

> 子类 -> 父类 -> 根类 -> nil

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-02-18-3DVEXQ.png)

可以看出来根类没有父类，顺便我们看一下根类的 isa 指向哪里？

```objc
NSLog(@"rootClass'isa: %p", object_getClass(rootClass));

// rootClass'isa: 0x7fff806e7060
```

地址 `0x7fff806e7060` 与前面根元类 `rootMetaClass` 一样，这也证实了 `根类 --> 根元类`。

[^1]: http://www.sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html










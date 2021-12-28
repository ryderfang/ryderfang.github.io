# ObjC 之 Runtime 是个啥


## 概述

Runtime 是 OC 这个语言的核心，也是为什么 OC 被称为动态语言的原因。

当我们在讲 `Runtime` 的时候，我们在说什么？

根据官方文档的定义，

[Objective-C Runtime](https://developer.apple.com/documentation/objectivec/objective-c_runtime?language=objc)

[Objective-C Runtime Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008048-CH1-SW1)

Runtime 是一个动态库 (/usr/lib/libobjc.A.dylib)，用于实现 OC 语言的动态性。

这个动态性主要体现在三个方面：

- Dynamic Typing  运行时才能决定对象的类型，也就是说编译器不检查类型合法性
- Dynamic Binding 运行时才能知道方法被如何执行，也就是消息机制 (messaging)
- Dynamic Loading 允许动态添加类、方法等


## 起源

孙源大佬在 [博客](http://blog.sunnyxx.com/2016/08/13/reunderstanding-runtime-0/) 中说过，OC[^1] 其实是 C 语言与 SmallTalk[^2] 思想结合的产物。

与同属 SmallTalk 学派的语言 Java, Python 和 Ruby 一样，OC 具有面向对象、动态类型和反射式等特点。

> Objective-C = C + Preprocessor + Runtime

[SmallTalk 领先了时代 20 年](https://blog.youxu.info/2010/02/28/why-mac-os-x-for-programmers/)，至今 OC 仍然没有实现它的全部特性。

## Runtime 里有什么

Runtime 的源码可以在 [RetVal/objc-runtime](https://github.com/RetVal/objc-runtime) 这里找到，甚至可以 Debug。

主要包含如下几个方面，后续会逐个总结。

### Class/Object 与 isa

### MetaClass

经典图再次镇楼：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2021-12-23-class-diagram.png)

### Method/IMP/SEL

### Category

### Messaging

### Swizzling

### 其它常用方法

++++++

[^1]: https://zh.wikipedia.org/wiki/Objective-C
[^2]: https://zh.wikipedia.org/zh-hans/Smalltalk



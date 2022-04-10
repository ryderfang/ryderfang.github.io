---
title: "ObjC 之 技术路线图"
date: 2021-12-23T17:32:58+08:00
categories: [ObjC, Interview]
tags: [objc]
---

{{< lead >}}
> 本文可以作为面试八股的准备指南
{{< /lead >}}

很早之前看过一个 [前端 Roadmap](https://github.com/kamranahmedse/developer-roadmap)，图做的非常漂亮。最近发现有人做了类似的 [移动端 Roadmap](https://github.com/godrm/mobile-developer-roadmap)，

其中 iOS 是这样的：

<!--more-->

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2021-12-23-iOS_roadmap_v1.0.png)

还有 Swift 的，暂时先不关注了。这里综合一下形成文字版，方面查缺补漏。

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2021-12-23-sepline.png)

iOS 的体系结构如下图：

<center>

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2021-12-23-98Rtfb.jpg)

<font size=2>[Ref: iOS abstraction layers](https://livebook.manning.com/book/ios-development-with-swift/chapter-1/7)</font>

</center>

需要重点关注的有下面几个方面：

{{< alert >}}
demo 工程：[https://github.com/ryderfang/iosBagu](https://github.com/ryderfang/iosBagu)
{{< /alert >}}

## Foundation

### ARC/MRC 与 内存管理

`ARC is supported in Xcode 4.2 for OS X v10.6 and v10.7 (64-bit applications) and for iOS 4 and iOS 5.`

现在除了一些老项目，基本没有 MRC 为主的代码了，所以只需要简单了解下 MRC 与 ARC 的区别即可

1. MRC 需要手动写 dealloc，并且一定要最后再调用父类的 dealloc；
   ARC 一般不需要写 dealloc，也不需要调用 [super dealloc]。移除 NSNotification Observer 和 KVC Observer 例外。

2. 在 ARC 的工程中使用 MRC，需要在工程中设置源文件的编译选项 `-fno-objc-arc`

* Tagged Pointer

* OC 对象与 CF 对象转换

  - `__bridge`, `__bridge_retained`, `__bridge_transfer`
### AutoReleasePool

* AutoReleasePool 的数据结构

* AutoReleasePool 与 @autoreleasepool

### Block 🔥

* __weak 与 __block

* block 的结构体类型

* block 如何捕获外部变量

* 循环引用 与 [Weak-Strong Dance](Foundation/Notes/weak-strong-dance.md)

### Category 🔥

* load 加载时机

* load 与 initialze

* 方法加载时机

* 如何添加属性 - 关联对象

* category 与 class-extension

* category 覆盖原类方法的原理

* category 同名方法调用顺序

### HotPatch

* JSPatch 的原理

### KVC 与 KVO 

* KVC 是如何实现的

* KVO 的原理

* KVC 与 KVO 有什么联系与区别

### MultiThread 多线程 🔥

* 哪些多线程方法

* GCD 与 NSThread, NSOperationQueue

* 互斥锁与自旋锁
### Network 🔥

* NSURLSession 与 NSURLConnection

* 常用网络库

  - [AFNetworking](https://github.com/AFNetworking/AFNetworking) (ObjC)

  - [Alamofire](https://github.com/Alamofire/Alamofire) (Swift)
### NSTimer 🔥

* timer 与 Runloop

* timer 导致循环引用的产生与解决

### Property 🔥

* 不指定任何关键字时，默认的类型：

  - OC 对象：`atomic, readwrite, strong`
  - 数值对象：`atomic, readwrite, assign`

* 不同属性的区别

> 1. atomic/nonatomic
> 2. readonly/readwrite
> 3. (retain, MRC)/assign/weak/strong/unsafe_unretained/copy

* copy 与 assign

* weak 与 copy

* weak 与 __unsafe_unretained

* atomic 并不是线程安全的

* 如何实现一个弱引用容器
   - \+ [NSPointerArray weakObjectsPointerArray] 弱引用数组
   - \+ [NSMapTable weakToWeakObjectsMapTable] 弱引用表
   - \+ [NSHashTable weakObjectsHashTable] 弱引用 hash 表
   - \+ [NSValue valueWithNonretainedObject:] 弱引用对象

### Runloop 🔥

* Runloop 与线程的关系

* mode

* source0 & source1

* 如何实现一个常驻线程

### Runtime 🔥

系列文章：[Runtime 是个啥？](/categories/runtime/)

* Method Swizzling

* [从 Meta 说起](/posts/2022/meta-class/)

* [Class, Object 与 isa](/posts/2022/class-object-isa/)

* 消息转发

* `NSObject` 与 `<NSObject>`

### 其他知识

* NSNotification 原理

* id 与 `instancetype`

* nil, Nil, NULL, NSNull

* NSPredicate 谓词

## UIKit

### UIView 与 CALayer

* bounds 与 frame

* setNeedsDisplay 与 layoutIfNeeded

### 常用 UI 组件

* UIScrollView

* UITableView

   - cell 复用原理

* UICollectionView

### AutoLayout

* Masonary 原理

* VFL 语法

* 约束 Constraints

### UIResponder

* touch events

* hitTest / pointsInside

* 事件传递与响应链

### 离屏渲染

* layoutSubview 与 drawRect

### 性能优化

* 图片渲染过程

* 卡顿优化

## Core 系列

### Core Graphics

* 高效绘制圆角

### Core Data

### AVFoundation


## 架构能力

### 设计模式

### 架构模式

* MVC

* MVP

* MVVM

### 响应式编程

### 重构与解耦

### 组件化

---

更多面试题：

1. https://github.com/LGBamboo/iOS-Advanced
2. https://www.jianshu.com/p/e709fde38de3
3. https://www.jianshu.com/p/d9a39ab1d526

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-10-KJGbb4.jpg)
---
title: "Objc 路线图"
date: 2021-12-23T17:32:58+08:00
categories: [ObjC]
tags: [Roadmap, ObjC]
resources:
- name: "featured-image"
  src: "featured-image.jpg"
---

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

## Foundation

### I. ARC/MRC 3️⃣

`ARC is supported in Xcode 4.2 for OS X v10.6 and v10.7 (64-bit applications) and for iOS 4 and iOS 5.`

现在除了一些老项目，基本没有 MRC 为主的代码了，所以只需要简单了解下 MRC 与 ARC 的区别即可

1. MRC 需要手动写 dealloc，并且一定要最后再调用父类的 dealloc；
   ARC 一般不需要写 dealloc，也不需要调用 [super dealloc]。移除 NSNotification Observer 和 KVC Observer 例外。

2. 在 ARC 的工程中使用 MRC，需要在工程中设置源文件的编译选项 `-fno-objc-arc`

### II. AutoReleasePool 4️⃣

* AutoReleasePool 的数据结构

* AutoReleasePool 与 @autoreleasepool

### III. Block 5️⃣

* block 的结构体类型

* block 如何捕获外部变量

* 循环引用 与 [Weak-Strong Dance](Foundation/Notes/weak-strong-dance.md)

### IV. Category 5️⃣

* load 加载时机

* load 与 initialze

* category 覆盖原类方法的原理

* category 同名方法调用顺序

### V. HotPatch 1️⃣

* JSPatch 的原理

### VI. KVC 2️⃣

* KVC 是如何实现的

### VII. KVO 4️⃣

* KVO 的原理

### VIII. MultiThread 4️⃣

* 哪些多线程方法

* 互斥锁与自旋锁
### IX. Network 3️⃣

* NSURLSession 与 NSURLConnection
### X. NSTimer 5️⃣

* timer 与 Runloop

* timer 导致循环引用的产生与解决

### XI. Property 5️⃣

* 不同属性的区别

* weak 与 copy

* atomic 并不是线程安全的

* 如何实现一个弱引用容器
   - \+ [NSPointerArray weakObjectsPointerArray] 弱引用数组
   - \+ [NSMapTable weakToWeakObjectsMapTable] 弱引用表
   - \+ [NSHashTable weakObjectsHashTable] 弱引用 hash 表
   - \+ [NSValue valueWithNonretainedObject:] 弱引用对象

### XII. Runloop 4️⃣

* Runloop 与线程的关系

* 如何实现一个常驻线程

### XIII. Runtime 5️⃣

一图胜千言，引用 Runtime 工程师 [Greg Parker](http://www.sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html) 在其博客中给出的经典图

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2021-12-23-class-diagram.png)
## UIKit

### UIView 与 CALayer

* bounds 与 frame

* setNeedsDisplay 与 layoutIfNeeded


### 常用 UI 组件

* UIScrollView

* UITableView

* UICollectionView

### AutoLayout

* Masonary 原理

### UIResponder

* touch events

* hitTest

### 离屏渲染

* layoutSubview 与 drawRect

## Core 系列

### Core Graphics

* 高效绘制圆角

### Core Data

### AVFoundation


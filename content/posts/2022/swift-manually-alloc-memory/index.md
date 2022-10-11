---
title: "Swift 中手动管理内存"
date: 2022-10-11T16:56:24+08:00
categories: [Swift, ARC, Memory]
tags: [swift]
---

> App 开发不可避免地要和内存问题打交道，`OOM (Out Of Memory)` 也是开发者非常头疼的问题。

为了方便复现内存问题，我们可以手动分配一个大内存，这样在 App 启动之后根据用户的操作路径就有可能复现这类问题。

在 Swift 中如何分配大内存呢？我们知道，Swift 一般来说变量的内存分配和销毁都是系统自动管理的 (`ARC`)，但 Swift 也为我们提供了直接访问内存的方法，
也就是 `Pointer` 类。

## 分配大内存

回到开头的问题，我们可以在代码中定义一个 `Pointer` 类型的变量，分配一块大内存让它常驻。

```swift
public class AppDelegate: NSObject, AppDelegateProtocol {
     private var p: UnsafeMutablePointer<UInt8>?

     public override init() {
        super.init()
        // ...
        p = UnsafeMutablePointer.allocate(capacity: Int(1.8 * 1024 * 1024 * 1024))
        p?.initialize(repeating: 0, count: Int(1.8 * 1024 * 1024 * 1024))
    }
}
```

`UInt8` 是占用一个字节的整型数据，所以上面我们分配了 1.8G 的内存！

> Tip: 超过 2G 内存 app 就很容易被系统杀掉：Terminated due to memory issue.

## 手动内存管理

https://medium.com/@shoheiyokoyama/manual-memory-management-in-swift-c31eb20ea8f


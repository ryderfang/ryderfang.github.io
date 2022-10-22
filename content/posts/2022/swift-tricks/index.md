---
title: "Swift 踩坑记"
date: 2022-10-22T21:50:02+08:00
categories: [Swift]
tags: [trick]
---

开发过程中遇到的一些坑，记录一下。

## Optional

可选类型作为 Swift 的一个标志性语法，有一些反直觉的坑。

### nil 判断

一个数组，比如这样的类型 `[Int?]`，想移除它最后的空值，直觉的写法是：

```swift
var ans: [Int?] = [1,2,nil,nil]
while ans.last == nil {
    ans.removeLast()
}
```

然而！结果并不是想的那样，`nil` 并没有被移除。为什么？

我们去看 `last` 方法的定义就会发现：

```swift
@inlinable public var last: Element? { get }
```

返回值是 `Element?` 类型，在这里就是 `Int??` 或者 `Optional<Optional<Int>>` 类型

> 嵌套的 `Optional` 总是非空的

所以上面的写法要改成：

```swift
while let last = ans.last, last == nil {
    ans.removeLast()
}
```


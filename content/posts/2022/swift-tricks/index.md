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
## compactMap

我们知道 `compactMap` 非常有用，它的原型是：

```swift
/*
@return
  An array of the non-nil results of calling transform 
  with each element of the sequence.

@param transform
  A closure that accepts an element of this sequence 
  as its argument and returns an optional value.
*/
func compactMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]

```

比如，一个数组 `[3,9,20,nil,nil,15,7]`，使用 `compactMap` 后：

```swift
let nums = [3,9,20,nil,nil,15,7]
let ans = nums.compactMap { $0 }
// [3,9,20,15,7]
```
> Good !

但是！如果接收 `compactMap` 结果的类型是 `[Int?]` 类型的呢？

```swift
let ans: [Int?] = nums.compactMap { $0 }
// [3,9,20,nil,nil,15,7]
```

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-12-03-SZsIv9.jpg)

这个时候再加一层 `map` 才会得到预期的结果

```swift
let ans: [Int?] = nums.compactMap { $0 }.map { $0 }
// [3,9,20,15,7]
```

> Why ?

在 [Swift 源码](https://github.com/apple/swift/blob/7123d2614b5f222d03b3762cb110d27a9dd98e24/stdlib/public/core/FlatMap.swift) 中发现：

```swift
@inlinable // lazy-performance
  public func compactMap<ElementOfResult>(
    _ transform: @escaping (Elements.Element) -> ElementOfResult?
  ) -> LazyMapSequence<
    LazyFilterSequence<
      LazyMapSequence<Elements, ElementOfResult?>>,
    ElementOfResult
  > {
    return self.map(transform).filter { $0 != nil }.map { $0! }
  }
```

看起来还挺正常？

我怀疑编译器根据返回类型，直接赋值而没有执行 `compactMap` 方法本身。
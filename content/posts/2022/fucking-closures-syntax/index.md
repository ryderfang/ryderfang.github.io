---
title: "在 Swift 中如何定义 Closures"
date: 2022-05-02T18:18:26+08:00
categories: [Swift, Closures]
tags: [closures]
---

在 [在 ObjC 中如何定义 Block](/posts/2017/how-to-declare-block-in-oc/) 中总结了 OC 中 block 的语法。

不知道 Swift 有没有类似 `fuckingblocksyntax.com` 的网站，反正我这篇是叫 `fucking-closures-syntax` 😬

## 使用方法

```swift
{ (parameters) -> returnType in
    statements
}
```

### 局部变量

<details>
<summary>语法定义</summary>

```swift
var closureName : (parameters) -> returnType = {
    (parameters) -> returnType in
    // statements
}
```

</details>

例如：
```swift
let handler : (Float) -> Void = {
    (_ arg: Float) -> Void in
    print(arg)
}

// 这里参数类型可以省略
let handler : (Float) -> Void = {
    arg in
    print(arg)
}

// 如果闭包内只有一个表达式，return 也可以省略
var completion : ((Float) -> Int)? = {
    Int($0) * 2
}
```

### 属性

<details>
<summary>语法定义</summary>

```swift
var closureName : (parameters) -> returnType
```

</details>

例如：
```swift
var defaultHandler : () -> Void = {
    print("Hello Closures.")
}
```

我们有时候需要定义一个可能为空的闭包，那么可以使用可选值。

```swift
var handler : ((Float) -> Void)?

// 在使用时更安全，不需要额外判空
self.handler?(2.0)
```

### 方法参数

```swift
func methodA(closure: () -> Void) {
    closure()
}

func methodB(closure: (_ a : Float) -> Void) {
    closure(3.0)
}

func methodC(closure: (_ a : Float) -> Void, arg: Int) {
    closure(3.0)
}
```

### 函数调用

对于上述参数是闭包的方法，调用时，我们可以忽略一些细节。

* 如闭包是函数最后一个参数，可以直接忽略实参标签
* 可以用 `$0` `$1` 代替闭包的实参，避免写 `arg in`
* 对于操作类闭包，甚至可以省略到只保留操作符

```swift
self.methodA {
    print(2.0)
}

self.methodB {
    print($0)
}

self.methodC(closure: { a in
    print(a)
}, arg: 0)
```

### typealias

```swift
typealias CompletionHandler = ((Float) -> Int)?
```
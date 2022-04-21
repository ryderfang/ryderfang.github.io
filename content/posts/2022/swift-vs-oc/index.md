---
title: "Swift 与 OC 有哪些不同"
date: 2022-04-10T15:15:57+08:00
categories: [ObjC, Swift]
tags: [swift]
---

{{< alert info >}}
参考：<a href='https://swift.bootcss.com/' target='_blank'>swift.bootcss.com</a>
{{< /alert >}}

## 基本语法

### 分号

* 分号在 Swift 中不是必须的，当然在一行中多个语句间还是需要的。

> 越看越觉得像 Python :)

### 空格

* Swift 对于空格有着一定的约束，相对 OC 来说更严格，但又没有 Python 那么精确 （不需要游标卡尺 🤡）

```swift
// '=' must have consistent whitespace on both sides
var a= 1 + 2
// '+' is not a postfix unary operator
var a = 1+ 2
// Consecutive statements on a line must be separated by ';'
var a = 1 +2
// ok
var a = 1 + 2
// ok, not recommand
var a = 1+2
```

### switch

* Swift 中的 switch 支持任意类型，而 OC 只支持整型及能转换成整型的类型。

* 在 Swift 中 break 并不是必须的。某个 case 匹配成功后，会在执行完代码后自动跳出；而 OC 以及 C/C++ 会继续匹配，
—— 这种方式叫做 **贯穿**。在 Swift 中可以使用 `fallthrough` 关键词以支持这种特性。

* Swift 中的 switch 支持 where 语句以添加额外的条件。

### 函数嵌套

* Swift 支持在函数内部定义函数。

```swift
func testVariable () {
    var a : String? = "1"
    func _inerfunc() {
        print("hello", a ?? "2")
    }
    _inerfunc()
}
```

### 继承

* Swift 继承自父类的方法，重写时，需要加 `override` 关键字。OC 不需要。

### 区间运算符

* 在 Swift 中 [a, b] 的区间可以用 `a...b`

* [a, b) 可以表示成 `a..<b`

* 还有 `[a...]` 和 `[..<b]` 等

## 类型

> Swift 是一个类型安全 (type safe) 的语言。

### typealias 类型别名

* 这个在 OC 中可以使用 `typedef` 实现。

### 隐式转换

* Swift 有严格类型定义，不能隐式转换。

比如 if 语句中的条件，在 OC 中可以使用整数，但在 Swift 中只能是 Bool 型。

```swift
let a = 1
// Type 'Int' cannot be used as a boolean; test for '!= 0' instead
if (a) {

}
```

### Optional 可选值

* 这是 OC 没有的特性，避免了很多判空的逻辑代码。在链式调用时，也更方便。


### 闭包与 block

* Swift 中的闭包与 OC 中的 block 类似，都是将一段代码封装起来，用于参数、返回值等，也都可以捕获外部变量。

* 但也有不同之处：

  - 本质不同，闭包本质是个函数，但 block 是一个结构体。

  - 闭包写起来更简洁、更灵活。有多种类型：自动闭包、尾随闭包、逃逸闭包 & 非逃逸闭包等。

### enum 枚举

* Swift 中的 `enum` 可以包含方法，而 OC 不行

### Tuple 元组

* 这是 OC 没有的类型，用于返回一组数据，如 (404, "Not Found")

### nil

* Swift 中的 nil 表示可选值类型的值为空，不能用于确定的类型。而 OC 中，它是一个空指针的概念，只能对于对象。

* 可选值可以是整型，如 `var a : Int? = nil`

### ?? 空合

* 是对一个可选类型解析，类型于 OC 中的 `a ?: b`

```swift
// if a == nil, return b
a ?? b
// is equal to 
a == nil ? a! : b
```

## 高级特性

### 函数

* Swift 中的函数，可以不指明返回值，默认返回的是 `()` —— 空元组。而不是 `Void`

* Swift 可以给函数参数设置标签（别名），`_` 表示不需要标签。

* 单行表达式的函数，可以直接省略 `return`；常用于 `get` 方法。

* 默认函数参数是不能修改的，需要使用 `inout` 标明需要修改的参数。
### 结构体与类

* struct 在 OC 中并不是一等公民，但在 Swift 中，是与 class 同等地位的对象封装。

ref: [Choosing Between Structures and Classes](https://developer.apple.com/documentation/swift/choosing_between_structures_and_classes)

### 值类型与引用类型

`值类型` 被赋值给另一个变量时，会进行 copy 操作，以确保新变量的修改不会影响原来的变量值。
而 `引用类型` 的赋值是一次指针赋值，新旧变量指向同一块内存。

* Swift 中 String, enum, struct 是值类型，class 是引用类型。

* OC 中仅有基本数据类型、基础 struct 是值类型。

### 属性包装器

* Swift 中的新特性，关键词 `@propertyWrapper`

用于将某个属性的实际值隐藏起来，对外暴露封装过的值。


### 类方法

* `static` 和 `class` 在 `func` 前都表示类型方法，后者表示可被子类继承

* Swift 中可以为类、结构体和枚举定义类型方法


### extension 扩展

* Swift 中的扩展与 OC 中的 category 类似，也有一些不同

  - 扩展是没有名字的
  - 扩展可以添加属性
  - 扩展不能重写已有方法，但分类可以（覆盖）
  - 扩展中的功能，可被扩展定义之前的实例使用；但分类方法必须被 import 后才可见

### protocol 协议 

* Swift 中的协议支持指定属性
* Swift 中的协议可以指定初始化方法，实现时需要使用 `required` 关键字
* Swift 中的协议可以组合，使用 `ProtocolA & ProtocolB` 变成一个新的协议类型
* Swift 中的协议，可以提供默认实现

### 泛型

* 类似 C++ 中的模板语法特性，OC 中没有。

### actor 类型

* Swift 中新增的类型

> To be continued...
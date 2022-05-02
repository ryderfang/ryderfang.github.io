---
title: "Swift 中的关键字"
date: 2022-04-26T12:18:16+08:00
categories: [Swift]
tags: [swift, keyword]
---

> 熟悉一门语言，可以从熟悉它的关键字入手。

本文列举一下 Swift 区别 OC 的一些特有关键字吧。这里仅列举常用的，完整的关键词列表可以参考：[Swift 语言参考/关键字和标点符号](https://swift.bootcss.com/03_language_reference/02_Lexical_Structure#keywords-and-punctuation)

## @autoclosure

> Closures are self-contained blocks of functionality that can be passed around and used in your code. Closures in Swift are similar to blocks in C and Objective-C and to lambdas in other programming languages.

—— [Swift 官方教程](https://docs.swift.org/swift-book/LanguageGuide/Closures.html)

自动闭包，也是一种闭包。

自动就是省略了 `{}`，系统自动将一个表达式转换成闭包。有个前提是这个闭包不能有参数。否则会收到编译错误：

> Argument type of @autoclosure parameter must be '()'

```swift
private func _autoclosure(_ bar: @autoclosure () -> Bool) {
    if bar() {
        print(#function)
    }
}
```

闭包是个值得讨论的话题，有机会单独写一篇文章。

## @escaping

逃溢闭包，是指闭包的生命周期被延长。正常情况下在闭包作为函数参数时，函数执行完，闭包就被释放了。

但是，如果闭包被缓存或延迟执行，生命周期被延长到函数执行之后。就需要显示指明 `@escaping`，否则会编译报错。

因为 Swift 3 以后，闭包默认都是 `nonescape` 的。

> Escaping closure captures non-escaping parameter 'bar'

```swift
private func _escapingclosure(_ arg1: Int, _ arg2: Int, _ bar: @escaping (_ a: Int, _ b: Int) -> Int) {
    let concurrentQueue = DispatchQueue(label: "com.ryder.concurrent.queue1", attributes: .concurrent)
    concurrentQueue.asyncAfter(wallDeadline: .now() + 1.5) {
        print(bar(arg1, arg2))
    }
}
```

## @convention

也是用于修饰闭包的

`@convention(c)` 修饰的闭包会返回 C 类型的函数指针，用于传给参数是函数指针的 C 方法。

`@convention(block)` 修复的闭包会返回 block，用于传给参数是 block 的 OC 方法。

## defer

defer 后面接一个闭包，表示推迟这个闭包执行到 defer 语句的作用域之后。

```swift
private func _defer() {
    var num = 1
    defer { print("Defer: \(num)") }
    num += 1
    print("Number: \(num)")
}
// Number: 2
// Defer: 2
```

> defer 内的闭包不会持有外部值。

More: [喵总遇到的 defer 死锁问题](https://onevcat.com/2018/11/defer/)

## deinit

```swift
deinit {
    print(String(format: "%@ dealloced.", String(describing: self)))
}
```

析构方法。

## extension

扩展，类似于 OC 的 category。

扩展的作用主要有：

* 添加计算实例属性和计算类型属性
* 定义实例方法和类型方法
* 提供新初始化器
* 定义下标
* 定义和使用新内嵌类型
* 使现有的类型遵循某协议

> 类型方法的定义，所有类型都可以有类型方法，不限于 class/struct/enum。都可以使用 `static func`，
而在 class 中还可以使用 `class func`。

注意：扩展不能直接定义存储类属性，也就是不能有属性的实例。也没有 OC 的关联对象可以使用 （当然我们可以桥接一个 OC 实现）。

那么怎么办呢？有个取巧的办法是定义一个类变量。

```swift
extension MyOCFunction {
    private static var _temp = 0
    var fact: Int {
        get {
            return MyOCFunction._temp
        }
        set {
            MyOCFunction._temp = newValue
        }
    }
}
```

## fallthrough

贯穿。Swift 中的 case 默认是非贯穿的，也就是 case 执行完之后自动退出，所以也就不需要 break 了。

但是，如果你希望像其他语言一样，多个 case 执行一段逻辑，则可以在 case 后使用 `fallthrough`

## fileprivate

Swift 共有五种访问控制关键字，从高到低：

* `open`, 可以被本模块和外部模块任意访问
* `public`, 与 open 唯一的区别是不能被外部模块继承和重写 (can't subclass or override outside the module)
* `internal`, **默认** 的级别，本模块内任意访问，不能被外部访问
* `fileprivate`, 当前文件可见
* `private`, 实体作用域可见，对于属性来说，仅当前类和它的 externsion 可见

这几个关键字可以用于修饰实体，如属性、基本类型、函数等。

## final

* final 修饰类，表示这个类不对被继承 （不能修饰 struct/enum，因为它们本来就不会被继承）
* final 修饰类中的属性、方法，表示不能被子类重写
* 显然，final 和 open 关键字是互斥的

## guard

guard 守卫，用于校验某个条件，并退出当前作用域。

在 `guard..else` 块中必须使用 `return/throw` 显式退出。

```swift
let temp = 0
guard temp != 0 else {
    print("zero checked.")
    return
}
```

## inout

inout 用于在函数内修改值类型数据。在调用时，需要在参数前加 `&` 

```swift
var num = 1
self._inout(num: &num)

private func _inout(num: inout Int) {
    num *= 2
}
```

inout 的工作方式是这样的（copy-in-copy-out）：

- 函数调用时，参数的值被拷贝。
- 函数体内部，拷贝后的值被修改。
- 函数返回后，拷贝后的值被赋值给原参数。

## let/var

let - constant 修饰常量，仅可赋值一次
var - variable 修饰变量，可以被改变

不管是常量还是变量，定义都遵循标识符的 [定义标准](https://docs.swift.org/swift-book/ReferenceManual/LexicalStructure.html#ID412)，我们可以使用各种 Unicode 字符包括 emoji 来定义名称。

```swift
private func _var() {
    var 🐶🐮 = "dogcow";
    🐶🐮 = "cowdog"
    print(🐶🐮)
    let 💩 = "shit"
    print(💩)
}
```

## lazy

lazy 用在属性中，表示这个属性只有在被访问到才会执行初始化。也就是所谓的“懒加载”，避免的无效的内存占用。

另一种用法，在序列，如 Array 的计算时，可以使用 lazy 只计算关心的值，如：

```swift
// 只输出两次 `Calculating..`
private func _lazy () {
    let array = Array(0..<100)
    let incArray = array.lazy.map{(item) -> Int in
        print("Calculating..")
        return item + 1
    }
    print(incArray[0], incArray[8])
}
```

如果没有 `lazy`，那么 map 会被调用 100 次。

ref: https://swift.gg/2016/03/25/being-lazy/

## mutating

对于 struct/enum 值类型对象来说，使用 mutating 修饰的方法才能修改它们的属性。

```swift
struct Meeting {
    var name : String
    var date : Date?
    init() {
        self.name = ""
        self.date = Date()
    }
    
    mutating func cancel() {
        self.date = nil
    }
}
```

## Optional

可选类型。

> 这是 Swift 区别 OC 的一个主要特征。

## prefix/infix/postfix

用于修饰自定义操作符的，prefix 表示操作符在变量前，同理 infix 和 postfix 分别是中缀表达式和后缀表达式。

自定义操作符方法，必须是 `static` 的。

```swift
extension Vector2D {
    static prefix func +++ (vector: inout Vector2D) -> Vector2D {
        vector += vector
        return vector
    }
}
```

## struct/class

结构体与类的区别，在 [之前](/posts/2022/swift-vs-oc/#结构体与类) 已经介绍过，不再赘述。

## tuple

元组，通过圆括号和分号，将不同的类型组成在一起，形成一个新的类型。tuple 甚至可以嵌套包含别的 tuple。

> A tuple type is a comma-separated list of zero or more types, enclosed in parentheses.

通常用于函数返回值。

一个有趣的事实：

`Void` 是 `()` 的 `typealias`，其实就是一个空的 tuple

## typealias

Swift 中替代 `typedef` 的关键字。
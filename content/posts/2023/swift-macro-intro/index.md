---
title: "Swift 5.9 新特性：宏(Macro)"
date: 2023-10-26T13:02:02+08:00
categories: [Swift]
tags: []
---

WWDC2023[^1] 发布 Swift 5.9，引入了 “宏” 的新特性[^2]。

> 必须使用 Xcode 15 才能完整使用 Macro 功能

## 概述

宏在 **编译期** 对源码进行替换，减少编写重复代码。这是一种增量操作，并不会修改或删除现有代码。

与 C/C++ 的宏不同，Swift 的宏会经过编译检查，并不是简单的字符串替换。

Swift 宏与语法树深度结合，已经是一种自定义编译过程的方式。

![]()

另外，要创建宏，必须使用 Swift Package，在 File -> New -> Package -> Swift Macro 创建，
并依赖 `swift-syntax 590.0.1`

![]()

有两类宏：

## 独立宏 (Freestanding Macros)

以井号 `#` 开头，语法上又分成两类[^3]

### @freestanding(declaration)

声明宏

```swift
@freestanding (declaration, names: arbitrary)
macro jsonModel(String)

struct JSONValue: Codable {
  #jsonModel("""
  "name": "Produce",
  "shelves": [
    {
      "name": "Discount Produce",
      "product": {
        "name": "Banana",
        "points": 200,
        "description": "A banana that's perfectly ripe."
      }
    }
  ]
  """)
}
```

### @freestanding(expression)

定义宏

```swift
@freestanding(expression)
macro #stringify<T>(_ value: T) → (T, String)

#stringify(x + y)
```

扩展成 `(x + y, "x + y")`

## 附加宏 (Attached Macros)

以 `@` 开头，有五类

### @attached(peer)

会在原方法基础上生成一个新的方法

### @attached(accessor)

添加 get/set 方法，将存储属性变成计算属性

```swift
@attached(accessor) 
macro DictionaryStorage(key: String? = nil)

struct MyStruct {
  var storage: [AnyHashable: Any] = [:]
  
  @DictionaryStorage
  var name: String
  
  @DictionaryStorage(key: "birth_date")
  var birthDate: Date?
}
```

--> 扩展成

```swift
struct MyStruct {
  var storage: [String: Any] = [:]
  
  var name: String {
    get { 
      storage["name"]! as! String
    }
    
    set {
      storage["name"] = newValue
    }
  }
  
  var birthDate: Date? {
    get {
      storage["birth_date"] as Date?
    }
    
    set {
      if let newValue {
        storage["birth_date"] = newValue
      } else {
        storage.removeValue(forKey: "birth_date")
      }
    }
  }
}
```

### @attached (memberAttribute)

给类的成员添加属性，如自动添加 `@objc` 等。

### @attached (member)

自动添加成员，如 `@OptionSet` 的使用。

### @attached(conformance)

自动添加对 `protocol` 的依赖。

## 一些提示

同一个宏可以有多个 `@attached` 修饰[^4][^5][^6]

使用 AST-Explorer 网站可以直接看到 AST 结构：[https://swift-ast-explorer.com/](https://swift-ast-explorer.com/)

参考资料：https://github.com/krzysztofzablocki/Swift-Macros

## 示例

<details>
<summary>展开查看</summary>

{{< gist ryderfang 6f3c1ee642e881b9f72052a6edab3e9b >}}
</details>

[^1]: https://developer.apple.com/videos/play/wwdc2023/10166
[^2]: https://github.com/apple/swift-evolution/blob/main/visions/macros.md
[^3]: https://medium.com/@tahabebek/swift-macros-36417a8557a
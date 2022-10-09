---
title: "一个 Swift 泛型导致 XCTestCase 失效的问题"
date: 2022-10-09T14:36:15+08:00
categories: [Swift, XCTestCase]
tags: [swift]
---

## 背景

最近在写 UT，使用 [SnapshotTesting](https://github.com/pointfreeco/swift-snapshot-testing) 对一些 UI 组件做测试。
为了方便扩展，使用了泛型([Generics](https://docs.swift.org/swift-book/LanguageGuide/Generics.html)) 。首先，有一个基类，大概是这样的：

```swift
class WidgetsTestCase<ViewClass: ViewClassProtocol>: XCTestCase {
    var sut: ViewClass!

    override func setUpWithError() throws {
        try super.setUpWithError()

        parseMockData()
        buildSut()
    }

    override func tearDownWithError() throws {
        sut = nil
        try super.tearDownWithError()
    }

    func mockFileName() -> String {
        XCTAssertTrue(false, "This function must be overrided.")
        return ""
    }

    func parseMockData() {
        let fileName = mockFileName()
        // ...
    }

    func buildSut() {

    }

    func testSut() throws {
        // ...
    }
}
```

然后对于不同的 Widgets，仅是 mock 文件和 test 方法的少许区别：

```swift
class MyCellViewTests: WidgetsTestCase<MyCellView> {
    override func mockFileName() -> String {
        return "MyCellViewData.json"
    }

    override func testSut() throws {
        try super.testSut()

        let exp = expectation(description: "wait for image loading")
        let result = XCTWaiter.wait(for: [exp], timeout: 2.0)
        if result == XCTWaiter.Result.timedOut {
            assertSnapshot(matching: sut, as: .image)
        }
    }
}
```

但是在提交完代码跑 CI 流水线时发现，新写的 `MyCellViewTests` 文件只是被编译，但并没有被测试跑到。

## 问题分析

首先，由于本地环境 (**Xcode 14.0 & iOS 16.0**) 和 CI 环境 (**Xcode12.4 & iOS 14.2**) 差距较大，
虽然本地跑起来没有问题，但一时无法找到原因在哪。

* 开始怀疑是 `throws` 导致的，删除了仍然没有效果。

* 而后又删除了 `override`，问题依旧。

* 新增了一个直接继承 `XCTestCase` 的类，正常被测试。

到这里，开始怀疑跟泛型有一定的关系，然后用 `XCTestCase Generics` 关键词搜索时，发现了关键线索：

https://stackoverflow.com/questions/35273597/is-use-of-generics-valid-in-xctestcase-subclasses

同样的单测框架 `Quick` 也被提过类似的 issue：

https://github.com/Quick/Quick/issues/1060

问题原因最终指向是 Xcode 的 bug (https://developer.apple.com/documentation/xcode-release-notes/xcode-12_5-release-notes)：

> XCTest now automatically includes specialized subclasses of Swift generic test classes when running tests on macOS 11.3, iOS 14.5, tvOS 14.5, watchOS 7.4, or later OS versions. This allows you to use generics to improve reusability of test classes.

## 解决

既然暂时无法升级 CI 的 Xcode 版本，只能先想办法绕过这个问题。

新增一个测试类，手动创建并调用这些泛型类的测试方法：

```swift
class DummyWidgetTests: XCTestCase {
    override func run() {
        XCTestSuite(forTestCaseClass: MyCellViewTests.self).run()
        super.run()
    }

    // At least one func is needed for `run` to be called
    func testDummy() {

    }
}
```

提交，这次测试方法被执行到了！🎉🎉


（但是又出现了 case 失败的情况，继续苦逼调试...

*Be debugging... 🐞*

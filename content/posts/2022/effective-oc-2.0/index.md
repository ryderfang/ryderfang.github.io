---
title: "一文学完《Effective Objective-C 2.0》"
date: 2022-04-07T21:23:42+08:00
categories: [Tech, Article]
tags: [objc]
---

{{< lead >}}

> 查了下订单，这本书买了 4 年多，还没看完！

{{< /lead >}}

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-07-book.jpeg)

所谓 flag，永远也完不成 😢

毕其功于一役，这次快速啃完这本书，吸收一些最佳实践。

这本书完整的书名是 《Effective Objective-C 2.0：编写高质量 iOS 与 OS X 代码的 52 个有效方法》，第一版写作于 2014 年，2017 年重印，距今已经比较长的时间了，那么，

> 这 52 条规则是不是都还适用呢？

带着这个疑问，快速过一遍！

## 基础概念

### 1. 起源

OC 是 C 的超集，是 `C + Object`。

OC 的消息发送机制与其他语言的函数调用的区别是：

> 前者由运行时决定，后者由编译器决定。

### 2. 减少头文件引用

这个应该所有语言 (严谨点，大部分) 都通用吧，减少模块间耦合，避免过多引用。

### 3. 字面量语法糖与下标操作

NSString, NSArray, NSNumber, NSDictionary 使用 @"", @[], @(), @{} 语法创建。

需要注意的是如果有空对象，字面量会抛异常而 crash，但是 `arrayWithObjects:` 会截断列表，只取 nil 前的元素。

而对于 NSArry 和 NSDictionary 来说，下标操作比 `objectAtIndex:` 和 `objectForKey:` 要方便一点，
但是越界一样会抛异常。

### 4. 用 const 常量代替 #define

```objc
// xx.m --> 尽量不要定义在 .h 中，如果是给别人使用，需要 extern
static const NSTimeInterval kAnimationDuration = 0.3
// xx.h
extern NSString *const XXStringConst;
// xx.m
NSString *const XXStringConst = @"VALUE"
```

* const 常量带有类型信息，会被编译器检查；#define 是单纯的字符串替换，没有任何校验。
* extern const 常量只能被定义一次 (可多次声明)，而 #define 没有限制，容易产生覆盖问题。
* tip: static const 定义在 .m 文件中，不会出现在全局符号表中。

### 5. 使用枚举

```objc
typedef NS_ENUM(NSInteger, XXState) {
    XXState1,
    XXState2,
    XXState3,
};

typedef NS_OPTIONS(NSInteger, XXOPT) {
    XXOPT1  = 1 << 0,
    XXOPT2  = 1 << 1,
    XXOPT3  = 1 << 2,
};
```

> switch 中的枚举，不要实现 default 分支，避免新加入枚举值时漏掉分支实现。

## 对象、消息与运行时

### 6. 属性

> `atomic` 是原子性的，但并不是线程安全的。

如果在一个线程多次读取某个属性的时候，有另一个线程在写，即使声明为 `atomic`，也会读取到不同的值。

> iOS 中使用同步锁开销较大，一般不使用 `atomic`

### 7. 在对象中尽量直接访问实例变量

* 在读取时，使用 `_val` 而不是 `self.val`
* 在设置时，使用 `self.val = xx`
* 不要在 `init` 和 `dealloc` 中使用 `self.val`！

    如果子类重写了某个属性的 set 方法，

    + 在 init 中，父类如果调用 set，其实是调用的子类实现，可能会出现不想要的结果
    + 在 dealloc 中，子类先释放了实例，父类再去调用 set 方法，会导致 crash

### 8. 对象相等性

* `==`： 是地址比较
* `isEqual:`： 默认也是比较指针，可以被重写。对于 `NSString`，等效于 `isEqualToString:`
* `hash`：如果对象相等，则 hash 必须相等；反之，不一定成立

### 9. 类族

`class cluster`，看起来类似于工厂模式。

系统库的集合类，如 `NSArray`、`NSDictionary` 都是类族的抽象基类。

### 10. 关联对象

> 非必要不要用。

### 11. 消息发送

`objc_msgSend` 是一个重要的概念。

`objc_msgSend` 在调用方法时，甚至使用了 "尾递归" 优化。

### 12. 消息转发

`message forwarding` 也是一个重要的概念。三步走：

1. `+ (BOOL)resolveInstanceMethod:(SEL)sel`，可用于动态添加实现
2. `- (id)forwardingTargetForSelector:(SEL)aSelector`，转发给其他对象
3. `- (void)forwardInvocation:(NSInvocation *)anInvocation`，完整的消息转发

    第三步，需要配合

    `- (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector`     
    
    使用。

### 13. 黑魔法

`Method Swizzling` 也是一个重要的概念。

> 不要滥用，难以调试

### 14. 类对象

参考：[[Runtime] Class, Object 与 isa](../class-object-isa/)

## 接口与 api

## 15. 使用前缀命名



## 协议与分类

## 内存管理 

## block 与 GCD

中文版译为 “块与大中枢派发”，无力吐嘈。

## 系统框架


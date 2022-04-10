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

### 15. 使用前缀命名

由于没有名字空间 (namespace) 机制，只能通过加前缀的方式避免符号冲突。

> 特别注意，要在分类方法名前加前缀

### 16. 使用指定初始化方法

* 指定初始化方法 (designated initializer, NS_DESIGNATED_INITIALIZER) 必须调用父类的指定初始化方法
* 本类的其他初始化方法 (便捷初始化方法，convenience initializer) 必须调用本类指定初始化方法，不能调用父类的
* 如果子类有指定初始化方法，则必须实现所有父类的指定初始化方法

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-09-o_initializerDelegation01_2x.png)

### 17. 实现 description 方法

或者 `debugDescription` 方法，用于调试输出日志。

### 18. 尽量使用不可变对象

`immutable` 也是个重要的概念。

> 对外的容器属性尽量只读，并提供读写接口。

### 19. 命名

前缀 + 驼峰式，尽可能一眼看懂作用的命名。

### 20. 私有方法加前缀 ️❓

作者建议私有方法使用 `p_` 作为前缀，这点个人觉得存疑。

实际开发中，没有必要区分 public 和 private 方法。不在头文件中的方法即为 private，
显然使用者有很多办法可以绕过这个限制。但这不重要。

这里作者提了一点很重要，不要使用 `_` 单下划线作为前缀，因为系统库也这样命名，容易无意中重载。

### 21. 处理异常

> 少用异常，除非必须 crash 的场景。一般错误使用 NSError 替代。

这里我要说一句，有些人喜欢 `NSAssert` 滥用，真是非常影响调试！😒

### 22. 理解 NSCopying

`immutable` 与 `mutable` 与 <u>深浅拷贝</u> 的概念不要混淆。

* `copy` -> `immutable`
* `mutableCopy` -> `mutable`
* `[NSArray copy]` -> 浅拷贝，即与原数组指针相同
* `[NSArray mutableCopy], [NSMutableArray copy], [NSMutableArray mutableCopy]` 都是深拷贝，会生成新的地址。

> 对于集合类成员来说，默认都没有执行 copy 操作。

> 可以使用 `-initWithXX:copyItems:YES` 方法执行逐个 copy。

## 协议与分类

### 23. 委托 delegate

Cocoa 框架大量使用，约定俗成的设计模式。

### 24. 分类

将一个大类，按功能拆成多个分类，是一种代码优化的方法。

### 25. 分类名和方法

在为系统或第三方类添加分类时，要加上自己特有的名字前缀。

与 [#15](./#15-使用前缀命名) 类似。

### 26. 分类中不要定义属性

一般也定义不了。除非使用关联对象。

### 27. 匿名类

`class-continuation` 

可以用来

* 隐藏私有变量
* 隐藏私有方法
* 隐藏私有协议

### 28. 用协议提供匿名对象

指 `id<XXProtocol> delegate` 这种形式
## 内存管理

{{< alert >}}
内存管理对于 OC 来说很重要。
{{< /alert >}}
### 29. 引用计数

对象间引用构成一颗树，根结点是 `NSApplication/UIApplication`。

`autorelease` 可以延长变量的生命期，通常用于方法返回。(MRC)

### 30. 使用 ARC

ARC 很好用。但需要注意：

* 必要的时候需要借用 autoreleasePool 管理
* CoreFoundation 对象不归 ARC 管，需要自行调用 `CFRelease`

### 31. dealloc 方法

> MRC 中 dealloc 最后需要手动调用 `[super dealloc]`，ARC 中不再需要

* 不要在 dealloc 中调用异步操作
* 不要在 dealloc 中调用属性的读写操作

在对象处于 `deallocating state` 时，不要做修改对象内容的事情。

### 32. 异常与内存管理

try 块中创建的对象需要在 @finally 中释放。ARC 下需要开启 `-fobjc-arc-exceptions` 编译标志才可以正确释放。

### 33. 弱引用

`weak` 也是一个重要的概念。

与 `unsafe_unretained` 区别在于，`weak` 会进行 `autonilling`。

### 34. @autoreleasepool 的使用

`autorelasePool` 也是一个重要的概念。

降低内存峰值 (high-memeory waterline)

### 35. 僵尸对象

`Zombie Object` 

Xcode 中有一个开关可以打开 `Enable Zombie Objects = YES`。

这样系统会替换 NSObject 的 dealloc 实现。在原类的 dealloc 中，通过 `objc_setClass`，生成一个 `_NSZombie_XXCls` 类替换原类，
在后续再向原类发送消息时，就会被转发到僵尸类中，然后输出已经被释放的类名和错误信息。

```objc
*** -[XXCls method]: message send to deallocated instance 0x7xxxx
```

### 36. 不要使用 retainCount

* ARC 下可用，MRC 下不准确。所以是无用的
* 存在自动释放池，延迟释放，所以这个值也不准
* 系统优化释放行为，可能对象引用计数不会为 0

## block 与 GCD

中文版译为 “块与大中枢派发”，无力吐嘈。

{{< alert >}}
这两者都非常重要。
{{< /alert >}}

### 37. 理解块 block

* block 也是对象，有自己的引用计数和生命周期管理
* block 是一种代替函数指针的语法结构，核心功能在 `void (*)(void *,) invoke` 函数指针
* 捕获的变量在 block 体内，invoke 将 block 本身传入以便于读取到捕获的变量
* 有栈 block、堆 block 和 全局 block，可以通过它的 Isa 指针区别

### 38. 使用 typedef 重命名 block

常用的做法

### 39. 使用 handler 块降低代码分散程度

* 就是将 block 作为参数传入，而不是使用 delegate

> 这个完全取决于实际情况，如果回调过多，还是 delegate 更好一点。

* API 设计常用同一个 block 返回结果和错误

* `NSNotificationCenter` 的设计值得学习，应该由调用者决定回调的线程

### 40. block 与 循环引用

`retain cycle` 是个使用 block 时常见的问题

某个类 retain 的 block 内部如果捕获了类本身，就会出现循环引用。此时需要及时释放 block。

### 41. 用队列代替锁

* 使用串行队列代替 `@synchronized(self)`
* 串行队列，读同步 `dispatch_sync`；写异步 `dispatch_async`，执行速度快，但性能会比同步慢，因为需要 copy block
* 并发队列，读同步，写异步，此时避免竞争需要用 `dispatch_barrier_async`，**栅栏**

> 到底什么是线程安全，很难有个准确的定义。锁机制能保证一定程度的 `thread safety`，但不绝对。

两次读之间，有写操作。这两次读的结果就可能不一样。这样算不算线程不安全？

### 42. 用 GCD 替代 performSelector

* `performSelector` 无法让编译器决定是否释放返回对象，容易内存泄露
* 使用 `dispatch_after` 代码 `performSelector:withObject:afterDelay:`

### 43. GCD 与 NSOperationQueue

`NSOperationQueue` 底层也是 GCD 实现的。但是相对来说，有一些优点：

* 更方便取消
* 可以指定依赖关系
* 可以用 KVO 了解运行状态
* 指定操作的优先级
* 代码可复用

### 44. dispatch_group

掌握几个方法的使用

```objc
dispatch_group_async(dispatch_group_t group, dispatch_queue_t queue, dispatch_block_t block);
// 成对出现
dispatch_group_enter(dispatch_group_t group);
dispatch_group_leave(dispatch_group_t group);
// 阻塞等结束或超时
dispatch_group_wait(dispatch_group_t group, dispatch_time_t timeout);
// 不阻塞等结束
dispatch_group_notify(dispatch_group_t group, dispatch_queue_t queue, dispatch_block_t block);
// 循环执行多次
dispatch_apply(size_t interations, dispatch_queue_t queue, void (^block)(size_t));
```

### 45. dispatch_once

> `dispatch_one` 性能是 `@synchronized` 的两倍以上

### 46. 不要使用 dispatch_get_current_queue

```cpp
API_DEPRECATED("unsupported interface", macos(10.6,10.9), ios(4.0,6.0))
DISPATCH_EXPORT DISPATCH_PURE DISPATCH_WARN_RESULT DISPATCH_NOTHROW
dispatch_queue_t
dispatch_get_current_queue(void);
```

这个 API 已经被弃用，不过理解其不可用的原因还是有用的。

* 返回值通常与预期不符，队列按层级组织，无法用单个队列描述当前队列。如在全局队列中 async 执行某个队列，当前队列可能是全局队列
* 可以使用 `dispatch_queue_set_specific()` 方法存储队列特有数据，类似于 TLS (Thread Local Storage)

## 系统框架

### 47. 熟悉系统框架

* Foundation 与 CoreFoundation 存在 “无缝桥接”，如 NString <-> CFString
* 常用系统库
  * CFNetwork
  * CoreAudio
  * AVFoundation
  * CoreData
  * CoreText
  * QuartzCore/CoreAnimation
  * CoreGraphics

### 48. 使用块遍历代替 for

* for...in 语法
* `enumerateObjectsUsingBlock:`

### 49. 使用 CoreFoundation 中的 collection 类

这一节感觉不是太常用。

* NSArray -> CFArrayRef: 使用 (__bridge CFArrayRef) 转换
* 反之使用 (__bridge_transfer NSMutableDictionary *)(CFMutableDictionaryRef xx)

### 50. 使用 NSCache

相比于 NSDictionary 的优势在于：

* 键不需要支持 copy
* 低内存时自动清理
* 线程安全
* 配合 NSPurgeableData 使用，实现自动清除数据

### 51. 精简 initialize 和 load 代码

* load 方法在启动时调用，先调用本类的，再调用分类的。先调用父类的，再调用子类的。子类不实现，父类不会调用。

* load 中使用其他类是不安全的

* 尽量在 initialize 方法中做初始化操作，与 load 的区别：
  * 惰性调用，使用时才调用
  * 比 load 更可靠，此时使用其他类是线程安全的
  * 遵循继承规则，子类没有实现，会调用父类的

* 也尽量不要在 initialize 中添加太多代码

### 52. NSTimer 会 retain 它的 Target

> NSTimer 也是一个重要的对象

有多种方法可以打破循环引用 。

{{< alert >}}
终于看完了！这是一本不错的书，但由于年代久远，一些概念和用法需要更新。
{{< /alert >}}

OC 这个古老的语言，如今在大厂的 `屎山` 项目中还在发挥着作用。

但是作为开发者，我们要拥抱未来！

> To Learn Swift, right now !!


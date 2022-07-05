---
title: "iOS 之 App 启动优化"
date: 2022-07-04T16:54:54+08:00
categories: [Launch, PkgSize]
tags: [launch]
---

书接上回，了解了 [发生在用户点击 App Icon 之后](/posts/2021/app-launch-process/) 的过程，可以对各个阶段做针对性优化。

回顾一下 App 启动的过程：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-07-05-jtHZBi.png)

通常来说，我们主要关注 `pre-main` 和 `启动 Tasks` 两个阶段。

## 影响因素

### 系统层

在这个阶段影响启动速度的因素有：

* 动态库的数量

* objc 类和方法的数量

* +load 方法的数量

* `__contructor__` 构造函数的数量

* `C++` 静态初始化代码的数量

### 业务层

启动的 Tasks 要具体分析，每个 app 情况不同，冷热启动也有所有不同。

需要关注的点有：

* 每个 Task 的耗时

* 核心 Task 的执行时序

* 异步 Task 占用内存/CPU 的情况


## 各显神通

### 初阶优化

容易想到的一些优化点：

1. 动态库加载耗时 -> 转静态库

2. Page fault 耗时 -> 二进制重排

3. rebase/rebind，oc setup 耗时 -> 减少冗余代码

4. +load 耗时 -> 减少 +load 使用，简化内部逻辑

5. C/C++ 构造函数耗时 -> 优化 `__contructor__` 代码

6. 启动 Task 耗时 -> 懒加载、延时加载、并行执行

7. 核心 Task 耗时 -> 专项优化，预加载

### 进阶优化

1. 图片加载优化

使用 xcassets 代码 bundle，图片读取速度提升 `80 ~ 100` 倍。

* bundle 加载图片相对慢的原因主要有两个：

  - 获取 `Key Signature` 时的位操作
  - 为了线程安全所做的加锁操作

* xcassets 相对更高效在于：

  - UIAssetManager 存在一个 `NSMapSet` 缓存
  - 未命中缓存时，会解压 Assets.car 查找
  - 再找不到才去 bundle 中找

2. `__TEXT__` 段

iOS 13 之前的系统会对 `__TEXT__` 段加密，启动时进行解密，所以这个段的大小在中低端机器上会影响启动速度。

通过 ld `-rename_section` 指令将 `__TEXT__` 段重命名，规避系统加密操作。

> 抖音就是将 `__TEXT__` 重命名成了 `__BD_TEXT__`

3. 启动 Tasks 清理

* 清理 `AppDelegate` 和 `Main` 方法中的代码

* 减少同步执行的高优任务 (Main Sync High Priority Tasks)

* 通过 TaskManager 管理所有同步低优和异步任务，减少资源消耗

4. 动态库懒加载

一般情况下 `dyld` 会递归分析 app 依赖的所有动态库并自行加载。

* 首先断开系统链接

使用 CocoaPods 的工程可以在 Podfile 中修改

```bash
new_xcconfig = new_xcconfig.sub('-framework "XX"', "")
```

* 手动加载

使用 `dlopen` 或者 `-[NSBundle loadAndReturnError:]` 来实现。

> 仅限于放在 ipa/Frameworks 目录下与主 app 同签名的动态库加载。

* 调用

想要在动态库加载前使用动态库中的类是不行的。

对于 OC 来说，可以使用 `NSClassFromString` 的反射方法，但是如果这个库已经被业务广泛使用，改造量会比较大。

还有一种比较 Trick 的方案：

* 使用宏定义 `#define DyLibClassA ProxyClassB`
* 将业务调用类转发到代理类中，实现所有 `DyLibClassA` 中的接口和协议

## 后记

优化之路无穷无尽，特别是在国内巨型 App 大行其道的今天，大家绞尽脑汗想出各种奇技淫巧只为那几千字节的优化。

我想说的是，

> 最大的优化应该是精简无效的业务代码，删除无用的功能，拒绝垃圾需求。


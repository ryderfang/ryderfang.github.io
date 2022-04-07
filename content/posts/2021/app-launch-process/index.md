---
title: "发生在用户点击 App Icon 之后"
date: 2021-12-28T16:18:03+08:00
categories: [iOS, Performance]
tags: [launch]
---

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-07-launch.jpg)

本文讨论一下 iOS 的 App 从用户点击图标开始到 App 完全可用的过程。苹果开发者文档有这样一篇文章：

[Responding to the Launch of Your App](https://developer.apple.com/documentation/uikit/app_and_environment/responding_to_the_launch_of_your_app?language=objc)

有个主要的流程图：

<center>

<img src='https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2021-12-28-GZXEUO.jpg' width='520'>
</img>

<font size=2>ref: [About the App Launch Sequence](https://developer.apple.com/documentation/uikit/app_and_environment/responding_to_the_launch_of_your_app/about_the_app_launch_sequence?language=objc)</font>

</center>

另外，还有一篇介绍如何优化启动速度的文章: 
[Reducing Your App’s Launch Time](https://developer.apple.com/documentation/xcode/reducing-your-app-s-launch-time)
，毕竟只有准确了解了启动中做了哪些事，才能更针对地进行优化。

这里还参考了以下几篇文章：

[1]: [iOS App 启动优化](https://www.jianshu.com/p/024b3d847fe0)

[2]: [iOS App 从点击到启动](https://www.jianshu.com/p/231b1cebf477)

[3]: [深入了解 App 启动过程](https://www.jianshu.com/p/e7a9e14205ac)

总结一下，整个启动过程分成四步：

## 1. 系统内核加载

> 应用程序由系统内核 XNU 加载，与此同时会加载一个叫 `dyld`的程序。

内核主要做了这几件事：

* 创建进程

* 加载解析可执行文件 (exec_activate_image)[^2]: 主要工作是对 Mach-O 进行检查，并将文件复制到内存中。

* 接下来会根据 Mach-O 的 load commands 中指定的信息来加载启动 `dyld`

更加详细深入的信息可以参加滴滴技术公众号上的两篇：

[XNU、dyld 源码分析，Mach-O 和动态库的加载过程 (上)](https://mp.weixin.qq.com/s/I60p2M-IHDmeUanDUkFdVw)

[XNU、dyld 源码分析，Mach-O 和动态库的加载过程 (下)](https://mp.weixin.qq.com/s/fdDPyjRkVf9AdWiikBagHg)

Mach-O 格式[^1]：

<img src='https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-07-Gj646G.png' width='360'>
</img>

Mac 与 iOS 仅在应用层实现上有一些差别，可执行文件的格式也都是 Mach-O 的。所以，Mac App 与 iOS App 启动流程是差不多的。

{{< mermaid >}}
graph TD
    A(Cocoa) --> | Mac | B(Media)
    E(Cocoa Touch) --> | iOS | B
    B --> C(Core Services)
    C --> D(Core OS)
{{< /mermaid >}}
## 2. pre-main 阶段

这里指 main 函数之前，内核加载 app 之后的一些事。主要是 `dyld` 的工作：

* 加载程序所需的动态库

包括分析依赖、验证有效性 (是否符号当前系统架构)，使用 `ImageLoader` 加载进内存

* rebase/rebind

为了安全性，苹果采用了 ASLR (Address space layout randomization)[^3] 技术，这样 app 实际加载地址会有偏移。

需要通过 rebase 对所有指向进程内的符号进行地址调整，同时使用 bind 处理 dylib 外部的符号。

* ObjC setup

Runtime 的初始化，ObjC 类的注册，selector 唯一性检查，Category 注册，Protocol 读取等。

* Initializers

这一阶段会调用所有类的 load 方法，执行带 attribute((constructor)) 修饰的 C++ 方法，非基本类型 C++ 静态变量创建

可以在 iOS 任一对象的 `load` 方法处打断点，获得如下堆栈信息[^4]：

```objc
0 +[AppDelegate load]
1 call_load_methods
2 load_images
...
3 dyld::notifySingle(dyld_image_states, ImageLoader const*)
4 ImageLoader::recursiveInitialization(...)
5 ImageLoader::processInitializers(...)
6 ImageLoader::runInitializers(...)
7 dyld::_main(...)
8 dyldbootstrap::start(...)
9 _dyld_start
```

## 3. main 方法

这个阶段是指从 main 函数开始到 -[UIApplicationDelegate application:didFinishLaunchingWithOptions:] 中首屏渲染完成之前的事。

* 初始化各种配置，如 info.plist，UserDefaults 等等

* 各种 sdk、日志系统初始化

* 用于首屏数据展示的网络请求

* 首屏渲染计算

## 4. 首屏渲染后

这里用户已经感知到 app 启动了，一般来说，会初始化一些非首屏功能的模块。

## 后记

了解了启动流程，就必须要继续研究如何加快 app 启动速度。一般来说，我们只能在上述第 2，3 两步尽可能做一些优化。

参考下一篇：

[还能更快吗之启动优化](/TODO)

[^1]: https://github.com/aidansteele/osx-abi-macho-file-format-reference
[^2]: https://juejin.cn/post/6844903511612899336
[^3]: https://en.wikipedia.org/wiki/Address_space_layout_randomization
[^4]: https://www.jianshu.com/p/c0a1a3ad9336
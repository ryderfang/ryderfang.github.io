# 发生在用户点击 icon 之后


本文讨论一下 iOS 的 App 从用户点击图标开始到 App 完全可用的过程。苹果开发者文档有这样一篇文章：

[Responding to the Launch of Your App](https://developer.apple.com/documentation/uikit/app_and_environment/responding_to_the_launch_of_your_app?language=objc)

有个主要的流程图：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2021-12-28-GZXEUO.jpg)

另外，还有一篇介绍如何优化启动速度的文章，毕竟只有准确了解了启动中做了哪些事，才能更针对地进行优化。

[Reducing Your App’s Launch Time](https://developer.apple.com/documentation/xcode/reducing-your-app-s-launch-time)

这里还参考了以下几篇文章：

[1]: [iOS App 启动优化](https://www.jianshu.com/p/024b3d847fe0)

[2]: [iOS App 从点击到启动](https://www.jianshu.com/p/231b1cebf477)

[3]: [深入了解 App 启动过程](https://www.jianshu.com/p/e7a9e14205ac)

总结一下：

## 系统层

## pre-main 阶段

## main 方法

## 首屏渲染后



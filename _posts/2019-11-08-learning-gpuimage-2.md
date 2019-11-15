---
layout: post
title: 学习 GPUImage 2 | GPUImage 2 (Swift)
categories: [GPUImage, iOS]
---

# 概述
<br>
书接上文，Brad Larson 在 2016 年用 Swift 语言重写了 GPUImage，创造了新的 [**GPUImage2**](https://github.com/BradLarson/GPUImage2)，同样在作者的网站上有介绍：[http://www.sunsetlakesoftware.com/2016/04/16/introducing-gpuimage-2-redesigned-swift](http://www.sunsetlakesoftware.com/2016/04/16/introducing-gpuimage-2-redesigned-swift)。

作为第二代框架，它的优势主要有：

1. Swift 比 Objective-C 更加简洁，代码量减少了 80%，作者做过统计：

    GPUImage Version | Files | Lines of Code
    - | - | -
    Objective-C (without shaders) | 359 | 20107
    Swift (without shaders) | 157 | 4549
    Shaders | 233 | 6670

    作者举了一个自定义操作符的例子，通过自定义 `operator -->` 表示 addTarget 简化了代码。

    作者在 [另一篇文章](http://www.sunsetlakesoftware.com/2014/12/02/why-were-rewriting-our-robotics-software-swift) 中解释了为什么要用 Swift 重写软件，其中针对开发中遇到的一些常见错误，由 OC 语言本身设计不够严谨导致的有：
    - nil 消息转发会导致错误被隐藏，延迟被发现。这里有两个例子：
      * 用 IB 来开发界面的时候，如果忘记连线，会导致属性为 nil，按钮点击无响应，很难排查问题；
      * 作者公司是做机器人的，有一个例子导致了上万美元的损失。存储机器人移动坐标的类在特定情况下变成了 nil，这样坐标系统的 Z 轴变成了 0，
        机械臂会把打印指针插入打印台里移动，导致产品损坏。
    - 对 NSError 和其他 OC 错误不合适的处理
      * 作者的意思是通常 error 是通过二级指针传入传出的，如果不小心置空，容易出问题，参见 [StackOverFlow](https://stackoverflow.com/questions/1808929/handling-nserror-when-reading-from-file) 的例子
    - Object (id) 类型错误转换
    - 枚举类型与整数藕合 (Swift 支持自定义类型枚举)

2. 不再局限于 iOS/Mac，新一代框架可以运行在 Linux 上 (支持 Swift)，甚至可以跑在树莓派上。

3. 新增特性：支持在图片上任意形状添加滤镜；像素级裁剪；高斯和均值滤波自动降采样和升采样。





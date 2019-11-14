---
layout: post
title: 学习 GPUImage 2 | GPUImage 2 (Swift)
categories: [GPUImage, iOS]
---

# 概述
<br>
书接上文，Brad Larson 在 2016 年用 Swift 语言重写了 GPUImage，创造了新的 [**GPUImage2**](https://github.com/BradLarson/GPUImage2)，同样在作者的网站上有介绍：[http://www.sunsetlakesoftware.com/2016/04/16/introducing-gpuimage-2-redesigned-swift](http://www.sunsetlakesoftware.com/2016/04/16/introducing-gpuimage-2-redesigned-swift)。

作为第二代框架，它的优势主要有：

* Swift 比 Objective-C 更加简洁，代码量减少了 80%，作者做过统计：

GPUImage Version | Files | Lines of Code
- | - | -
Objective-C (without shaders) | 359 | 20107
Swift (without shaders) | 157 | 4549
Shaders | 233 | 6670

作者举了一个自定义操作符的例子，通过自定义 `operator -->` 表示 addTarget 简化了代码。

* 不再局限于 iOS/Mac，新一代框架可以运行在 Linux 上 (支持 Swift)，甚至可以跑在树莓派上。
* 新增特性：支持在图片上任意形状添加滤镜；像素级裁剪；高斯和均值滤波自动降采样和升采样。





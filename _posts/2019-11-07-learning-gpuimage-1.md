---
layout: post
title: 学习 GPUImage | GPUImage Framework
categories: [GPUImage, iOS]
---

# 概述
<br>
![](https://img.alicdn.com/tfs/TB1ws.EmO_1gK0jSZFqXXcpaXXa-240-240.png)

[**GPUImage**](https://github.com/BradLarson/GPUImage) 是 iOS 上一个开源图像处理库，基于 OpenGL GS 2.0，作者是 Brad Larson。

作者于 2012 年发布了这个框架，官方网站介绍：[http://www.sunsetlakesoftware.com/2012/02/12/introducing-gpuimage-framework](http://www.sunsetlakesoftware.com/2012/02/12/introducing-gpuimage-framework)

相对于系统的 CoreImage (iOS 5.0)，GPUImage 可以更方便地自定义滤镜，并且在处理速度上更快。相对于 CPU 计算来说，GPU 在处理图形图像时更具优势，
在 iPhone 4 的机器上，GPU 的图片处理性能比 CPU 强百倍以上。

GPUImage 是基于 BSD 协议的开源框架，我们可以直接在 [GitHub](https://github.com/BradLarson/GPUImage) 上获取源码。

* 系统要求
  * iPhone 4+ (iPhone 3G/iPod 1/iPod 2 不支持)
  * iOS 4.0+ (依赖 iOS 5.0 SDK)
  * 支持 ARC/MRC (-fobjc-arc)

可以看出，GPUImage 是一个非常古老的库，GitHub 最新的提交也只到 2016.05，作者应该不再更新。

作者后续又推出了基于 Swift 和 OpenGL 的 [**GPUImage2**](https://github.com/BradLarson/GPUImage2) 和
基于 Metal 的 [**GPUImage3**](https://github.com/BradLarson/GPUImage3)。

但是初代 GPUImage 仍然可以用在最新的 iOS 13.2 上，而且它是后续两个框架的基础。所以我们仍然有必要去研究和学习它。

# 整体架构







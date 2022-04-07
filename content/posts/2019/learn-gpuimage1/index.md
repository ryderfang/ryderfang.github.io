---
title: GPUImage1 学习
date: 2019-11-07T16:18:03+08:00
categories: [iOS, GPUImage]
tags: [GPUImage]
draft: true
---

## 概述

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

## GPU 渲染

![](https://img.alicdn.com/tfs/TB1iPL0nbH1gK0jSZFwXXc7aXXa-1308-387.png)

GPU 的高度并行结构使得在大块数据并行算法上比 CPU 更加高效，所以在 iOS 上使用 GPU 渲染图形图像会比 CPU 更快。

经过比较，GPUImage 在处理同一张图片的滤镜操作会比 CPU 操作快百倍以上，比系统的 Core Image 快 40 倍；作者的测试是在 iPhone 4 上进行的，我在 iPhone 6s 上重新运行了一下 Benchmark 测试发现，现在差距已经没有这么大了，一方面 CPU 在升级，另一方面 Core Image 通常也会使用 GPU 进行计算，但 GPUImage 仍然优秀！比 CPU 快 10位，视频处理比 Core Image 快一倍！

<div style="text-align:center;margin:20px;">
<img src="https://img.alicdn.com/tfs/TB1yjvYneH2gK0jSZFEXXcqMpXa-376-669.png" width="200" height="356"
  style="margin-right: 40px" />
<img src="https://img.alicdn.com/tfs/TB12mzVnhz1gK0jSZSgXXavwpXa-376-669.png" width="200" height="356" />
</div>

了解 GPU 渲染还得从 OpenGL 说起，作为一个跨语言、跨平台的 API 规范，OpenGL 将操作 GPU 硬件的图形指定翻译成易用的 API 接口。在嵌入式平台，如 iOS/安卓 上，OpenGL 的子集叫 OpenGL ES （OpenGL for Embedded Systems ），本文说的 GPUImage 就是基于此进一步封装和优化的。

引用下苹果 [官方文档](https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/Introduction/Introduction.html) 的图：

![](https://img.alicdn.com/tfs/TB1bi20nhD1gK0jSZFKXXcJrVXa-1344-249.png)

可以看出，我们是通过 OpenGL ES 与硬件打交道的，那为什么平时开发过程中，很难感觉到呢？这是由于苹果通过 UIKit 和 Core Animation 将实现细节隐藏了，这也可以解释为什么 UIView/NSView 绘制实现都交给了 CALayer，其实就是通过 CoreAnimation (虽然名字叫 Animation，但动画仅是其中的一小部分) 调用 OpenGL ES/Core Graphics 来完成视图渲染的。

![](https://img.alicdn.com/tfs/TB1XeL1nbj1gK0jSZFuXXcrHpXa-500-201.png)

那 GPU 渲染包含哪些步骤呢？下面的 OpenGL 渲染流水线展示了主要的流程：

![](https://img.alicdn.com/tfs/TB1D160nkT2gK0jSZPcXXcKkpXa-642-324.png)

* 不管是顶点信息 (几何信息)，还是像素信息 (图片信息)，传入 GPU 后都被处理成 OpenGL 指令存储在 Display List 中。
* 顶点信息会被存储成矩阵，经过原始处理，如各种变换、反射和坐标转换后，进行组装。
* 像素信息也会经过缩放、裁剪等操作后，存储在纹理中。
* 光珊化 (Rasterization) 会将以上处理后得到的原始数据变成一系列片元 (Fragment)，每一个片元代表了最终帧缓冲区中的一个像素所有的信息，包括位置、颜色等。
* 片元操作，也叫片元着色 (Fragment Shader)，根据光珊化的结果逐一操作片元，获得最终渲染的像素数据。
* 最后帧缓冲区会把渲染好的数据返回给设备显示。


## 整体架构







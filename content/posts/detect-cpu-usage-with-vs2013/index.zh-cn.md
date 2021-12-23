---
title: "VS2013 检测 CPU 占用率"
date: 2016-08-08T19:59:09+08:00
categories: [Windows]
tags: [CPU]
resources:
- name: "featured-image"
  src: "featured-image.jpg"
---

最近开发的一个程序，用户反馈 CPU 占用非常高，基本把一个内核占用满了。

<!--more-->

![CPU 占用](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-8-16/10993914.jpg)

我自己在虚拟机中试了下，确实这样！

在用户机器中获取了 DUMP，只看到有几个线程一直在跑，调用堆栈中也看不到太多信息（主要是没有线程 CPU 占用信息），一时没有方法。

今天突然想到 VS2013，新版本增加了一些功能，貌似有性能分析相关的。

找了一下，果然在`调试`菜单下发现了`性能与诊断`：

![调试菜单](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-8-16/13597794.jpg)

选择 `CPU使用率`，就开始分析啦！

很快就给出了分析结果：

![分析结果](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-8-16/34785051.jpg)

哈哈！瞬间定位 CPU 占用元凶，原来是一个后台线程一直在跑（空转），设计不合理。这个线程最早设计成自驱动的，找到原因就好办了，改成被驱动式就行了！
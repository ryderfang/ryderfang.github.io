---
title: "Jekyll 本地安装"
date: 2016-06-05T19:34:55+08:00
categories: [Manual, Blog]
tags: [jekyll]
lastmod: 2021-11-12T11:26:13+08:00
---

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-07-jekyll.jpg)

安装 Ruby 和 Ruby DevKit

  - [Ruby 2.2.4](http://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.2.4.exe)
  - [Ruby DevKit](http://dl.bintray.com/oneclick/rubyinstaller/DevKit-mingw64-32-4.7.2-20130224-1151-sfx.exe)

<!--more-->

切换到安装目录：

```bash
$ cd C:\RubyDevKit
$ ruby dk.rb init
$ ruby dk.rb install
```

安装Jekyll

```bash
$ gem install jekyll
$ gem install wdm
```

切换到博客目录运行

```bash
$ jekyll build [--watch/-w]
$ jekyll serve [--watch/-w]
```

用浏览器打开`http://127.0.0.1:4000`，即可看到效果，而且在修改文件的同时刷新页面即可实时更新。

可以通过--port 888指定端口号，更多命令行参数参考[官方手册][^1]

安装有问题，可以参考更多文档：

- [Running Jekyll on Windows][^2]

- [Jekyll Windows][^3]

- [Setup Jekyll on Windows][^4]

[^1]: http://jekyll.bootcss.com/docs/configuration/ "配置"
[^2]: http://www.madhur.co.in/blog/2011/09/01/runningjekyllwindows.html
[^3]: http://jekyll-windows.juthilo.com/
[^4]: http://yizeng.me/2013/05/10/setup-jekyll-on-windows/

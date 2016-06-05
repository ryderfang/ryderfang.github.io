---
layout: post
title: 本地安装Jekyll调试环境（Windows）
description: Jekyll本地安装、调试
category: coding
---
# 安装Ruby和Ruby DevKit
[Ruby 2.2.4](http://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.2.4.exe)

[Ruby DevKit](http://dl.bintray.com/oneclick/rubyinstaller/DevKit-mingw64-32-4.7.2-20130224-1151-sfx.exe)

`cd C:\RubyDevKit
ruby dk.rb init
ruby dk.rb install`

# 安装Jekyll
`gem install jekyll`
`gem install wdm`

# 运行
`jekyll build [--watch/-w]`
`jekyll serve [--watch/-w]`


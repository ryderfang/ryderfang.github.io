---
layout: post
title: 介绍几个常用的vim插件
description: vim插件安装、使用
category: coding
---

## [vim-multiple-cursors](https://github.com/terryma/vim-multiple-cursors#quick-start)

### 1. 编辑同一变量

    def hello(poorly_named_var)
      poorly_named_var ||= "Nameless"
      puts("Hi, " + poorly_named_var)
    end

![1](https://github.com/terryma/vim-multiple-cursors/raw/master/assets/example1.gif?raw=true)

* 命令：`2Gfp<C-n><C-n><C-n>cname`
* 解释：到第二行，fp找到p，三次<C-n>选中三个单词，c进入编辑

### 2. 多行操作 I

    _ 
    Mon
    Tue
    Wed
    Thu
    Fri
    Sat
    Sun

![2](https://github.com/terryma/vim-multiple-cursors/raw/master/assets/example2.gif?raw=true)

* 命令：`2Gvip<C-n>i"<Right><Right><Right>",<Esc>vipJ$r]Idays = [`
* 解释：
  * 2Gvip到第二行，全选
  * <C-n>i在所有行开头插入光标，输入"
  * 移动到行尾，输入",
  * vip全选后，输入J，让所有行上移

### 3. 多行操作 II

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

![3](https://github.com/terryma/vim-multiple-cursors/raw/master/assets/example3.gif?raw=true)

* 命令：`2Gdf[$r,0f,v<C-n>…<C-n>c<CR><Up><Del><Right><Right><Right><Del>`
* 解释：
  * 2Gdf[，删除[前的内容
  * $r，到结尾，将[替换成,
  * 0f,，到开头，查找到`,`
  * 切换到v模式，选中所有的`,`，c插入，回车
  * 上移一行，删除，移动到最右，删除

### 4. HTML加密（？）

![4](https://github.com/terryma/vim-multiple-cursors/raw/master/assets/example4.gif?raw=true)

* 命令：
* 解释：

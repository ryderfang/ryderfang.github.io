---
title: "Vue 调试工具 Devtools"
date: 2018-01-24T20:09:09+08:00
categories: [RTFM]
tags: [Vue, Front-End]
lastmod: 2021-11-12T11:26:13+08:00
upd: "前端真难"
---

最近开始学习 [Vue.js](https://cn.vuejs.org/), 一脸懵逼地进入前端世界。

不使用 `vue-cli` 和 `webpack` 这些构建工具，使用单个 html 引入 Vue。

<!--more-->

html 内容是这样的:

``` html
<html>

<head>
    <meta charset="UTF-8">
    <title>Hello, Vue</title>
    <script src="https://cdn.jsdelivr.net/npm/vue"></script>
</head>

<body>
    <div id='app'>
        <span v-bind:title="message">鼠标悬停</span>
    </div>
    <script>
        var app = new Vue({
            el: '#app',
            data: {
                message: '页面加载于 ' + new Date().toLocaleString()
            }
        })
    </script>
</body>

</html>
```


用浏览器打开这个 html 就可以看到效果（鼠标悬停显示『页面加载于yyyy-MM-dd hh:mm:ss』）

安装 [Vue-Devtools](https://chrome.google.com/webstore/detail/nhdogjmejiglipccpnnnanhbledajbpd)，但是插件栏显示

`Vue.js not detected`

![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-8-16/41087835.jpg)

> 由于访问的路径是 file:// 文件路径，Chrome 扩展默认是不能访问的。

## Vue.js not detected

打开右上角 `...` -> `更多工具` -> `扩展程序`，找到 `Vue.js devtools`，选中 `允许访问文件网址`:

![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-8-16/14411118.jpg)

OK，然后 devtools 仍然不可用，提示

`Vue.js is detected on this page. Devtools inspection is not available because it's in production mode or explicitly disabled by the author.`

> 由于我们使用的 vue.js <https://cdn.jsdelivr.net/npm/vue> 是生产版本，所以不能访问。

## Production mode

下载开发版本的vue.js，放到本地，修改src路径为本地即可。

* 开发版本: https://vuejs.org/js/vue.js

* 生产版本: https://vuejs.org/js/vue.min.js (或者 https://cdn.jsdelivr.net/npm/vue)


## Vue-Devtools

这样，打开开发者工具 (`option + command + i` || `F12`)

可以看到多了一个Vue的Tab:

![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-8-16/10548580.jpg)
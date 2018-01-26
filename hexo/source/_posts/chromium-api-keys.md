---
title: Chromium 缺少 Google API 密钥解决办法
date: 2018-01-26 11:13:16
tags: [chrome, chromium]
categories: Tutorial
---

### 前言

Chromium 是 Chrome 的开发版本，也就是开发过程中存在一堆 Bug 的版本，那么为什么要用这个呢 😏

> 当然是因为好（zhuang）用（bi）了。

废话少说，下载地址：
https://download-chromium.appspot.com/

如果下载不了，可以试下：
* Windows
https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Win_x64/

* Mac
https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Mac/

打不开之类的需要翻墙的问题自行解决吧。

<!-- more -->

### 问题

打开 Chromium 会提示 `缺少 Google API 密钥，因此 Chromium 的部分功能将无法使用` 😒

由于 Chromium 使用的 API 都需要自行申请密钥才能使用。

所以 在 https://console.cloud.google.com/ 上创建密钥。

相关文档：http://www.chromium.org/developers/how-tos/api-keys

最后密钥有三个，位置在 https://console.cloud.google.com/apis/credentials

- GOOGLE_API_KEY
- GOOGLE_DEFAULT_CLIENT_ID
- GOOGLE_DEFAULT_CLIENT_SECRET

### 解决

官方的解决方法是：

将下面三行写到 ~/.bash_profile 中，然后重启浏览器即可

``` bash
export GOOGLE_API_KEY="****"
export GOOGLE_DEFAULT_CLIENT_ID="****
export GOOGLE_DEFAULT_CLIENT_SECRET="****"


$ source ~/.bash_profile
```

这样，有时是管用的。特别是在 Windows上，使用类似的在命令行输入：

``` bash
setx GOOGLE_API_KEY your_key_goes_here
setx GOOGLE_DEFAULT_CLIENT_ID your_client_id_goes_here
setx GOOGLE_DEFAULT_CLIENT_SECRET your_client_secret_goes_here
```

但是 Mac 上有时不管用，参考:

https://gist.github.com/cvan/44a6d60457b20133191bd7b104f9dcc4

在文档最后，发现有个哥们写了一个 Python 脚本，试了下，很好用！

我 Fork 了一下，修复了一个 bug，给他提了 PR (https://github.com/ezeeyahoo/ChromiumSyncEnabler/pull/1)

https://github.com/FongRay/ChromiumSyncEnabler

跑下来重启 Chromium 就 OK 了！


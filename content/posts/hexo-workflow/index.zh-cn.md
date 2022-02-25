---
weight: 0
title: "使用 Hexo 遇到的一些问题"
date: 2017-09-27T20:04:57+08:00
categories: [RTFM]
tags: [Hexo, Blog]
resources:
- name: "featured-image"
  src: "featured-image.jpg"
---

关于 Hexo 如何使用，网上已经有很多教程了，不再赘述。涉及的几个相关命令也就是:

```bash
$ npm install -g hexo
$ hexo init
$ hexo generate (hexo g)
$ hexo server (hexo s)

$ hexo new [name] - 新建文章
$ hexo new page [name] - 新建页面
```

<!--more-->

正常情况下，这样就会启动本地的服务:[http://localhost:4000](http://localhost:4000)，但现实总是残酷的，

由于国内XXX的网络环境，总会遇到各种各样的问题，

下面总结一下本博客迁移到Hexo过程中遇到的一些问题。

## NPM 源

node的包管理工具npm，默认使用国外的源，访问比较慢，建议换成国内源，一般是[淘宝npm](https://npm.taobao.org):
```bash
$ npm install -g cnpm --registry=https://registry.npm.taobao.org
```
这样就可以使用cnpm代替npm进行模块安装了:
```bash
$ cnpm install [name]
```
或者，使用nrm (npm的源管理工具):
```bash
$ npm install nrm
$ nrm ls
* npm ---- https://registry.npmjs.org/
  cnpm --- http://r.cnpmjs.org/
  taobao - https://registry.npm.taobao.org/
  nj ----- https://registry.nodejitsu.com/
  rednpm - http://registry.mirror.cqupt.edu.cn/
  npmMirror  https://skimdb.npmjs.com/registry/
  edunpm - http://registry.enpmjs.org/
$ nrm use taobao
$ nrm test taobao
```

## Hexo 安装

### **hexo-server**
hexo server执行失败:
```bash
ERROR Plugin load filed: hexo-server
```
需要单独安装hexo-server:
```bash
$ npm install hexo-server --save
```

### **node-sass**
```bash
$ npm install node-sass --save
```
如果出现如下情况:
```bash
$ node scripts/install.js

Cannot download "https://github.com/sass/node-sass/releases/download/v4.5.3/darwin-x64-51_binding.node": 

read ECONNRESET

Hint: If github.com is not accessible in your location
      try setting a proxy via HTTP_PROXY, e.g. 

      export HTTP_PROXY=http://example.com:1234

or configure npm proxy via

      npm config set proxy http://example.com:8080

$ node-sass@4.5.3 postinstall /private/tmp/node_modules/node-sass
$ node scripts/build.js
```
说明github访问比较慢，两种方法：
* 修改host:
> http://tool.chinaz.com/dns?type=1&host=github.com&ip=
找一个TTL比较小的host，如:
```bash
192.30.255.112 github.com
```
* 直接去github下载
> https://github.com/sass/node-sass/releases/download/v4.5.3/darwin-x64-51_binding.node
然后将该文件放到目录:`~/.npm/node-sass/4.5.3/darwin-x64-51_binding.node`
再执行安装命令
```bash
$ npm intall node-sass --save
```

### **hexo-renderer-scss**
有些主题需要安装hexo-renderer-scss:
```bash
$ npm install hexo-renderer-scss --save
```
会出现错误:
```bash
ERROR Plugin load failed: hexo-renderer-scss
Error: ENOENT: no such file or directory, scandir 'xxx/node_modules/node-sass/vendor'
   at Object.fs.readdirSync (fs.js:914:18)
   ...
```
提示这个目录找不到，那我们手动创建好了:
```bash
$ mkdir xxx/node_modules/node-sass/vendor
$ mkdir xxx/node_modules/hexo-renderer-scss/node_modules/node-sass/vendor
```
接下来还是报错:
```bash
ERROR Plugin load failed: hexo-renderer-scss
Error: Missing binding xxx/node_modules/hexo-renderer-scss/node_modules/node-sass/vendor/darwin-x64-51/binding.node
Node Sass could not find a binding for your current environment: OS X 64-bit with Node.js 7.x

Found bindings for the following environments:
```
到这个目录下，把刚刚下载的darwin-x64-51_binding.node重命名复制进去好了:
```bash
$ mkdir xxx/node_modules/hexo-renderer-scss/node_modules/node-sass/vendor/darwin-x64-51/
$ cp darwin-x64-51_binding.node xxx/node_modules/hexo-renderer-scss/node_modules/node-sass/vendor/darwin-x64-51/binding.node
```

### **页面空白**
有时执行hexo s后显示服务启动，但页面打开空白，显示`Cannot GET /`，这种情况有很多原因，

可以尝试:
```bash
$ npm install
$ hexo cl
$ hexo g
$ hexo s
```
如果还有问题，查看一下npm插件是否安装正常:
```bash
$ npm ls --depth 0
hexo-site@0.0.0 xxx
├── hexo@3.3.9
├── hexo-deployer-git@0.3.1
├── hexo-generator-archive@0.1.4
├── hexo-generator-baidu-sitemap@0.1.2
├── hexo-generator-category@0.1.3
├── hexo-generator-feed@1.2.2
├── hexo-generator-index@0.2.1
├── hexo-generator-sitemap@1.2.0
├── hexo-generator-tag@0.2.0
├── hexo-renderer-ejs@0.3.1
├── hexo-renderer-marked@0.3.0
├── hexo-renderer-scss@1.0.3
├── hexo-renderer-stylus@0.3.3
├── hexo-server@0.2.2
└── node-sass@4.5.3

npm ERR! invalid: hexo-generator-baidu-sitemap@0.0.8 xxx/node_modules/hexo-generator-baidu-sitemap/node_modules/hexo-generator-baidu-sitemap
```
可以看到hexo-generator-baidu-sitemap这个插件安装失败了，尝试重新安装或者删除它:
```bash
$ npm install hexo-generator-baidu-sitemap --save
$ npm uninstall hexo-generator-baidu-sitemap
```
或者在`package.json`中将它删除掉。
---
title: "2021 个人目标 🎯"
date: 2021-11-16T16:32:25+08:00
lastmod: 2022-01-13T11:44:00+08:00
categories: [Flag]
tags: [flag]
---

时隔两年，再次拾起博客。

<!--more-->

我完全不是一个有恒心的人，而且做什么事都是三分钟热度。包括博客，从 Jekyll 到 Hexo，再到现在 Hugo。

有新鲜玩意都想把玩一下，折腾完了又觉得索然无味。注重形式大于内容，纠结字体字号、各种样式的事情，反而没什么内容沉淀下来。

## 关于博客

在腾讯云买了域名 [ryderfang.com](https://ryderfang.com)，然后折腾备案、SSL 证书部署、nginx 配置静态页面等等，
目前源文件拖管在 [Github](https://github.com/ryderfang/ryderfang.github.io/) 上，每次 push 自动触发 [Actions](https://github.com/ryderfang/ryderfang.github.io/actions)，
完成编译并推送到 *gh-pages* 分支的操作。站内搜索使用 [algolia](https://www.algolia.com/)，使用手动 Actions 的方式，需要时触发更新。

同样在腾讯云买了一个轻应用服务器，托管一下这个静态博客，不打算再折腾自动化了，需要同步的时候 ssh 登录一下，手动拉一下 repo 就好。

> 哈哈，总是在打脸，还是把自动同步服务器做成了一个 Action

```shell
- name: remote ssh command
  uses: appleboy/ssh-action@master
  with:
    host: ${{ secrets.TENCENT_CLOUD_HOST }}
    username: ubuntu
    key: ${{ secrets.TENCENT_CLOUD_KEY }}
    port: 22
    script: |
      whoami
      cd blog && git pull
      echo 'Done!'
```


再把之前的博客内容整理到新的博客上，发现并没多少值得保留的，真是有点惭愧。

## 技术目标

常常想起小时候爸爸告诫我的话：

> 有志之人立常志，无志之人常立志。

但是，这么多年的工作经历，让我认识到自己只是个普通人。普通的技术、普通的能力和普通的志向，甚至于在 “内卷” 与 “躺平” 的浪潮中，已经逐渐想要躺平。

最近又看到一句话：

> 到底什么样的终点，才配得上这一路的颠沛流离 ?!

是啊，或许，我们只是想去码头整点薯条，人生本无太多意义。

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2021-11-16-life.jpeg)

扯远了，总之，普通人就定几个能完成的普通目标。也不要过分自责，因为你就是一粒宇宙的尘埃。

### 写文章

到年底还有一个多月，输出 2-3 篇技术博客。

> UPDATE: 算完成 80% 吧，内容还需要补充

### iOS 技术栈

继续完善 iOS 八股技术栈: https://github.com/ryderfang/iOSBagu，尽可能去了解一些犄角旮旯的知识点。

> UPDATE: 没有完成，需要尽快补齐 
### 读书

读一点其他领域的书，随便看一点。

> UPDATE: 没有完成，多读书是 2022 重点目标

## 生活目标

### 健康

身体 NO.1，换季的时候，一家人都得了咽炎，去医院太折腾了。希望全家都健康，宝宝也快点长大，少让姥姥和大家操点心吧。

> UPDATE: 安安越来越大了，前段时间脸上又被虫咬了一大块，最近快长好了。

> 平安、健康、快乐，足矣。没有别的希冀。
### 早起

每天送老婆上班，虽然累，但还是挺好的，早到公司一小时，可以做很多事了。困的问题就中午多午睡一会儿吧。

能睡说明自己还年轻吧，至少没有失眠的困扰，感觉至少要睡十个小时才能满足，也只能周末才有这个机会了。

> UPDATE: 本来年底想面试一下来年换个工作，但老婆可能也要换，准备还是继续苟一段时间。

> 总的来说，鹅厂的人文关怀还是可以的。但不同项目组也差异很大，PCG 确实是个天坑。

## 结语

就这些吧，我感觉能完成 80% 就已经很不错了。元旦的时候再来 check 一下 🚀


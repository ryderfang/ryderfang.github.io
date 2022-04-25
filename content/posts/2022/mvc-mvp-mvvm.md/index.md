---
title: "面试八股之 MVC/MVP/MVVM"
date: 2022-04-25T15:47:49+08:00
categories: [Eight-Legged]
tags: [MVC, MVP, MVVP]
---

> 我是万万没想到，现在客户端面试卷到要问 ⌜图灵机⌟ 了。

—— 某公司一面后有感

大清废除八股已经 120 年了，但我们选拔制度并没有明显的改变。不管是面试还是晋升，无不充斥着八股套路。

“破题“结束，闲话少说。

三大架构中公共的 View 和 Model 很好理解：

* View，也就是 UI，是用户看到的界面，是 Model 的外在表现

* Model，Data Logic，是数据的集合

## MVC

* Controller 是什么？类似一个中枢的概念，控制着数据如何被展示出来。

### 类型 1

MVC 架构有很多设计。最早的版本是这样的：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-25-bW95gq.png)

用户通过操作 View 来完成系统更新，整个控制流是单向的。

当然还有一种，用户只通过 Controller 来操作，这在 [Wikipedia](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) 中可以看到。

### 类型 2

如果 View 和 Controller 都接收用户指令的话，就会变化成这样：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-25-1Wr4Oa.png)

- Controller 可以直接接收用户指令，如通过 scheme/url 进入某个页面，而不是通过直接操作 View。这时，Controller 响应的方法，
可能是 Update/Manipulate(操纵) Model，也可能是更新 View。

- 用户直接操作 View，这里 View 如果想要变更 Model，只能通过 Controller 中转。

- 有时，Model 的变更会直接通知 View （通过观察者的方式）。

这个实现，也就是阮一峰在博客[^1]中提到的 `Backbone.js` 的架构方式。

### 类型 3

在 iOS 开发中，MVC 被苹果演变成了如下方式：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-25-wMatUH.png)


解除了 Model -> View 之间的耦合。

## MVP

在上述类型 3 的 MVC 模型中，将 Controller 替换成 Presenter，就是 MVP 模型。

* 也就是说，Presenter 作为 View/Model 的中枢，承载了所有显示相关的逻辑[^2]。

<img src='https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-25-GrO3ag.png' width='60%'>
</img>

在 MVP 架构下原先的 UIViewController 其实变成了 View 的一部分。

## MVVM[^3]

* 区别与 MVP 的显著特征就是 View <-> Model 之间使用了数据绑定 (Data-binding) 技术。使两者在松耦合的同时，也能及时感知对方的变化。

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-25-56i89q.png)

Data Binding 在前端框架中比较常见，比如 Vue 中：[https://v1.vuejs.org/guide/syntax.html](https://v1.vuejs.org/guide/syntax.html)

```html
<span>Message: {{ msg }}</span>
```

在 iOS 中，要实现双向绑定，可以使用 RAC 框架 [ReactiveCocoa](https://github.com/ReactiveCocoa/ReactiveCocoa)

SwftUI 中的 `@Binding` 也可以实现类似的功能。（或许不是？这里待学习）

[^1]: https://www.ruanyifeng.com/blog/2015/02/mvcmvp_mvvm.html
[^2]: https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter
[^3]: https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel
[^4]: https://juejin.cn/post/6901200799242649607

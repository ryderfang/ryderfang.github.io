---
layout: post
title: 怎么面试一个 iOS 开发 | iOS Interview
categories: [iOS, Interview]
---

# 前言 

这是一篇 iOS 面试问题总结，也是对自己 iOS 开发的总结。老实说作为一个半路出家的 iOS 程序员 ( 2016.12 ~ now ) ，心里还是很虚的。自己到底是什么样水平，以后的技术之路要怎么走，这些心里还没有把握，希望整理完之后，有个答案。

<!--  more -->

# Roadmap 路线图

> 首先，我们需要有一个大图，iOS 开发到底包含了哪些东西？

![](https://cdn.nlark.com/yuque/0/2019/png/370705/1568733024889-c3cf0005-322e-4ff4-9748-488d2596401d.png)

# 1. 语言基础篇

## 1.1 关键词类

* property
  * weak
  * atomic 线程安全吗
  * copy 与 assign

* id 与 instancetype

* __weak 与 __block

* __weak 与 _Unsafe_Unretain

* block
  * 原理
  * 循环引用
  * copy 属性 (MRC 传统)

* category
  * 方法列表加载时机
  * 如何添加属性；关联对象的存储
  * category 与 class extension

# 2.UIKit

* 性能优化
  * 离屏渲染
  * 卡顿优化
  * 图片渲染
  * 异步绘制

* 事件传递机制
  + hitTest 与 pointInside:withEvent:

    ```objc
    - (UIView *)hitTest:(CGPoint)point withEvent:(UIEvent *)event {
        // 1. 判断自己能否接收触摸事件
        if (self.userInteractionEnabled == NO || self.hidden == YES || self.alpha <= 0.01) return nil;
        // 2. 判断触摸点在不在自己范围内
        if (![self pointInside:point withEvent:event]) return nil;
        // 3. 从后往前遍历自己的子控件，看是否有子控件更适合响应此事件
        int count = self.subviews.count;
        for (int i = count - 1; i >= 0; i--) {
            UIView *childView = self.subviews[i];
            CGPoint childPoint = [self convertPoint:point toView:childView];
            UIView *fitView = [childView hitTest:childPoint withEvent:event];
            if (fitView) {
                return fitView;
            }
        }
        // 没有找到比自己更合适的 view
        return self;
    }
    ```

    事件传递是自根向叶的 (根是 UIApplicatin),

    UIApplication -> UIWindow -> View -> subviews

  + 响应链 与 UIResponder

    响应链是由叶向根的，所有 pointInside 返回 YES 的 view 构成

    view -> superView -> viewController -> UIWindow -> UIApplication

# 3. 底层原理

## 3.1 RunLoop

## 3.2 Runtime

> 源码 https://opensource.apple.com/source/objc4/

## 3.3 AutoreleasePool

* AutoReleasePool 与 @autoreleasePool

* Tagged Pointer

## 3.4 消息转发

* 四个步骤

# 4. 开发实践

## 4.1 多线程

## 4.2 架构

> https://www.jianshu.com/p/f8806c2f3ee3

* MVC

* MVP

* MVVM

# 5. 其他知识

## 5.1 App 启动流程

## 5.2 JsPatch

## 5.3 算法

* LRU
  * 常见实现就是 `HashMap + 双向链表`，HashMap 的 value 是 链表的节点地址。
  * **get**: 查找 HashMap，找到就把链接表对应节点移到头部，返回值；否则返回空。
  * **set**: 查找 HashMap，如果存在，更新值并移动节点到链表头部；不存在，新增值放到链表头部，空间不够则淘汰尾部节点。
![](https://pic2.zhimg.com/80/v2-09f037608b1b2de70b52d1312ef3b307_hd.jpg)
    

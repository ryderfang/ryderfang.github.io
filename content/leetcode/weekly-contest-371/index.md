---
title: "题解 Weekly Contest 371"
date: 2023-11-12T19:24:15+08:00
categories: [Contest]
tags: []
---

{{< katex >}}

记录下第一次 AK！！

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2023-11-12-weekly-371.jpg)

https://leetcode.com/contest/weekly-contest-371

## 2932. Maximum Strong Pair XOR I

https://leetcode.com/problems/maximum-strong-pair-xor-i/

## 2935. Maximum Strong Pair XOR II

https://leetcode.com/problems/maximum-strong-pair-xor-ii/

一个 Easy，一个 Hard，是同一个问题，仅数据规模的区别。

\\( 1 <= nums.length <= 5 * 10^4 \\)

好像也没多大。。一个二分搜索莽过去了，感觉不太科学。

## 2933. High-Access Employees

很简单啊，时间换算成分钟，排序之后第三个检查下间隔 \\( diff <= 59 \\) 即可。

## 2934. Minimum Operations to Maximize Last Elements in Arrays

最后一个做的，开始觉得好难。然后发现可以枚举一下。。

两种情况：
1. 不交换 *nums1* 和 *nums2* 最后一位，将当前队列中大于最后的数都换出去。
2. 交换 *nums1* 和 *nums2* 最后一位，同样交换掉不符合的，记得这种情况 *count* 要加 1。

两种情况取最少的，注意找不到返回 -1 即可。

---

昨天 [Biweekly 117](https://leetcode.com/contest/biweekly-contest-117/)，Hard 题也做出来了，之前都不敢上手或者没空看。现在发现还是没想象中难的。加油开始准备分类刷题了！！💪🖖🤟🤟🤟

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2023-11-12-DhSjfS.png)



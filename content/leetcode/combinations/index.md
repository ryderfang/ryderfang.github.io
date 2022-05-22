---
title: "组合算法"
date: 2022-05-22T00:26:54+08:00
categories: [Combinations]
tags: []
---

{{< katex >}}

组合，就是在排列的基础上，去除顺序的因素。对于同一组数，只计数 1。

$$
  C_n^m = \frac {P_n^m}{P_m} = \frac {n!}{m!(n-m)!} = \frac {n(n-1)(n-2)...(n-m+1)}{m!}
$$

组合总数：\\( \displaystyle\sum_{k=0}^nC_n^k = C_n^0 + C_n^1 + ... + C_n^n = 2^n \\)

性质：

$$
\begin{aligned}
C_n^m&=C_n^{n-m}\newline
C_{n+1}^m&=C_n^m + C_n^{m-1}
\nonumber
\end{aligned}
$$

## 原理

## 例题

* [77. Combinations](https://leetcode.com/problems/combinations/)


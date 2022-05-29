---
title: "重拾数据结构中的算法"
date: 2022-04-22T16:48:09+08:00
categories: [Data Structure]
tags: [algo]
---

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-22-data-structure.jpg)

很多年前，我在本科时，学习数据结构用的教科书上面这本 <u>《数据结构教程》（蔡子经、施伯乐 编著）</u>。
在家翻了下，发现已经找不到了。不知道什么时候遗失了，因为我一般不会丢弃书籍，尤其是专业书。

写这篇的目的是帮自己回忆一下，有些数据结构和算法的内容都已经被忘记了。
比如 Trie 树、B 树等结构，Floyd 算法本质是个 DP，还有 KMP 算法，常看常忘。

数据结构这门课的教科书五花八门，尤其以严蔚敏的那版最为出名。目前看网上好评最高的是清华大学的**邓俊辉**教授的
《数据结构（C++ 语言版）》。本文参考：

https://cloud.tsinghua.edu.cn/d/76cbab99574046698804/files/?p=%2Fdsacpp-3rd-edn.pdf

虽然有电子版，等疫情结束还是会买本实体书支持下老师。

> `2022/05/27` 买到了！JD 下单后 4 天收到，说明上海的疫情快结束了。加油吧！

{{< alert info >}}

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-05-27-data-structure.jpg)
{{< /alert >}}

这本书有自己的官网：[https://dsa.cs.tsinghua.edu.cn/~deng/ds/dsacpp/index.htm](https://dsa.cs.tsinghua.edu.cn/~deng/ds/dsacpp/index.htm)

## I. 数据结构

队列、链表、栈这些基础的结构按下不提，主要看看有哪些平时用得很少容易忽略的类型。

### 优先队列

### 二叉树的遍历

### Huffman 编码

### 邻接矩阵

### 邻接表

## II. 算法

### 散列 hash

### 字符串

#### BMP

#### BM

#### Karp-Rabin 算法

### 二叉树/平衡树

二叉搜索树，又叫二叉查找树 (Binary Search Tree)，简称 BST。

平衡二叉树，也就是平衡树 (self-Balancing Binary Bearch Tree)，简称 BBST。

平衡树有非常多的 [种类](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree#Implementations)

常见的有：

#### AVL 树

#### 伸展树

#### B 树

#### 红黑树

#### k-d 树

### 图论

#### BFS

#### DFS

#### 最短路


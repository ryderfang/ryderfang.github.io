---
title: "一个神奇的减包方法"
date: 2022-04-08T17:03:29+08:00
categories: [iOS, PkgSize]
tags: []
---

最近大搞减包运动，今天从同事那了解到一个神奇的减包策略：

{{< alert >}}
把 `@protocol` 换成 `NSProtocolFromString` !
{{< /alert >}}

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-08-why.webp)

这是为啥呢？

## 做个实验

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-08-4ODA2i.png)

添加一个 `@protocol` 调用：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-08-JmELvX.png)

可以看到生成的 lib 中 `__DATA,__objc_const` 段中少了多个 `protocol` 相关的符号。

改成 `NSProtocolFromString`，也不会生成符号：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-08-RiuEXg.png)

## 为啥呢

我们反编译一下 [文件](https://github.com/ryderfang/iOSBagu/blob/main/StaticLib/BGStaticLib/BGStaticLib/BGStaticLib.m)：

```objc
clang -rewrite-objc BGStaticLib.m
```

在反编译后的 [BGStaticLib.cpp](https://github.com/ryderfang/iOSBagu/blob/main/StaticLib/BGStaticLib/BGStaticLib/BGStaticLib.cpp) 中可以看出：

新增的几个符号，被指定放到了 `__DATA` 段，正是用 `MachOView` 看到新增的那几个符号：

```cpp
_OBJC_PROTOCOL_INSTANCE_METHODS_NSObject __attribute__ ((used, section ("__DATA,__objc_const")))

_OBJC_PROTOCOL_OPT_INSTANCE_METHODS_NSObject __attribute__ ((used, section ("__DATA,__objc_const")))

_OBJC_PROTOCOL_PROPERTIES_NSObject __attribute__ ((used, section ("__DATA,__objc_const"))) 

_OBJC_PROTOCOL_REFS_BGProtocol __attribute__ ((used, section ("__DATA,__objc_const")))
```


## 能减多少

比较了下修改前后的 lib 文件，`size xx.a`

```
// 修改前
__TEXT	__DATA	__OBJC	others	dec	hex
703	1256	0	6519	8478	211e	xx/libBGStaticLib.a(BGStaticLib.o)
```

```
// 修改后
__TEXT	__DATA	__OBJC	others	dec	hex
204	320	0	6531	7055	1b8f	xx/libBGStaticLib.a(BGStaticLib.o)
```

`__TEXT` 和 `__DATA` 段共减少了 `499 + 936 = 1435`，共 1.4 KB。

通过 `stat xx.a` 命令获取整个 lib 字节数发现：

共减少了 `15504 - 11168 = 4336`，共 4.3 KB。

## 积小成多

看起来单个文件并不多，但实际上在巨型 app 中，使用 `protocol` 作为 bridge 跨工程调用其他模块的方法非常多。

这次减包过程中，某模块经过这样改写之后，减少了 **10M** 的包体积。🤩
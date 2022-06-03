---
title: "日常小问题的技术偏方"
date: 2022-06-02T13:01:37+08:00
categories: [Tips]
tags: []
---

经常遇到一些编码、调试或者电脑方面的小问题，苦寻解答无果后自己找出了症结。

这些方案只是当时场景下的一种可能解决思路，现在或者你的环境下并不一定适用。

> So，仅供参考

## 调试问题

1. 替换沙盒中的文件

默认情况下 App 沙盒是不可见，可以在 `Info.plist` 添加

UIFileSharingEnabled = YES (Application supports iTunes file sharing)

即可在 `Finder` 中找到 App 的沙盒文件。

2. crash 符号化

* 使用 symbolicatecrash

```bash
// 找到本地 symbolicatecrash 所在位置
find /Applications/Xcode.app -name symbolicatecrash -type f

export DEVELOPER_DIR=/Applications/XCode.app/Contents/Developer

// 把 symbolicatecrash copy 到 crash 文件同一目录下再执行
./symbolicatecrash ./*.crash ./*.app.dSYM > symbol.log

```

* 使用 atos

找到 dSYM 符号文件

```bash
atos -o ./xx.framework.dSYM/Contents/Resources/DWARF/xx -arch arm64 -l 0x10888e8000 0x00000001xxxx 0x00000001yyyy
```

其中 `0x10888e8000` 是 xx 二进制的基址，也就是程序的入口地址。一般在 crash 日志最后。
`0x00000001xxxx`, `0x00000001yyyy` 是堆栈中函数的地址。

3. `LLDB` 调试技巧

* 输出格式化字符串

```bash
po [[NSString alloc] initWithFormat:@"$RYDER$ %@", self.xxStr]

po [[NSString alloc] initWithData:[NSJSONSerialization dataWithJSONObject:xxDic options:0 error:0] encoding:NSUTF8StringEncoding]
```

## 编码问题

1. 一些常用的 Xcode 编译错误关键词

在编译机吐出大量 Xcodebuild 编译日志时方便快速定位错误。

```
❌

error generated.

ERROR: 

ERROR: Build failed.

clang: error:

linker command failed with exit code
```

2. pod lint 命令，添加私有源

```bash
pod spec lint *.podspec --allow-warnings --no-clean  --verbose --use-libraries --sources='xxx/pod_specs.git,yyy/pod_specs.git'
```

3. UIButton 点击状态

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-06-03-uibutton_state.jpg)

## 开发环境问题

1. 清理资源

MBP 作为开发机，如果一直使用 Xcode 开发，会产生大量中间文件。512G 的存储很容易爆掉，下面是一些可清理的资源位置：

* CocoaPods 缓存

```bash
/Users/$USER/Library/Caches/CocoaPods/Pods/Release/
```

```bash
/Users/$USER/Library/Caches/CocoaPods/Pods/External/
```

* Xcode 编译缓存

```bash
/Users/$USER/Library/Developer/Xcode/DerivedData
```

* 微信缓存

```bash
/Users/$USER/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/$UID/Message/
```

* 企业微信缓存

```bash
/Users/$USER/Library/Containers/com.tencent.WeWorkMac/Data/Library/Application Support/WXWork/Data/$UID/Cache
/Users/$USER/Library/Containers/com.tencent.WeWorkMac/Data/Library/Application Support/WXWork/Data/$UID/Emotion
/Users/$USER/Library/Containers/com.tencent.WeWorkMac/Data/Documents/Profiles/$UID/Caches
```

* 邮箱缓存

```bash
/Users/$USER/Library/Group Containers/UBF8T346G9.Office/Outlook/Outlook 15 Profiles/Main Profile/Data
```

## 其他问题

1. M1 的 MacBook Pro 突然 `Esc` 键无效了？

打开活动监视器，找到 `Siri` 进程，强制关闭它！（再也不用每次重启解决了）

2. `git` 操作

* 删除本地在远程已经被删除的分支

```bash
git branch --merged >/tmp/merged-branches && \
  vi /tmp/merged-branches && xargs git branch -d </tmp/merged-branches
```

* git 暂存区、工作区文件恢复

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-06-03--git%20reset%20HEAD.png)

3. 模拟器点击异常

现象：模拟器点击位置漂移
解决：是多点触控导致，按住 alt，把两个触控点合并就可以了


> To be continued...
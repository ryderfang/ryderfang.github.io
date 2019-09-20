---
layout: post
title: 从搬瓦工到 Vlutr，继续科学上网 | GFW
categories: [VPS, Config]
---

之前用的 bangwagon 突然连不上了，找到现在可用的官网 (https://bwh88.net/clientarea.php?action=products) 看了下，服务虽然到期了，但整个 Service 被停用了。

![](https://img.alicdn.com/tfs/TB1tiAwfpY7gK0jSZKzXXaikpXa-1970-312.png)

发了个 Ticket 问了下，倒是很快回复了。结论就是我之前买的那种 10G 的产品是 OpenVZ v6 架构，已经不再维护，下架了。
看了下，现在最便宜的就是 20G 这款，一年 50 美金，差不多也是行情价。

![](https://img.alicdn.com/tfs/TB1xY3zfxz1gK0jSZSgXXavwpXa-628-708.jpg)

考虑到 bandwagon 配置并不是特别方便，经同事推荐改用 Vlutr，现在优惠还不错 (重点)：

1、<u>充 $10 送 $25</u>。 [点击注册](https://www.vultr.com/?ref=8250675)

2、<u>充 $25 送 $50</u>。 [点击注册](https://www.vultr.com/?ref=8250676-4F)

最关键的是，支持 **支付宝** 付款！

# 注册

注册非常简单，点击上面的链接，用邮箱注册即可。都不用激活，方便的一比。

# 充值

登录之后，在 https://my.vultr.com/billing/ 页面，选择 Alipay (支付宝)，充 $25，搞定！

> $25 足够用 5 个月了！

![](https://img.alicdn.com/tfs/TB1VusFfAT2gK0jSZFkXXcIQFXa-979-622.jpg)

# 买机器

进入 https://my.vultr.com/deploy/

* 地区 选欧洲或者美国的，相对快一点。
* 操作系统 选 Ubuntu, 版本 18.04 x64。(因为这是 LTS 版本，相对稳定点)
* 机器类型选最便宜的 $5/月 的。

其他不用管，直接 Deploy 吧。

# 配置

等机器准备好，在 Products 页面中找到你的机器 IP 地址、密码等信息。打开本地终端，
`ssh root@ip -p 22`
输入密码，登录远程机器。

通过脚本一键安装 SS 服务端即可。

```
wget --no-check-certificate -O shadowsocks.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh
chmod +x shadowsocks.sh
./shadowsocks.sh 2>&1 | tee shadowsocks.log
```

设置端口号、密码等，等脚本执行完。
这里有个坑，脚本里 shadowsocks.json 里配置的服务器地址是 0.0.0.0，有 Vlutr 环境里好像不通，我之前用 bandwagon 不用改，但是 Vlutr 不行。

```
vim /etc/shadowsocks.json
// 把里面的 "server" 字段修改为服务器的 IP 址。
```

在本地，用 SS 服务端，设置好同样的 IP 地址、端口号和密码即可。

至此，就可以去浪了！🌊🌊🌊


---
title: Shadowsocks 翻墙和搬瓦工 VPS 配置
date: 2018-06-21 11:26:11
tags: [VPS, VPN, Shadowsocks, Bandwagon, 搬瓦工, 翻墙]
categories: Configuration
---

### 这是干啥的

敏感你懂的，不多谈。🌝 🌝 🌝

### 怎么用

* 下载 `ShadowsocksX-NG`，

https://github.com/shadowsocks/ShadowsocksX-NG/releases/

* 配置自己的 VPS，比如我自己使用的 Bandwagon VPS，或者使用其他 SS server 地址

* 在 `ShadowsocksX-NG` 中添加服务器，配置好可以 FQ 了。

### 搬瓦工

目前可用的主页地址是

https://bwh1.net/clientarea.php?action=products

我买的最便宜的一个 `10G VZ - PROMO`，一个月 $2.99，但年付才 $19.99 (130 软妹币) 而已。

每月流量 `550GB` 根本用不完

有需要的朋友，如果不想自己配置，可以给我转 ￥10 (一个月)，我把我的 VPS 共享给你。

<!-- more -->

### 配置项

在 `ShadowsocksX-NG` 的服务器配置中，导入如下配置即可

```
{
  "random" : false,
  "authPass" : null,
  "useOnlinePac" : false,
  "TTL" : 0,
  "global" : false,
  "reconnectTimes" : 3,
  "index" : 0,
  "proxyType" : 0,
  "proxyHost" : null,
  "authUser" : null,
  "proxyAuthPass" : null,
  "isDefault" : false,
  "pacUrl" : null,
  "configs" : [
    {
      "enable" : true,
      "password" : "****",
      "method" : "aes-256-cfb",
      "remarks" : "Bandwangon",
      "server" : "*.*.*.*",
      "kcptun" : {
        "nocomp" : false,
        "key" : "****",
        "crypt" : "salsa20",
        "datashard" : 70,
        "mtu" : 1350,
        "mode" : "fast2",
        "parityshard" : 30,
        "arguments" : ""
      },
      "enabled_kcptun" : true,
      "server_port" : 8989,
      "remarks_base64" : "QmFuZHdhbmdvbg=="
    }
  ],
  "proxyPort" : 0,
  "randomAlgorithm" : 0,
  "proxyEnable" : false,
  "enabled" : true,
  "autoban" : false,
  "proxyAuthUser" : null,
  "shareOverLan" : false,
  "localPort" : 1080
}
```

请帮忙 star🌟 

> https://github.com/FongRay/FongRay.github.io

---
### 附录

> 一些命令

```
$ /usr/bin/python /usr/local/bin/ssserver -c /etc/shadowsocks.json -d start
```

```
# /etc/shadowsocks.json
{
    "server":"0.0.0.0",
    "server_port":8989,
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"****",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open":false
}
```

> start kcp

```
{
    "server":"0.0.0.0",
    "server_port":8989,
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"fangr",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open":false
}
```

> kcp config

```
{
    "listen": ":29900",
    "target": "127.0.0.1:8989",
    "key": "****",
    "crypt": "salsa20",
    "mode": "fast2",
    "mtu": 1350,
    "sndwnd": 1024,
    "rcvwnd": 1024,
    "datashard": 70,
    "parityshard": 30,
    "dscp": 46,
    "nocomp": false,
    "acknodelay": false,
    "nodelay": 0,
    "interval": 40,
    "resend": 0,
    "nc": 0,
    "sockbuf": 4194304,
    "keepalive": 10
}
```

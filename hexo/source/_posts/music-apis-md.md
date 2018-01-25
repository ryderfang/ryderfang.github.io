---
title: 各种音乐平台 API 整理
date: 2018-01-22 15:24:20
tags: [API]
categories: Coding
---

> 本文总结一些常见音乐平台 API 接口，仅用于学习使用，不保证大流量请求的可用性。

* [豆瓣FM](#豆瓣FM)

* [网易云音乐](#网易云音乐)

* [虾米音乐](#虾米音乐)

---

<!-- more -->

### 豆瓣FM

> 写了一个脚本，将豆瓣红心歌曲导入到网易云音乐:
> [douban2netease.py](https://github.com/FongRay/PyTools/blob/master/douban2netease.py)

#### 登录

* 接口: https://www.douban.com/service/auth2/token  (POST)
* 请求头:
`{'Content-Type': 'application/x-www-form-urlencoded'}`
* 参数:
账号、密码是明文的
``` json
post_data = {
        'apikey': '02646d3fb69a52ff072d47bf23cef8fd',
        'client_id': '02646d3fb69a52ff072d47bf23cef8fd',
        'client_secret': 'cde5d61429abcd7c',
        'udid': '07e0335d0c38a73384f709fa3102b33a94710d60',
        'douban_udid': 'b635779c65b816b13b330b68921c0f8edc049590',
        'device_id': '07e0335d0c38a73384f709fa3102b33a94710d60',
        'grant_type': 'password',
        'redirect_uri': 'http://www.douban.com/mobile/fm',
        'username': user,
        'password': passwd
    }
```
* 返回值:
access_token 后续接口会用到。
``` json
{
  "access_token": "****",
  "douban_user_name": "****",
  "douban_user_id": "****",
  "expires_in": 0,
  "refresh_token": "****"
}
```

#### 获取红心歌曲

* 接口: https://api.douban.com/v2/fm/redheart/basic (GET)
* 请求头:
`{'Authorization': 'Bearer ' + ACCESS_KEY}`
* 参数：
``` json
query_data = {
        'alt': 'json',
        'apikey': '02646d3fb69a52ff072d47bf23cef8fd',
        'app_name': 'radio_iphone',
        'audio_patch_version': 4,
        'client': 's:mobile|y:iOS 11.2.2|f:122|d:07e0335d0c38a73384f709fa3102b33a94710d60|e:iPhone8,1|m:appstore',
        'douban_udid': '677209cb05feeb5aa10fd34ed2d25765d8284f33',
        'kbps': 128,
        'udid': '07e0335d0c38a73384f709fa3102b33a94710d60'
    }
```
* 返回值:
``` json
{
	"description": "",
	"collected_count": 0,
	"creator": {
		"url": "https:\/\/www.douban.com\/people\/FongRay\/",
		"picture": "http://img7.doubanio.com\/icon\/u66096063-4.jpg",
		"id": "66096063",
		"name": "小咩"
	},
	"offshelf_alert": "部分红心歌曲版权洽谈中，暂时不能收听，等待它们浮出海面的同时，去收获更多新的红心吧",
	"title": "我的红心歌曲",
	"cover": "",
	"updated_time": "2017-05-05 17:16:03",
	"is_collected": true,
	"rec_reason": "",
	"created_time": "",
	"can_play": true,
	"type": -1,
	"id": -1,
	"songs": [{
		"update_time": 1493982773,
		"playable": true,
		"like": 1,
		"sid": "1888519"
	}, {
		"update_time": 1498647084,
		"playable": true,
		"like": 1,
		"sid": "2236918"
	}]
}
```

#### 获取歌曲详情

* 接口: https://api.douban.com/v2/fm/songs (POST)
* 请求头:
`{'Authorization': 'Bearer ' + ACCESS_KEY}`
* 参数:
其中 sids 参数是多个sid用分隔符`|`拼接而来的
``` json
    post_data = {
        'alt': 'json',
        'apikey': '02646d3fb69a52ff072d47bf23cef8fd',
        'app_name': 'radio_iphone',
        'audio_patch_version': 4,
        'client': 's:mobile|y:iOS 11.2.2|f:122|d:07e0335d0c38a73384f709fa3102b33a94710d60|e:iPhone8,1|m:appstore',
        'douban_udid': '677209cb05feeb5aa10fd34ed2d25765d8284f33',
        'sids': sids,
        'udid': '07e0335d0c38a73384f709fa3102b33a94710d60',
        'user_accept_play_third_party': 1,
        'version': 122
    }
```
* 返回值:
歌曲列表，每首歌的详细信息
``` json
[
  {
    "all_play_sources": [
      {
        "confidence": 0.937778,
        "source_full_name": "itunes",
        "file_url": null,
        "source": "it",
        "source_id": "514603298",
        "playable": true,
        "page_url": null
      }
    ],
    "albumtitle": "回蔚 莫文蔚演唱會@台北小巨蛋",
    "file_ext": "mp4",
    "album": "/subject/10546781/",
    "ssid": "6b4b",
    "title": "爱情",
    "subtype": "",
    "sid": "1888519",
    "sha256": "07d68b92880a24a25d6e3688880acbff3d52f0ed52984b28ccf8e1bee216a7f0",
    "status": 0,
    "picture": "http://img7.doubanio.com/lpic/s8953971.jpg",
    "update_time": 1493982773,
    "alert_msg": "",
    "is_douban_playable": false,
    "public_time": "2012",
    "partner_sources": [],
    "singers": [
      {
        "style": [],
        "name": "莫文蔚",
        "region": [
          "香港"
        ],
        "name_usual": "莫文蔚",
        "related_site_id": 0,
        "avatar": "http://img3.doubanio.com/img/fmadmin/large/31309.jpg",
        "genre": [
          "Pop"
        ],
        "is_site_artist": false,
        "id": "8260"
      }
    ],
    "artist": "莫文蔚",
    "is_royal": false,
    "url": "http://mr3.doubanio.com/e49a7486849f6067219c959dc03077e4/0/fm/song/p1888519_128k.mp4",
    "length": 165,
    "release": {
      "link": "https://douban.fm/album/10546781g7be3",
      "id": "10546781",
      "ssid": "7be3"
    },
    "aid": "10546781",
    "kbps": "128",
    "available_formats": {
      "64": 1290,
      "128": 2523,
      "192": 3806
    }
  }
]
```

### 网易云音乐


### 虾米音乐


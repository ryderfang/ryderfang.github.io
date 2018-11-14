---
title: Visual Paradigm 去除水印的方法 (Python)
date: 2018-01-25 11:24:45
tags: [Python, Tools]
categories: [Python]
---

### 前言

Visual Paradigm 是一个不错的画流程图、时序图和类图的工具，有30天试用版和社区版，其中社区版 Community Version 是永久免费的，唯一不足的是在导出图表为图片时，右下角会有一个水印：

![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-8-16/46295044.jpg)

本文就是要 Python 去除这个水印，输出 png 图片。

> 该方法参考了网络上手动去除的方法，需要有一些操作

<!-- more -->

### 导出

首先需要将完成的图表导出为 svg 格式的图片：

![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-8-16/20666066.jpg)

选择 svg 格式保存：

![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-8-16/26387925.jpg)

这样我们就得到了一个带水印的 [svg 图片](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-8-16/vp_test.svg):

![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-8-16/vp_test.svg)

### 去除水印

* 处理 svg 图片

> Svg（Scalable Vector Graphics，可缩放矢量图形） 是一种矢量图片格式，可以使用文本编辑器直接打开，可以看得到在最后几行有水印的内容，所以我们可以用代码自动把他们去掉（当然也可以手动删除）。

水印内容在 Svg 文件中：

```xml
<text x="68" xml:space="preserve" y="276" stroke="none"
      >Powered ByVisual Paradigm Community Edition</text
      ><image font-size="12" x="303" y="264" fill="white" width="16" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABvklEQVR42o1TPUgC
YRi+z1PSzWrSc6ho6W/xNIhEoZoCl/a2fqaGoJKwyHIp16ZyCyIolwpq6c8lIz0h
h6ACa/KWOHGz4byezz7lkNM8eHjf7/ve53l/vu84rsWXEcVo2uOJtYrhW5A3YCKE
48YXnE7zoSzfty3AyFHdln/R4bBA5O5fgQbyiUbIK6oY5gjxG1XCtyAngFl7qXT+
Y7UOwR+glTSK8EZkomlJMZsNCrKs7iuKOuXzJboUJYAqemrtHEBkGwsTIy/pe0bZ
/Rmvd6K27svnx7Q/cu08LIliiPpmlvEGJo0DL4sRSKVyBuEZledznKpeYs+u6/YF
nKt6C+jpe14QPjCsQUpmQVYgaNK0R9hPYJLtZ5Eo5JGkVF0AmUZAvoBLM5WBXhZs
A6YB+pi+AAudD+zOnMuVjBcKheoMbOXyG0wcWKGtAPr77gauKyYTFU8g+xrsUWex
mKu2r79Gye3eQkAE7i4wCtQG+YTMKZwt0zOUv274DjCLJGZBoEqv9JRtyyDfgrwK
f09PNnyJ6OuBiYSxPAbecf9UMNZIbvovUBE8FjRINrEMNJbd1t9I28Gz7YD7DHKo
WdwvFl2vGaThOSEAAAAASUVORK5CYII=" height="16" stroke="white" preserveAspectRatio="none"
    />
```

用 Python 读取文件内容，去除这一段内容即可。

* 转换成 png 图片

然后将 Svg 格式转换成 png格式，这里有现成的库 [cairosvg](http://cairosvg.org/) 来实现。

完整的代码可以在 我的 [Github]() 上找到。

### 使用方法

* 需要先安装 `cairosvg`:

``` bash
$ pip3 install cairosvg
```

可能会报错，`Pillow` 安装失败，提示：
`The headers or library files could not be found for zlib.`

可以尝试一下:
``` bash
$ xcode-select —-install
$ brew install libtiff libjpeg webp little-cms2
$ pip3 install Pillow
```

安装 `cairosvg` 成功后，使用 Python3 `import cairosvg` 发现还是报错:
```
>>> import cairosvg
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/cairosvg/__init__.py", line 29, in <module>
    from . import surface
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/cairosvg/surface.py", line 24, in <module>
    import cairocffi as cairo
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/cairocffi/__init__.py", line 41, in <module>
    cairo = dlopen(ffi, 'cairo', 'cairo-2')
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/cairocffi/__init__.py", line 38, in dlopen
    raise OSError("dlopen() failed to load a library: %s" % ' / '.join(names))
OSError: dlopen() failed to load a library: cairo / cairo-2
```

经过搜索，发现还需要安装 `cairo` 和 `libffi`：
``` bash
$ brew install cairo pango gdk-pixbuf libffi
```

* 终于弄完了

![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-8-16/49384223.jpg)

源文件：
[vp_remove_watermark.py](https://github.com/FongRay/PyTools/blob/master/vp_remove_watermark.py)


* 核心代码如下：
``` python
import cairosvg

svg_content = ''
with open(src_name, 'r') as f:
    svg_content = f.read()
    end = svg_content.rfind('</g')
    beg = svg_content.rfind('<g', 0, end)
    svg_content = svg_content[:beg] + svg_content[end:]

with open('./vp_test_out.svg', 'w') as f:
    f.write(svg_content)

cairosvg.svg2png(url='./vp_test_out.svg', write_to=dst_name)
```

* 赶紧跑起来

```bash
$ python vp_remove_watermark test.svg -o out.png
```


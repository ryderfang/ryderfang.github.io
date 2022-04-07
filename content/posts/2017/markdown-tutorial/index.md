---
title: Markdown 完全手册
date: 2017-10-12
categories: [Manual]
tags: [markdown]
---

# 速查手册
`*斜体*` ~> *斜体*

`**粗体**` ~> **粗体**

`***粗斜体***` ~> ***粗斜体***

`~~删除线~~` ~> ~~删除线~~

`***` ~> 分割线

`# 一级标题`

`###### 六级标题`

`[超链接](http://fangr.cc/)` ~> [超链接](http://fangr.cc/)

`[超链接][1] [1]:http://fangr.cc` ~>

[超链接][1]

[1]: http://fangr.cc

`<http://fangr.cc/>` ~> <http://fangr.cc/>

`*/+/- 无序列表` ~>
- 无序列表
- 无序列表

`1. 有序列表` ~>
1. 有序列表
1. 有序列表

`>>> 引用` ~>
>> 多层引用

> 多层引用

`![图片alt](图片url "图片title")`

锚点: `[速查手册](#速查手册)` -> [速查手册](#速查手册)

<!-- more -->

---
***
# 整理版

***原作者: [HaoqiangChen](https://github.com/HaoqiangChen), [LeaNote](http://blog.leanote.com/post/freewalk/Markdown-语法手册)***

## 目录

```
有些编辑器使用`[TOC]`可以直接生成目录, 但原生并不支持。
```

>[0. 目录](#目录)
>[1. 分级标题](#分级标题)
>[2. 斜体和粗体](#斜体和粗体)
>[3. 超链接](#超链接)
>>[3.1 行内式](#行内式)
>>[3.2 参考式](#参考式)
>>[3.3 自动链接](#自动链接)

>[4. 锚点](#锚点)
>[5. 列表](#列表)
>>[5.1 无序列表](#无序列表)
>>[5.2 有序列表](#有序列表)
>>[5.3 定义型列表](#定义型列表)
>>[5.4 列表缩进](#列表缩进)
>>[5.5 包含段落的列表](#包含段落的列表)
>>[5.6 包含引用的列表](#包含引用的列表)
>>[5.7 包含代码区块的引用](#包含代码区块的引用)
>>[5.8 一个特殊情况](#一个特殊情况)

>[6. 引用](#引用)
>>[6.1 引用的多层嵌套](#引用的多层嵌套) 
>>[6.2 引用其它要素](#引用其它要素)

>[7. 插入图像](#插入图像)
>>[7.1 行内式](#行内式)
>>[7.2 参考式](#参考式)

>[8. 分隔线和预格式化](#分隔线和预格式化) 
>>[8.1 分隔线](#分隔线)
>>[8.2 预格式化](#预格式化)

>[9. 表格](#表格)
>[10. 注脚](#注脚)
>[11. LaTeX公式](#LaTeX公式)
>>[11.1 $表示行内公式](#表示行内公式)
>>[11.2 $$表示整行公式](#表示整行公式)

>[12. 流程图](#流程图)
>[13. 代码](#代码)
>>[13.1 行内式](#行内式)
>>[13.2 缩进式多行代码](#缩进式多行代码)
>>[13.3 包裹多行代码](#包裹多行代码)
>>[13.4 HTML原始码](#HTML原始码)

---

## 分级标题

第一种写法:

```
这是一个一级标题
============================

这是一个二级标题
--------------------------------------------------

```
第二种写法:
```
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题

一级标题字号最大, 依级递减。

```

**显示效果:**
<!- ignore ->
***

## 斜体和粗体

**代码:**

```
Markdown 使用星号（*）和底线（_）作为标记强调字词的符号, 被 * 或 _ 包围的字词会被转成用 <em> 标签包围, 
用两个 * 或 _ 包起来的话, 则会被转成 <strong>, 例如:

*斜体*或_斜体_
**粗体**
***加粗斜体***
~~删除线~~
但是目前MarkdownPad2和GitHub的Markdown并不支持~~删除线~~这个语法功能, 可以用html的<del></del>或<s></s>代替。
```

**显示效果:**

- *这是一段斜体*
- **这是一段粗体**
- ***这是一段加粗斜体***
- <del>这是一段删除线</del> 

***

## 超链接

Markdown 支持两种形式的链接语法: 行内式和参考式两种形式, 行内式一般使用较多。

### 行内式

**语法说明:**

- []里写链接文字, ()里写链接地址, ()里面" "中的内容可以为链接指定title属性, title属性可加可不加。title属性的效果是鼠标悬停在链接上会出现指定的 title文字。\[链接文字\]\(链接地址 "链接标题"\)这样的形式。***链接地址与链接标题前有一个空格。***

**代码:**

```
欢迎来到[Markdown语法篇](https://github.com/HaoqiangChen/Hq-note/tree/master/Markdown)

欢迎来到[Markdown语法篇](https://github.com/HaoqiangChen/Hq-note/tree/master/Markdown "Markdown语法篇")

```

**显示效果:**

欢迎来到[Markdown语法篇](https://github.com/HaoqiangChen/Hq-note/tree/master/Markdown)

欢迎来到[Markdown语法篇](https://github.com/HaoqiangChen/Hq-note/tree/master/Markdown "Markdown语法篇")



### 参考式

参考式超链接一般用在学术论文上面, 或者另一种情况, 如果某一个链接在文章中多处使用, 那么使用引用 的方式创建链接将非常好, 它可以让你对链接进行统一的管理。

**语法说明:**

- 参考式链接分为两部分, 文中的写法 [链接文字][链接标记], 在文本的任意位置添加[链接标记]:链接地址 &#34;链接标题&#34;, ***链接地址与链接标题前有一个空格。***

如果链接文字本身可以做为链接标记, 你也可以写成[链接文字][]
[链接文字]:链接地址的形式, 见代码的最后一行。

**代码:**

```
欢迎阅读本[Markdown语法篇][1], 还有这几篇高手总结的也不错:[入门篇][2]、
[简明版][3]、[完整版][4], 我就喜欢把百家汇成[自己一家][]^_^。

[1]:https://github.com/HaoqiangChen/Hq-note/tree/master/Markdown "Markdown语法篇"
[2]:https://sspai.com/post/25137 "入门篇"
[3]:http://wowubuntu.com/Markdown/index.html "简明版"
[4]:http://blog.leanote.com/post/freewalk/Markdown-语法手册 "完整版"
[自己一家]:https://github.com/HaoqiangChen/Hq-note/tree/master/Markdown

```

**显示效果:**

欢迎阅读本[Markdown语法篇][1], 还有这几篇高手总结的也不错:[入门篇][2]、
[简明版][3]、[完整版][4], 我就喜欢把百家汇成[自己一家][]^_^。

[1]:https://github.com/HaoqiangChen/Hq-note/tree/master/Markdown "Markdown语法篇"
[2]:https://sspai.com/post/25137 "入门篇"
[3]:http://wowubuntu.com/Markdown/index.html "简明版"
[4]:http://blog.leanote.com/post/freewalk/Markdown-语法手册 "完整版"
[自己一家]:https://github.com/HaoqiangChen/Hq-note/tree/master/Markdown


### 自动链接

**语法说明:**
Markdown 支持以比较简短的自动链接形式来处理网址和电子邮件信箱, 只要是用&lt;&gt;包起来,Markdown 就会自动把它转成链接。一般网址的链接文字就和链接地址一样, 例如:

**代码:**

```
<http://example.com/>
<address@example.com>
```

**显示效果:**

<http://example.com/>
<address@example.com>

***

## 锚点

网页中, 锚点其实就是页内超链接, 也就是链接本文档内部的某些元素, 实现当前页面中的跳转。比如我这里写下一个锚点, 点击回到目录, 就能跳转到目录。 在目录中点击这一节, 就能跳过来。还有下一节的注脚。这些根本上都是用锚点来实现的。

注意:
1. Markdown Extra 只支持在标题后插入锚点, 其它地方无效。
2. Leanote 编辑器右侧显示效果区域暂时不支持锚点跳转, 所以点来点去发现没有跳转不必惊慌, 但是你发布成笔记或博文后是支持跳转的。
3. 非常遗憾的是, 目前MarkdownPad2和GitHub的Markdown并不支持`[TOC]`目录和锚点这个功能, 暂时只能用HTML的标签id来使用页内跳转。

**语法描述:**
1. 使用`[TOC]`标记编辑器会把所有标题写到目录大纲中。
2. 在你准备跳转到的指定标题后插入锚点`{\#标记}`, 然后在文档的其它地方写上连接到锚点的链接。
3. 直接HTML语法锚点功能。
4. 而说到这个就有一个值得一提的地方了, 就是如何在GitHub上也能实现页面跳转, 原先我用的是HTML的a标签锚点, 并且自己给每个标题套上个span#id, 但是发现在gitbook可以有效果, 但是在GitHub上不行, 后面发现这个原生Markdown会自动帮你处理, 自动转成 HTML 实体, 然后我就去看是怎么转化的, 发现它转化每个标题的同时都会赋予一个ID, 那么我们完全直接拿这个ID来做锚点, 至于怎么拿到这个ID, 这个应该就不用我说了吧, 会点编程都知道, 直接打开chrome或者Firefox等调试工具就可以看到了。

**代码:**

```
## 0. 目录{#index}
[TOC]
上面这两种方法原生Markdown都不支持, 但是第一种在gitbook居然有效果, 可惜在GitHub还是没有效果

<span id="#index"></span>

跳转到[目录](#目录)
```
**显示效果:**

跳转到[目录](#目录)

***

## 列表

### 无序列表

使用 *, +, - 表示无序列表, 三个都显示为实心圆点。

**代码:**

```
- 无序列表项 一
- 无序列表项 二
- 无序列表项 三
```

**显示效果:**

- 无序列表项 一
- 无序列表项 二
- 无序列表项 三

### 有序列表

有序列表则使用数字接着一个英文句点再加个空格。

**代码:**

```
1. 有序列表项 一
2. 有序列表项 二
3. 有序列表项 三
```
**显示效果:**

1. 有序列表项 一
2. 有序列表项 二
3. 有序列表项 三

### 定义型列表

**语法说明:**

定义型列表由名词和解释组成。一行写上定义, 紧跟一行写上解释。解释的写法:紧跟一个缩进(Tab)

**代码:**

```
Markdown
:轻量级文本标记语言, 可以转换成html, pdf等格式（左侧有一个可见的冒号和四个不可见的空格）

代码块 2
:这是代码块的定义（左侧有一个可见的冒号和四个不可见的空格）

代码块（左侧有八个不可见的空格）
```
**显示效果:**

Markdown
:轻量级文本标记语言, 可以转换成html, pdf等格式(没效果, 可能又是不支持吧)

代码块 2
: 这是代码块的定义(没效果, 可能又是不支持吧)

代码块（左侧有八个不可见的空格）

**注:方法一和二在马克飞象编辑器是有效果的, 但是gitbook没有, 可能又是不支持, 至于有没有什么方法可以实现我也不知道- -！**

### 列表缩进

**语法说明:**

列表项目标记通常是放在最左边, 但是其实也可以缩进, 最多 3 个空格, 项目标记后面则一定要接着至少一个空格或制表符。

要让列表看起来更漂亮, 你可以把内容用固定的缩进整理好（显示效果与代码一致）:但是可能又是不支持缘故, gitbook需要每一行末尾空两空格换行才行。

```
*轻轻的我走了,正如我轻轻的来； 我轻轻的招手,作别西天的云彩。
 那河畔的金柳,是夕阳中的新娘； 波光里的艳影,在我的心头荡漾。
 软泥上的青荇,油油的在水底招摇； 在康河的柔波里,我甘心做一条水草！
*那榆荫下的一潭,不是清泉,是天上虹； 揉碎在浮藻间,沉淀着彩虹似的梦。
 寻梦？撑一支长篙,向青草更青处漫溯； 满载一船星辉,在星辉斑斓里放歌。
 但我不能放歌,悄悄是别离的笙箫； 夏虫也为我沉默,沉默是今晚的康桥！
 悄悄的我走了,正如我悄悄的来； 我挥一挥衣袖,不带走一片云彩。
```

但是如果你懒, 那也行:
**代码:**
```
* 轻轻的我走了,正如我轻轻的来； 我轻轻的招手,作别西天的云彩。
那河畔的金柳,是夕阳中的新娘； 波光里的艳影,在我的心头荡漾。
软泥上的青荇,油油的在水底招摇； 在康河的柔波里,我甘心做一条水草！
* 那榆荫下的一潭,不是清泉,是天上虹； 揉碎在浮藻间,沉淀着彩虹似的梦。
寻梦？撑一支长篙,向青草更青处漫溯； 满载一船星辉,在星辉斑斓里放歌。
但我不能放歌,悄悄是别离的笙箫； 夏虫也为我沉默,沉默是今晚的康桥！
悄悄的我走了,正如我悄悄的来； 我挥一挥衣袖,不带走一片云彩。
```
**显示效果:**

* 轻轻的我走了,正如我轻轻的来； 我轻轻的招手,作别西天的云彩。
那河畔的金柳,是夕阳中的新娘； 波光里的艳影,在我的心头荡漾。
软泥上的青荇,油油的在水底招摇； 在康河的柔波里,我甘心做一条水草！
* 那榆荫下的一潭,不是清泉,是天上虹； 揉碎在浮藻间,沉淀着彩虹似的梦。
寻梦？撑一支长篙,向青草更青处漫溯； 满载一船星辉,在星辉斑斓里放歌。
但我不能放歌,悄悄是别离的笙箫； 夏虫也为我沉默,沉默是今晚的康桥！
悄悄的我走了,正如我悄悄的来； 我挥一挥衣袖,不带走一片云彩。 


### 包含段落的列表

**语法说明:**

列表项目可以包含多个段落, 每个项目下的段落都必须缩进 4 个空格或是 1 个制表符（显示效果与代码一致）:但是可能又是不支持缘故, gitbook需要每一行末尾空两空格换行才行。

```
* 轻轻的我走了,正如我轻轻的来； 我轻轻的招手,作别西天的云彩。
那河畔的金柳,是夕阳中的新娘； 波光里的艳影,在我的心头荡漾。
软泥上的青荇,油油的在水底招摇； 在康河的柔波里,我甘心做一条水草！

那榆荫下的一潭,不是清泉,是天上虹； 揉碎在浮藻间,沉淀着彩虹似的梦。
寻梦？撑一支长篙,向青草更青处漫溯； 满载一船星辉,在星辉斑斓里放歌。
但我不能放歌,悄悄是别离的笙箫； 夏虫也为我沉默,沉默是今晚的康桥！

* 悄悄的我走了,正如我悄悄的来； 我挥一挥衣袖,不带走一片云彩。
```

如果你每行都有缩进, 看起来会看好很多, 当然, 再次地, 如果你很懒惰, Markdown 也允许:

**代码:**

```
* 轻轻的我走了,正如我轻轻的来； 我轻轻的招手,作别西天的云彩。
那河畔的金柳,是夕阳中的新娘； 波光里的艳影,在我的心头荡漾。
软泥上的青荇,油油的在水底招摇； 在康河的柔波里,我甘心做一条水草！

那榆荫下的一潭,不是清泉,是天上虹； 揉碎在浮藻间,沉淀着彩虹似的梦。
寻梦？撑一支长篙,向青草更青处漫溯； 满载一船星辉,在星辉斑斓里放歌。
但我不能放歌,悄悄是别离的笙箫； 夏虫也为我沉默,沉默是今晚的康桥！


* 悄悄的我走了,正如我悄悄的来； 我挥一挥衣袖,不带走一片云彩。
```

**显示效果:**

* 轻轻的我走了,正如我轻轻的来； 我轻轻的招手,作别西天的云彩。
那河畔的金柳,是夕阳中的新娘； 波光里的艳影,在我的心头荡漾。
软泥上的青荇,油油的在水底招摇； 在康河的柔波里,我甘心做一条水草！

那榆荫下的一潭,不是清泉,是天上虹； 揉碎在浮藻间,沉淀着彩虹似的梦。
寻梦？撑一支长篙,向青草更青处漫溯； 满载一船星辉,在星辉斑斓里放歌。
但我不能放歌,悄悄是别离的笙箫； 夏虫也为我沉默,沉默是今晚的康桥！


* 悄悄的我走了,正如我悄悄的来； 我挥一挥衣袖,不带走一片云彩。

### 包含引用的列表

**语法说明:**

如果要在列表项目内放进引用, 那在 &gt; 前面需要缩进:

**代码:**

```
* 阅读的方法:

> 打开书本。
> 打开电灯。
```

**显示效果:**

* 阅读的方法:

> 打开书本。
> 打开电灯。

### 包含代码区块的引用

**语法说明:**
如果要放代码区块的话, 该区块就需要缩进两次, 也就是 8 个空格或是 2 个制表符:


* 一列表项包含一个列表区块:

> <代码写在这>


### 一个特殊情况
在特殊情况下, 项目列表很可能会不小心产生, 像是下面这样的写法:

```
1986. What a great season.
```
会显示成:

1986. What a great season.


换句话说, 也就是在行首出现数字-句点-空白, 要避免这样的状况, 你可以在句点前面加上反斜杠:

```
1986\. What a great season.
```
会显示成:

1986\. What a great season.

***

## 引用

**语法说明:**

引用需要在被引用的文本前加上&gt;符号。

**代码:**

```
> 这是一个有两段文字的引用,
> 无意义的占行文字1.
> 无意义的占行文字2.
>
> 无意义的占行文字3.
> 无意义的占行文字4.
```
**显示效果:**

> 这是一个有两段文字的引用,
> 无意义的占行文字1.
> 无意义的占行文字2.
>
> 无意义的占行文字3.
> 无意义的占行文字4.


Markdown 也允许你偷懒只在整个段落的第一行最前面加上 &gt; :

**代码:**

```
> 这是一个有两段文字的引用,
无意义的占行文字1.
无意义的占行文字2.

> 无意义的占行文字3.
无意义的占行文字4.
```
**显示效果:**
> 这是一个有两段文字的引用,
无意义的占行文字1.
无意义的占行文字2.

> 无意义的占行文字3.
无意义的占行文字4.

### 引用的多层嵌套
区块引用可以嵌套（例如:引用内的引用）, 只要根据层次加上不同数量的 &gt; :

**代码:**

```
>>> 请问 Markdwon 怎么用？ - 小白

>> 自己看教程！ - 愤青

> 教程在哪？ - 小白
```
**显示效果:**

>>> 请问 Markdwon 怎么用？ - 小白

>> 自己看教程！ - 愤青

> 教程在哪？ - 小白

### 引用其它要素

引用的区块内也可以使用其他的 Markdown 语法, 包括标题、列表、代码区块等:

**代码:**

```
> 1. 这是第一行列表项。
> 2. 这是第二行列表项。
>
> 给出一些例子代码:
>
> return shell_exec("echo $input | $Markdown_script");
```

**显示效果:**

> 1. 这是第一行列表项。
> 2. 这是第二行列表项。
>
> 给出一些例子代码:
>
> return shell_exec("echo $input | $Markdown_script");


***


## 插入图像

图片的创建方式与超链接相似, 而且和超链接一样也有两种写法, 行内式和参考式写法。

语法中图片Alt的意思是如果图片因为某些原因不能显示, 就用定义的图片Alt文字来代替图片。 图片Title则和链接中的Title一样, 表示鼠标悬停与图片上时出现的文字。 Alt 和 Title 都不是必须的, 可以省略, 但建议写上。

### 行内式

**语法说明:**!\[图片Alt\]\(图片地址 "图片Title"\)

**代码:**

```
美丽花儿:
![美丽花儿](https://raw.githubusercontent.com/HaoqiangChen/Hq-note/master/asset/Markdown/img/flower.jpg "美丽花儿")
```

**显示效果:**

美丽花儿:
![美丽花儿](https://raw.githubusercontent.com/HaoqiangChen/Hq-note/master/asset/Markdown/img/flower.jpg "美丽花儿")


### 参考式
**语法说明:**

在文档要插入图片的地方写![图片Alt][标记]

在文档的最后写上[标记]:图片地址 "Title"

**代码:**

```
美丽花儿:
![美丽花儿][flower]

[flower]:https://raw.githubusercontent.com/HaoqiangChen/Hq-note/master/asset/Markdown/img/flower.jpg "美丽花儿"
```

**显示效果:**

美丽花儿: 
![美丽花儿][flower]

[flower]:https://raw.githubusercontent.com/HaoqiangChen/Hq-note/master/asset/Markdown/img/flower.jpg "美丽花儿"

***

## 分隔线和预格式化

### 分隔线

你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线, 行内不能有其他东西。你也可以在星号或是减号中间插入空格。下面每种写法都可以建立分隔线:

**代码:**

```
* * *

***

*****

- - -

---------------------------------------
```

**显示效果都一样:**

---

***

### 预格式化

用\`\`\`+中间你所想注释的内容或代码+\`\`\`包裹:预格式化, 可用于Markdown里面的注释, 解释说明什么的
Markdown的预格式化 相当于HTML的&lt;pre&gt;&lt;/pre&gt;预格式化, 
不过Markdown这个除了预格式化之外还会添加了一个背景色与其他内容区分开, 相当好用。

---

## 表格

**语法说明:**

1. 不管是哪种方式, 第一行为表头, 第二行分隔表头和主体部分, 第三行开始每一行为一个表格行。
2. 列于列之间用管道符|隔开。原生方式的表格每一行的两边也要有管道符。
3. 第二行还可以为不同的列指定对齐方向。默认为左对齐, 在-符号右边加上冒号: 就会右对齐。

**代码:**

简单方式写表格:

```
学号|姓名|分数
-|-|-
小明|男|75
小红|女|79
小陆|男|92
```
原生方式写表格:

```
|学号|姓名|分数|
|-|-|-|
|小明|男|75|
|小红|女|79|
|小陆|男|92|
```
为表格第二列指定方向:

```
产品|价格
-|-:
Leanote 高级账号|60元/年
Leanote 超级账号|120元/年
```

**显示效果:**
简单方式写表格:

学号|姓名|分数
-|-|-
小明|男|75
小红|女|79
小陆|男|92

原生方式写表格:

|学号|姓名|分数|
|-|-|-|
|小明|男|75|
|小红|女|79|
|小陆|男|92|

为表格第二列指定方向:

产品|价格
-|-:
Leanote 高级账号|60元/年
Leanote 超级账号|120元/年

---

## 注脚

**语法说明:**

在需要添加注脚的文字后加上脚注名字[^注脚名字],称为加注。 然后在文本的任意位置(一般在最后)添加脚注, 脚注前必须有对应的脚注名字。

注意:经测试注脚与注脚之间必须空一行, 不然会失效。成功后会发现, 即使你没有把注脚写在文末, 经Markdown转换后, 也会自动归类到文章的最后。

**代码:**

```
使用 Markdown[^1]可以效率的书写文档, 直接转换成 HTML[^2], 你可以使用 Leanote[^Le] 编辑器进行书写。

[^1]:Markdown是一种纯文本标记语言

[^2]:HyperText Markup Language 超文本标记语言

[^Le]:开源笔记平台, 支持Markdown和笔记直接发为博文

**注:脚注自动被搬运到最后面, 请到文章末尾查看, 并且脚注后方的链接可以直接跳转回到加注的地方。**
```

**显示效果:**

**注:因为Markdown是没有一个所谓的规范的(Markdown官网都不支持这么做), 因此导致gitbook没有目录[TOC]和注脚功能, 所以某些特性功能需要写作工具自己支持才可以, 像马克飞象和Leanote就可以。**

---

## LaTeX公式

### $表示行内公式

**代码:**

```
质能守恒方程可以用一个很简洁的方程式 $E=mc^2$ 来表达。
```

**显示效果：**

<p>质能守恒方程可以用一个很简洁的方程式 <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-1-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>E</mi><mo>=</mo><mi>m</mi><msup><mi>c</mi><mn>2</mn></msup></math>" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-1" role="math" style="width: 4.383em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.57em; height: 0px; font-size: 123%;"><span style="position: absolute; clip: rect(1.448em, 1003.57em, 2.577em, -999.998em); top: -2.437em; left: 0.002em;"><span class="mrow" id="MathJax-Span-2"><span class="mi" id="MathJax-Span-3" style="font-family: STIXGeneral-Italic;">E<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mo" id="MathJax-Span-4" style="font-family: STIXGeneral-Regular; padding-left: 0.318em;">=</span><span class="mi" id="MathJax-Span-5" style="font-family: STIXGeneral-Italic; padding-left: 0.318em;">m</span><span class="msubsup" id="MathJax-Span-6"><span style="display: inline-block; position: relative; width: 0.86em; height: 0px;"><span style="position: absolute; clip: rect(3.435em, 1000.409em, 4.158em, -999.998em); top: -4.018em; left: 0.002em;"><span class="mi" id="MathJax-Span-7" style="font-family: STIXGeneral-Italic;">c</span><span style="display: inline-block; width: 0px; height: 4.022em;"></span></span><span style="position: absolute; top: -4.379em; left: 0.454em;"><span class="mn" id="MathJax-Span-8" style="font-size: 70.7%; font-family: STIXGeneral-Regular;">2</span><span style="display: inline-block; width: 0px; height: 4.022em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.441em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.053em; border-left-width: 0px; border-left-style: solid; width: 0px; height: 1.169em;"></span></span></nobr></span>来表达。</p>

注: 原生不支持LaTeX公式。可以用codecogs的云服务, 在线LaTeX数学公式编辑工具, api+一大串LaTex, 比如:
<img src="http://latex.codecogs.com/gif.latex?\frac{\partial J}{\partial \theta_k^{(j)}}=
\sum_{i:r(i,j)=1}{\big((\theta^{(j)})^Tx^{(i)}-y^{(i,j)}\big)x_k^{(i)}}+\lambda \theta_k^{(j)}" />

> 当然这么强大的在线公式编辑器肯定提供了在线GUI给大家, 打开网址: 

> <http://www.codecogs.com/latex/eqneditor.php>, 

> 你就可以随心所欲的编辑公式了, 它同样想Mathtype一样提供了不少模板, 直接编辑, 也很方便。编辑完成之后, 页面上就会实时得到编辑的Latex格式公式图片。

> 或者:<http://latex.codecogs.com/>

> 这个网址的使用方法:\!\[\]\(http://latex.codecogs.com/gif.latex?\\frac{1}{1+sin(x)}\)

\->
> 所以, 上面的例子可以修改为

> 质能守恒方程可以用一个很简洁的方程式 \!\[\](http://latex.codecogs.com/gif.latex?E=mc^2) 来表达。

**显示效果:**

质能守恒方程可以用一个很简洁的方程式 ![](http://latex.codecogs.com/gif.latex?E=mc^2) 来表达。 

### $$表示整行公式

**代码:**

```
$$\sum_{i=1}^n a_i=0$$

$$f(x_1,x_x,\ldots,x_n) = x_1^2 + x_2^2 + \cdots + x_n^2 $$

$$\sum^{j-1}_{k=0}{\widehat{\gamma}_{kj} z_k}$$
```

同上, 原生不支持, 使用上面的网站即可。

**显示效果:**

![](http://latex.codecogs.com/gif.latex?\\sum_{i=1}^n&space;a_i=0 "\sum_{i=1}^n a_i=0")

<img src="http://latex.codecogs.com/gif.latex?f(x_1,x_x,\ldots,x_n)&space;=&space;x_1^2&space;&plus;&space;x_2^2&space;&plus;&space;\cdots&space;&plus;&space;x_n^2" title="f(x_1,x_x,\ldots,x_n) = x_1^2 + x_2^2 + \cdots + x_n^2" />

![](http://latex.codecogs.com/gif.latex?\\sum^{j-1}_{k=0}{\widehat{\gamma}_{kj}&space;z_k} "\sum^{j-1}_{k=0}{\widehat{\gamma}_{kj} z_k}")

访问 [MathJax](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference) 参考更多使用方法。

---

## 流程图

**代码:**

```
flow
st=>start: Start:>https://www.zybuluo.com
io=>inputoutput: verification
op=>operation: Your Operation
cond=>condition: Yes or No?
sub=>subroutine: Your Subroutine
e=>end

st->io->op->cond
cond(yes)->e
cond(no)->sub->io
```

**显示效果:**

<div class="flow-chart"><svg height="579.359375" version="1.1" width="453.5625" xmlns="http://www.w3.org/2000/svg" style="overflow: hidden; position: relative;"><desc>Created with Raphaël 2.1.0</desc><defs><path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block"></path><marker id="raphael-marker-endblock33" markerHeight="3" markerWidth="3" orient="auto" refX="1.5" refY="1.5"><use NS1:href="#raphael-marker-block" transform="rotate(180 1.5 1.5) scale(0.6,0.6)" stroke-width="1.6667" fill="black" stroke="none"></use></marker></defs><rect x="0" y="0" width="60.46875" height="41.21875" r="20" rx="20" ry="20" fill="#ffffff" stroke="#000000" style="" stroke-width="2" class="flowchart" id="st" transform="matrix(1,0,0,1,65.4063,29.2109)"><title>https://www.zybuluo.com</title></rect><text x="10" y="20.609375" text-anchor="start" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="text-anchor: start; font-style: normal; font-variant-caps: normal; font-weight: normal; font-size: 14px; line-height: normal; font-family: sans-serif;" id="stt" class="flowchartt" font-size="14px" font-family="sans-serif" font-weight="normal" transform="matrix(1,0,0,1,65.4063,29.2109)"><tspan dy="6.8046875">Start</tspan><title>https://www.zybuluo.com</title></text><path fill="#ffffff" stroke="#000000" d="M10,20.609375L0,41.21875L137.0625,41.21875L157.0625,0L20,0L10,20.609375" stroke-width="2" font-family="sans-serif" font-weight="normal" id="io" class="flowchart" style="font-family: sans-serif; font-weight: normal;" transform="matrix(1,0,0,1,17.1094,149.6406)"></path><text x="30" y="20.609375" text-anchor="start" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="text-anchor: start; font-style: normal; font-variant-caps: normal; font-weight: normal; font-size: 14px; line-height: normal; font-family: sans-serif;" id="iot" class="flowchartt" font-size="14px" font-family="sans-serif" font-weight="normal" transform="matrix(1,0,0,1,17.1094,149.6406)"><tspan dy="6.8046875">verification</tspan></text><rect x="0" y="0" width="153.3125" height="41.21875" r="0" rx="0" ry="0" fill="#ffffff" stroke="#000000" stroke-width="2" class="flowchart" id="op" style="" transform="matrix(1,0,0,1,18.9844,270.0703)"></rect><text x="10" y="20.609375" text-anchor="start" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="text-anchor: start; font-style: normal; font-variant-caps: normal; font-weight: normal; font-size: 14px; line-height: normal; font-family: sans-serif;" id="opt" class="flowchartt" font-size="14px" font-family="sans-serif" font-weight="normal" transform="matrix(1,0,0,1,18.9844,270.0703)"><tspan dy="6.8046875">Your Operation</tspan></text><path fill="#ffffff" stroke="#000000" d="M45.8203125,22.91015625L0,45.8203125L91.640625,91.640625L183.28125,45.8203125L91.640625,0L0,45.8203125" stroke-width="2" font-family="sans-serif" font-weight="normal" id="cond" class="flowchart" style="font-family: sans-serif; font-weight: normal;" transform="matrix(1,0,0,1,4,365.2891)"></path><text x="50.8203125" y="45.8203125" text-anchor="start" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="text-anchor: start; font-style: normal; font-variant-caps: normal; font-weight: normal; font-size: 14px; line-height: normal; font-family: sans-serif;" id="condt" class="flowchartt" font-size="14px" font-family="sans-serif" font-weight="normal" transform="matrix(1,0,0,1,4,365.2891)"><tspan dy="6.8046875">Yes or No?</tspan></text><rect x="0" y="0" width="52.265625" height="41.21875" r="20" rx="20" ry="20" fill="#ffffff" stroke="#000000" stroke-width="2" class="flowchart" id="e" style="" transform="matrix(1,0,0,1,69.5078,536.1406)"></rect><text x="10" y="20.609375" text-anchor="start" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="text-anchor: start; font-style: normal; font-variant-caps: normal; font-weight: normal; font-size: 14px; line-height: normal; font-family: sans-serif;" id="et" class="flowchartt" font-size="14px" font-family="sans-serif" font-weight="normal" transform="matrix(1,0,0,1,69.5078,536.1406)"><tspan dy="6.8046875">End</tspan></text><rect x="0" y="0" width="181.4375" height="41.21875" r="0" rx="0" ry="0" fill="#ffffff" stroke="#000000" stroke-width="2" class="flowchart" id="sub" style="" transform="matrix(1,0,0,1,242.2031,390.5)"></rect><rect x="10" y="0" width="161.4375" height="41.21875" r="0" rx="0" ry="0" fill="#ffffff" stroke="#000000" stroke-width="2" id="subi" font-family="sans-serif" font-weight="normal" transform="matrix(1,0,0,1,242.2031,390.5)" style="font-family: sans-serif; font-weight: normal;"></rect><text x="20" y="20.609375" text-anchor="start" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="text-anchor: start; font-style: normal; font-variant-caps: normal; font-weight: normal; font-size: 14px; line-height: normal; font-family: sans-serif;" id="subt" class="flowchartt" font-size="14px" font-family="sans-serif" font-weight="normal" transform="matrix(1,0,0,1,242.2031,390.5)"><tspan dy="6.8046875">Your Subroutine</tspan></text><path fill="none" stroke="#000000" d="M95.640625,70.4296875C95.640625,70.4296875,95.640625,132.16335821151733,95.640625,146.6321872845292" stroke-width="2" marker-end="url(#raphael-marker-endblock33)" font-family="sans-serif" font-weight="normal" style="font-family: sans-serif; font-weight: normal;"></path><path fill="none" stroke="#000000" d="M95.640625,190.859375C95.640625,190.859375,95.640625,252.59304571151733,95.640625,267.0618747845292" stroke-width="2" marker-end="url(#raphael-marker-endblock33)" font-family="sans-serif" font-weight="normal" style="font-family: sans-serif; font-weight: normal;"></path><path fill="none" stroke="#000000" d="M95.640625,311.2890625C95.640625,311.2890625,95.640625,350.94316244125366,95.640625,362.28950158460066" stroke-width="2" marker-end="url(#raphael-marker-endblock33)" font-family="sans-serif" font-weight="normal" style="font-family: sans-serif; font-weight: normal;"></path><path fill="none" stroke="#000000" d="M95.640625,456.9296875C95.640625,456.9296875,95.640625,518.6633582115173,95.640625,533.1321872845292" stroke-width="2" marker-end="url(#raphael-marker-endblock33)" font-family="sans-serif" font-weight="normal" style="font-family: sans-serif; font-weight: normal;"></path><text x="100.640625" y="466.9296875" text-anchor="start" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="text-anchor: start; font-style: normal; font-variant-caps: normal; font-weight: normal; font-size: 14px; line-height: normal; font-family: sans-serif;" font-size="14px" font-family="sans-serif" font-weight="normal"><tspan dy="6.8046875">yes</tspan></text><path fill="none" stroke="#000000" d="M187.28125,411.109375C187.28125,411.109375,227.7503170222044,411.109375,239.21128326872713,411.109375" stroke-width="2" marker-end="url(#raphael-marker-endblock33)" font-family="sans-serif" font-weight="normal" style="font-family: sans-serif; font-weight: normal;"></path><text x="192.28125" y="401.109375" text-anchor="start" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="text-anchor: start; font-style: normal; font-variant-caps: normal; font-weight: normal; font-size: 14px; line-height: normal; font-family: sans-serif;" font-size="14px" font-family="sans-serif" font-weight="normal"><tspan dy="6.8046875">no</tspan></text><path fill="none" stroke="#000000" d="M332.921875,431.71875C332.921875,431.71875,332.921875,456.71875,332.921875,456.71875C332.921875,456.71875,451.5625,456.71875,451.5625,456.71875C451.5625,456.71875,451.5625,124.640625,451.5625,124.640625C451.5625,124.640625,95.640625,124.640625,95.640625,124.640625C95.640625,124.640625,95.640625,140.01406955718994,95.640625,146.64987277425826" stroke-width="2" marker-end="url(#raphael-marker-endblock33)" font-family="sans-serif" font-weight="normal" style="font-family: sans-serif; font-weight: normal;"></path></svg></div>

**从上面的例子可以看出原生对流程图同样也是不支持, 所以只能采取迂回取巧方法了, 就是用一些支持流程图的编辑器先画出来, 然后截图放到这个不支持的页面上**

---

**更多语法参考:[流程图语法参考](http://adrai.github.io/flowchart.js/)**

---

## 代码

对于程序员来说这个功能是必不可少的, 插入程序代码的方式有两种, 一种是利用缩进(Tab), 
另一种是利用”`”符号（一般在ESC键下方）包裹代码。

**语法说明:**

1. 插入行内代码, 即插入一个单词或者一句代码的情况, 使用\`code`这样的形式插入。
2. 插入多行代码, 可以使用缩进或者“\` code “`,具体看示例。

**注意: 缩进式插入前方必须有空行**

### 行内式

**代码:**

```
C语言里的函数 `scanf()` 怎么使用？
```

**显示效果:**

C语言里的函数 `scanf()` 怎么使用？

### 缩进式多行代码

缩进 4 个空格或是 1 个制表符

一个代码区块会一直持续到没有缩进的那一行（或是文件结尾）。

**代码:**

```
    # 空一行
    #include <stdio.h>
    int main(void)
    {
    printf("Hello world\n");
    }
```

**显示效果:**


    #include <stdio.h>
    int main(void)
    {
    printf("Hello world\n");
    }


### 包裹多行代码

**代码:**

```
#include <stdio.h>;
int main(void)
{
printf("Hello world\n");
}
```

**显示效果:**

```
#include <stdio.h>;
int main(void)
{
printf("Hello world\n");
}
```

### HTML原始码

在代码区块里面,& 、 &lt; 和 &gt; 会自动转成 HTML 实体, 这样的方式让你非常容易使用 Markdown 插入范例用的 HTML 原始码, 只需要复制贴上, 剩下的 Markdown 都会帮你处理, 例如:

***Tip: 值得注意的是，Markdown对空格、空行很敏感，在解析成HTML时会自动添加一些\<br\>标签导致出现大段空白，所以HTML块要尽量紧凑。***

**代码:**

第一个例子:
``` html
<div>&copy; 2007 Foo Corporation</div> 
```
第二个例子:
``` html
<table><tbody><tr><th rowspan="2">值班人员</th><th>星期一</th><th>星期二</th><th>星期三</th></tr><tr><td>李强</td><td>张明</td><td>王平</td></tr></tbody></table>
```

**显示效果:**

第一个例子:
<div>&copy; 2007 Foo Corporation</div> 

第二个例子:
<table><tbody><tr><th rowspan="2">值班人员</th><th>星期一</th><th>星期二</th><th>星期三</th></tr><tr><td>李强</td><td>张明</td><td>王平</td></tr></tbody></table>

<br>

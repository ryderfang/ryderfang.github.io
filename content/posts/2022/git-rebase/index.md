---
title: "关于 Rebase 容易被坑的那些事"
date: 2022-03-19T15:16:29+08:00
categories: [Manual, Git]
tags: [git, rebase, merge]
---

Git 操作是程序员必须掌握的基本技能。刚毕业那会，大家还都使用 svn 作为版本管理工具。

但近些年大家基本都改用 git 了，甚至在我们项目内部 UI 切图都开始使用 git 管理了。

<!--more-->

> 感谢 [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) 的伟大发明！

一般情况下，我们常用的命令无非是：

```bash
$ git init
$ git checkout 
$ git add
$ git pull
$ git push
$ git merge
```

在说 rebase 前，先重点强调一下 **黄金法则**：

{{< alert >}}
永远不要在公共分支上使用 rebase !!
{{< /alert >}}

rebase 作为一个进阶命令，常常与 merge 放在一起比较。

## rebase 与 merge

```bash
$ git checkout feature
$ git merge main
// or
$ git merge feature main
```

将 main 分支合并到 feature：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-ZUkpmx.png)

这样在 feature 分支上会产生一个新的 commit，这是一个 merge commit。

而对于 rebase:

```bash
$ git checkout feature 
$ git rebase main
```

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-tiBfqE.png)

可以看到 feature 分支所有 commit 都被放到了 main 前面，整个 history 形成了一条直线。

值得注意的是，feature 的所有 commit 都被重建了，它们的 hash 已经不是原来的那个了！

所以，rebase 相对于 merge 来说，优点是：

* 时间线更漂亮，符号强迫症和整洁癖的喜好

为了做到这个，它对 安全性 (safety) 和 可追溯性 (traceability) 做了折衷[^1]，如果不遵循 [rebase 黄金法则](https://www.atlassian.com/git/tutorials/merging-vs-rebasing#the-golden-rule-of-rebasing)，将带来灾难！

rebase 的缺点很明显：

* 不当的使用容易造成严重后果
* 难以追溯历史，比如上面的 feature 分支在 rebase 之后，无法知道是什么时候从 main 切出进行的修改。无法知道什么时候合入的 main 分支。

## git pull

首先，git pull 是两个动作的合并，即 git fetch + git merge FETCH_HEAD

比如 git pull origin master，首先拉取 origin/master，再将本地分支与 origin/master 执行 merge 操作。

如果你本地有一个 commit，但是没有提交到远程；同时你的同事在同一个分支上提交了代码。你进行 fetch 的时候会发现，本地分支既 ahead 又 behind：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-JbTiR1.png)

* 如果这个时候执行 merge 操作：

> Merge made by the 'recursive' strategy.

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-zMKyn3.png)

会产生一个 merge 节点！

* 如果执行的是 rebase 呢？

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-HO9IfP.png)

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-IiZCmQ.png)

会将本地的 commit 重建，并放到最上面。（可以看到 commit id 不一样了）

然后 push 之后，时间线就成了一条直线！

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-p74J3h.png)

所以，git pull 这个操作，大部分情况来说，使用 --rebase 更合适！

我们可以设置 git pull 默认使用 rebase 选项：

```bash
# 仅设置 master 分支生效
git config branch.master.rebase true

# 对所有 tracking 的 branch 生效
git config branch.autosetuprebase always

# 对所有 pull 操作生效
git config pull.rebase true
```

> 以上仅对当前目录的 git 生效，如果要全局生效，记得加上 `--global` 选项。

```bash
# 手动编辑更方便！
git config --global --edit
```

## rebase 的禁忌

再次复习一下 **黄金法则**：

{{< alert >}}
永远不要在公共分支上使用 rebase !!
{{< /alert >}}

如果你和同事公用了一个 feature 分支，而你使用 rebase 同步主干。很有可能弄丢同事的代码！

我们来看下是怎么出现的：

1. 首先我们从 master 切出一个 feature 分支：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-MFAPD6.png)

这个时候有两个同事同时在这个分支上开发，相安无事。

2. 某天，有个同事说，主干上有一些更新，我们要不要同步一下到 feature 分支：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-GNzNkg.png)

3. “好啊，好啊”，那么怎么同步呢？要不要试试新学的 `rebase` 命令 ?!

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-f059b760-97b9-4ecf-b9e5-b0cb9da444fd.jpg)

3.1. 你的同事一边说“好啊”，一边在自己本地的 feature 上提交了好几次，并 push 到了远程！

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-w0g8ep.png)

你并不知道，这样你本地的 feature 分支并没有完全包含同事的提交，与此同时，你开始了可怕的 rebase 操作：

这时，你发现提交不上去：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-01S6Nb.png)

4. 于是，头脑一热，你决定大力出奇迹，`--force` 一把：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-AbX7Kd.png)

这时，你同事更新一下代码，发现！“我的代码怎么没了？？！！”

### 怎么办？

有办法补救嘛？有！

让你的同事使用 `git reflog`：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-gIu5YZ.png)

找到丢失的 commit，通过 `git cherry-pick [commit-id]` 提交到 feature 分支即可！

但是！我们还是不要随便使用 `--force` 来制造这种凶险事件了。

看下面这个场景：

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-90mrdW.png)

前面介绍过，超前是本地分支有三个变更，落后是远程分支有四个变更没有同步过来。

如果我们强行 push 就会丢失远程的 commit，所以我们试一下 `--force-with-lease` 参数：

没有区别，还是提交上去了！

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-03-21-BWneVQ.png)

在这种明知道本地落后，仍然强行提交的情况下，`--force-with-lease` 的作用与 `--force` 是一样的！

正常的做法是：

> git pull --rebase 更新本地分支

而 `git push --force-with-lease` 能够解决的是，在 `rebase-push` 过程中，有其他人提交到该分支时的，这次提交操作会被拒绝。相对来说更安全一点。

所以，总得来说，还是**黄金法则**：

{{< alert >}}
永远不要在公共分支上使用 rebase !!
{{< /alert >}}

> 多人协作分支，同步主干，请使用 merge !!


[^1]:https://www.atlassian.com/git/tutorials/merging-vs-rebasing
[^2]:https://git-scm.com/book/en/v2/Git-Branching-Rebasing
[^3]:https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%8F%98%E5%9F%BA

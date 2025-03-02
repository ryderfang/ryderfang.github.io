---
title: "使用 AI 辅助 Weekly Contest"
date: 2025-03-02T12:58:58+08:00
categories: [Contest]
tags: [AI, DeepSeek]
---

一句话总结这次使用 AI 的效果 [Weekly Contest 439](https://leetcode.com/contest/weekly-contest-439/)，就是一塌糊涂。

比较有意思的是在复制完 Leetcode 题目到 [DeepSeek](chat.deepseek.com) 之后，LeetCode 会自动在 Prompt 中添加私货，猜测用来检测是否是 AI 写的？

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2025-03-02-piAyna-IPCBlP.png)

但是 AI 似乎没那么听话？

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2025-03-02-DcUMoF-pLTpvK.png)

另一方面，LeetCode 官方竟然直接提供了 [AI 排行榜](https://leetcode.com/contest/weekly-contest-439/ranking/?region=llm)

那么我用的是假的 DeepSeek 咯？

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2025-03-02-Xjv58R-DgOYoa.png)

## 3471. Find the Largest Almost Missing Integer

https://leetcode.com/problems/find-the-largest-almost-missing-integer/

第一道 Easy 题，AI 快速地给出了正确的解答，但是也只是最容易的暴力解法，没有任何的优化，好在 Easy 通常不用卡时间复杂度。

```swift
func largestInteger(_ nums: [Int], _ k: Int) -> Int {
    let n = nums.count
    var freq = [Int: Int]()

    for i in 0...(n - k) {
        let subarray = Array(nums[i..<(i + k)])
        let uniqueElements = Set(subarray)
        for x in uniqueElements {
            freq[x] = (freq[x] ?? 0) + 1
        }
    }

    var result = -1
    for (x, count) in freq {
        if count == 1 {
            result = max(result, x)
        }
    }

    return result
}
```

## 3472. Longest Palindromic Subsequence After at Most K Operations

https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

这题 AI 给出了错误的答案，然而在我给出一个结果错误的 Case 之后，AI 还不承认 !?

<img src='https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2025-03-02-R4RApo-q0aFzP.png' width='50%' />

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2025-03-02-UD3rSR-h0JQQE.png)

就一本正经胡说八道咯~

## 3473. Sum of K Subarrays With Length at Least M

https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

这一道题，AI 第一次写出的代码存在溢出问题而且结果错误，经过提示后做了优化，但结果超时，最终也没有给出正确的解答。

## 3474. Lexicographically Smallest Generated String

https://leetcode.com/problems/lexicographically-smallest-generated-string/

一直在纠结前两个 Medium 的问题，压根没时间看 Hard。

## EOF

总之，这是一次失败的尝试，个人使用下来目前的 LLM 工具非常依赖 Prompt 和人类自己的判断，同时针对新问题很难一次就给出最优的解答。

所以，我个人对所谓 “AI 会让程序员失业” 的论调一直嗤之以鼻。

> 工具的属性决定了它们永远无法取代使用工具的人，除非有一天它们产生了自我意识，希望这一天永远不要到来，否则人类就是末日将至。
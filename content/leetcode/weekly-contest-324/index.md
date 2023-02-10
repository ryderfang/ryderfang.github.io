---
title: "题解 Weekly Contest 324"
date: 2022-12-18T14:15:57+08:00
categories: [Contest]
tags: []
---

{{< katex >}}

这周只做出两题，竟然有两道 Hard，但是最后一题明明是一道 Easy 啊！！

https://leetcode.com/contest/weekly-contest-324/

## 2506. Count Pairs Of Similar Strings

https://leetcode.com/problems/count-pairs-of-similar-strings/

这个没什么好说的，枚举所有 pair 就行

```swift
class Solution {
    func similarPairs(_ words: [String]) -> Int {
        var ans = 0
        let n = words.count
        guard n > 1 else { return 0 }
        let sets = words.map { Set($0) }
        for i in 0..<n-1 {
            for j in i+1..<n {
                if sets[i] == sets[j] {
                    ans += 1
                }
            }
        }
        return ans
    }
}
```

## 2507. Smallest Value After Replacing With Sum of Prime Factors

https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

* 输入一个数 \\(n, n \in [2, 10^5] \\)
* 计算 n 的所有素数因子，想加之和替代 n
* 重复上述过程，直到最小

直接暴力也行，先计算出素数再模拟也行。

```swift
class Solution {
    func smallestValue(_ n: Int) -> Int {
        let Limit = 100001
        var isPrime = [Bool](repeating: true, count: Limit)
        (isPrime[0], isPrime[1]) = (false, false)
        var plist = [Int]()
        for i in 2..<Limit {
            if isPrime[i] {
                plist.append(i)
            }
            for p in plist {
                guard p * i < Limit else { break }
                isPrime[p * i] = false
                // 避免重复，每个合数只需要被最小的素数筛过
                if i % p == 0 {
                    break
                }
            }
        }
        var tmp = n
        while !isPrime[tmp] {
            let pre = tmp
            var next = 0
            var i = 0
            while i < plist.count && !isPrime[tmp] {
                if tmp % plist[i] == 0 {
                    tmp /= plist[i]
                    next += plist[i]
                } else {
                    i += 1
                }
            }
            next += tmp
            tmp = next
            guard next != pre else { break }
        }
        return tmp
    }
}
```

## 2508. Add Edges to Make Degrees of All Nodes Even

https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

* 给定一个无向图（不一定连通），求能否添加至多两条边，让图的每个顶点的度是偶数。

> 顶点的度，就是与它想邻的顶点的个数

首先算出各个顶点的度，统计当前度是奇数的顶点的个数。

1. 如果多于 `4` 个，无解
2. 如果是 `0` 个，则直接满足要求
3. 如果是 `1` 个，无解
4. 如果有 `2` 个，
   - 要么直接将它们俩相连（它们之前本身没有边的前提下）
   - 要么引入第三个节点，分别将它与两者相连
5. 如果有 `3` 个，无解（添加一条、两条边都不可行）
6. 如果有 `4` 个，可以枚举添加边的情况，看是否可行。

```swift
class Solution {
    func isPossible(_ n: Int, _ edges: [[Int]]) -> Bool {
        var mp = [Int: [Int]]()
        for e in edges {
            mp[e[0], default: []].append(e[1])
            mp[e[1], default: []].append(e[0])
        }

        func _add(_ u: Int, _ v: Int) -> Bool {
            return !mp[u, default: []].contains(v)
        }

        var ans = [Int]()
        for (k, v) in mp {
            if v.count % 2 == 1 {
                ans.append(k)
            }
            guard ans.count <= 4 else { return false }
        }
        if ans.count == 0 {
            return true
        }
        if ans.count == 2 {
            if _add(ans[0], ans[1]) {
                return true
            }
            // 引入第三个节点，多加一条边
            for x in mp.keys {
                guard x != ans[0] && x != ans[1] else { continue }
                if _add(x, ans[0]) && _add(x, ans[1]) {
                    return true
                }
            }
            return false
        } else if ans.count == 4 {
            if _add(ans[0], ans[1]) && _add(ans[2], ans[3]) {
                return true
            }
            if _add(ans[0], ans[2]) && _add(ans[1], ans[3]) {
                return true
            }
            if _add(ans[0], ans[3]) && _add(ans[1], ans[2]) {
                return true
            }
            return false
        }
        return false
    }
}
```

## 2509. Cycle Length Queries in a Tree

https://leetcode.com/problems/cycle-length-queries-in-a-tree/

粗看好像挺复杂，其实就是：

> 找出两个节点的最近公共祖先，然后计算它们到这个祖先的距离之和

再 `+1`（添加的边）即得结果。

由于给出的是完全二叉树，一个节点的子节点是固定的：

\\(n -> (2 * n, 2 * n + 1)\\)

那么一个节点的父节点就是 \\( n / 2\\)

这样，拿输入的两个节点，依次计算父节点，直接找到公共祖先，同时计数即可。

> 确实是一道 Easy 题啊！可惜比赛中没想出来。

```swift
class Solution {
    func cycleLengthQueries(_ n: Int, _ queries: [[Int]]) -> [Int] {
        var ans = [Int]()
        for q in queries {
            var (u, v) = (q[0], q[1])
            var count = 0
            while u != v {
                if u > v {
                    u /= 2
                } else {
                    v /= 2
                }
                count += 1
            }
            ans.append(count + 1)
        }
        return ans
    }
}
```

## EOF

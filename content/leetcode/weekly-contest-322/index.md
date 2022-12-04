---
title: "题解 Weekly Contest 322"
date: 2022-12-04T13:25:57+08:00
categories: [LeetCode, Contest]
tags: []
---

{{< katex >}}

这周还是只做出来 3 题。

https://leetcode.com/contest/weekly-contest-322/

## 2490. Circular Sentence

https://leetcode.com/problems/circular-sentence/

简单题，空格分词。

```swift
class Solution {
    func isCircularSentence(_ sentence: String) -> Bool {
        let words = sentence.components(separatedBy: " ")
        let first = words[0].first!
        var last = words[0].last!
        for x in words.dropFirst() {
            guard x.first == last else { return false }
            last = x.last!
        }
        return first == last
    }
}
```


## 2491. Divide Players Into Teams of Equal Skill

https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

题意：将 `n` 个数两两分成 `n/2` 组，每组的和都相等。求各组两个数的乘积之和。

$$
\displaystyle\sum_{0<i<n/2} { group[i][0] * group[i][1] }
$$

* 首先，求整个数组的和，除以 `n/2`，如果能除尽，就可以得到每个组的和；否则无解。

* 其次，统计每个数出现的个数。

* 出现一次减少一次；这里有个问题是要区分：
    1. 某个数在原数组中就没有：`-1`，如果是这种情况，说明无解。
    2. 某个数是被用完了：`0`，这种情况直接跳过。

```swift
class Solution {
    func dividePlayers(_ skill: [Int]) -> Int {
        let n = skill.count
        guard n > 2 else { return skill[0] * skill[1] }
        var sum = 0
        var mp =  [Int: Int]()
        for x in skill {
            sum += x
            if mp[x, default: -1] < 0 {
                mp[x] = 1
            } else {
                mp[x, default: -1] += 1
            }
        }
        guard sum % (n / 2) == 0 else { return -1 }
        sum /= (n / 2)
        var ans = 0
        for x in skill {
            guard mp[x, default: -1] != 0 else { continue }
            mp[x, default: -1] -= 1
            if mp[sum - x, default: -1] > 0 {
                mp[sum - x, default: -1] -= 1
                ans += (x * (sum - x))
            } else {
                return -1
            }
        }
        return ans
    }
}
```

## 2492. Minimum Score of a Path Between Two Cities

https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

一个表面是图论，其实是并查集的题。

* `n` 个节点的无向图，可能非连通。

* 求节点 `1` 到节点 `n` 路径上最小的边的大小。需要注意的是路径可以重复经过顶点。

所以，其实就是求 `1` 和 `n` 连通图上的最短边。

```swift
class Solution {
    func minScore(_ n: Int, _ roads: [[Int]]) -> Int {
        var uf = [Int](repeating: -1, count: n + 1)
        for i in 0...n {
            uf[i] = i
        }
        func _find(_ x: Int) -> Int {
            if uf[x] == x {
                return x
            } else {
                uf[x] = _find(uf[x])
                return uf[x]
            }
        }

        func _merge(_ i: Int, _ j: Int) {
            let x = min(i, j)
            let y = max(i, j)
            uf[_find(x)] = _find(y)
        }
        for edge in roads {
            _merge(edge[0], edge[1])
        }
        var ans = Int.max
        for edge in roads {
            if _find(edge[0]) == _find(n) || _find(edge[1]) == _find(n) {
                ans = min(ans, edge[2])
            }
        }
        return ans
    }
}
```

## 2493. Divide Nodes Into the Maximum Number of Groups

https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

TBU

## EOF
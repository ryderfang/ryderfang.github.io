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

题意是：

> 给定一个无向图，将图中所有顶点按照两条规则分组，求最大的分组数。
  1. 一个顶点只在一个分组中
  2. 有边相连的两个点，必须在想邻的分组里

注意到：

* 输入的图不一定连通。
* 对于非连通的图，只需要分别求每个连通区域的分组数，然后相加即可。
* 每个连通区域的分组数，可能通过枚举各个顶点，通过 BFS 得到，分组数就是 BFS 的深度。

关键点：

* 在 BFS 过程中，每一层的节点不能相连 （也就是二分图 `bipartite graph`）
* 同一个连通图内的点，可能使用并查集判断或者 DFS 获取

```swift
class Solution {
    func magnificentSets(_ n: Int, _ edges: [[Int]]) -> Int {
        // Union Find
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

        var path = [Int: [Int]]()
        var conn = [[Int]](repeating: [Int](repeating: 0, count: n + 1), count: n + 1)
        for edge in edges {
            path[edge[0], default: []].append(edge[1])
            path[edge[1], default: []].append(edge[0])
            conn[edge[0]][edge[1]] = 1
            conn[edge[1]][edge[0]] = 1
            _merge(edge[0], edge[1])
        }

        // Find Components
        var components = [Int: [Int]]()
        for i in 1...n {
            components[_find(i), default: []].append(i)
        }

        func _bfs(_ visited: [Int], _ queue: [Int], _ depth: Int) -> Int {
            var v = visited
            for x in queue {
                v[x] = 1
            }
            var queue = queue.flatMap { path[$0, default: []] }
            queue = Array(Set(queue)).filter { v[$0] == 0 }
            let sz = queue.count
            if sz == 0 {
                return depth
            }

            // check connection
            for i in 0..<sz-1 {
                for j in i+1..<sz {
                    if conn[queue[i]][queue[j]] == 1 {
                        return -1
                    }
                }
            }

            return _bfs(v, queue, depth + 1)
        }

        var ans = 0
        for comp in components.values {
            var maxLevel = -1
            for v in comp {
                let tmp = _bfs([Int](repeating: 0, count: n + 1), [v], 1)
                if tmp == -1 {
                    continue
                }
                maxLevel = max(maxLevel, tmp)
            }
            guard maxLevel > 0 else { return -1 }
            ans += maxLevel
        }
        return ans
    }
}
```

整体框架就是这样，有几处细节可以优化一下。



### 优化1

* 判断当前层是否有连通的线段，可以通过比较当前层（本身就是上一层的 neighbor 的子集）的 neighbor 和上一层的 neighbor 来判断。如果它们有重合，那么说明当前层内有连通。

* 如果有连通，则整个图不是二分图，无法找到满足条件的分组，直接返回 -1。

```swift
func _bfs(_ visited: [Int], _ queue: [Int], _ lastLevel: Set<Int>, _ depth: Int) -> Int {
    var v = visited
    for x in queue {
        v[x] = 1
    }
    var queue = queue.flatMap { path[$0, default: []] }
    var nextLevel = Set(queue)
    if nextLevel.intersection(lastLevel).count > 0 {
        return -1
    }
    queue = Array(nextLevel).filter { v[$0] == 0 }
    guard queue.count > 0 else { return depth }
    return _bfs(v, queue, nextLevel, depth + 1)
}
```

### 优化2

不使用并查集，使用 DFS 来生成 `components`。

```swift
func magnificentSets(_ n: Int, _ edges: [[Int]]) -> Int {
    var path = [Int: [Int]]()
    for edge in edges {
        path[edge[0], default: []].append(edge[1])
        path[edge[1], default: []].append(edge[0])
    }

    // Find Components
    var components = [Int: [Int]]()
    var visit = [Int](repeating: 0, count: n + 1)
    var groupId = 0
    for i in 1...n {
        guard visit[i] == 0 else { continue }
        _dfs(i, &visit, groupId)
        groupId += 1
    }

    // DFS
    func _dfs(_ v: Int, _ visit: inout [Int], _ groupId: Int) {
        visit[v] = 1
        components[groupId, default: []].append(v)
        for x in path[v, default: []] {
            _dfs(x, &visit, groupId)
        }
    }

    func _bfs(_ visited: [Int], _ queue: [Int], _ lastLevel: Set<Int>, _ depth: Int) -> Int {
        var v = visited
        for x in queue {
            v[x] = 1
        }
        var queue = queue.flatMap { path[$0, default: []] }
        var nextLevel = Set(queue)
        if nextLevel.intersection(lastLevel).count > 0 {
            return -1
        }
        queue = Array(nextLevel).filter { v[$0] == 0 }
        guard queue.count > 0 else { return depth }
        return _bfs(v, queue, nextLevel, depth + 1)
    }

    var ans = 0
    for comp in components.values {
        var maxLevel = -1
        for v in comp {
            let tmp = _bfs([Int](repeating: 0, count: n + 1), [v], [], 1)
            guard tmp > 0 else { return -1 }
            maxLevel = max(maxLevel, tmp)
        }
        ans += maxLevel
    }
    return ans
}
```

## EOF
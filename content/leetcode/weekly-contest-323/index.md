---
title: "题解 Weekly Contest 323"
date: 2022-12-11T15:03:19+08:00
categories: [Contest]
tags: []
---

{{< katex >}}

这周相对简单一点，最后一道 hard 比赛完不久也搞出来了。

https://leetcode.com/contest/weekly-contest-323/

## 2500. Delete Greatest Value in Each Row

https://leetcode.com/problems/delete-greatest-value-in-each-row/

简单题，每次从各行中找一个最大的。然后求和。

```swift
class Solution {
    func deleteGreatestValue(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var grid = grid.map { $0.sorted() }
        var ans = 0
        for j in 0..<n {
            var tmp = 0
            for i in 0..<m {
                tmp = max(tmp, grid[i][j])
            }
            ans += tmp
        }
        return ans
    }
}
```

## 2501. Longest Square Streak in an Array

https://leetcode.com/problems/longest-square-streak-in-an-array/

求数组的最长子序列的长度，子序列需要满足：

1. 最少两个数

2. 排序之后，当前数最前一个数的平方

$$
  sub[i] = sub[i-1] * sub[i-1], i \in [1...)
$$

注意到数据量 `2 <= nums[i] <= 10^5`，所以这个子序列第一位最大也只能是

\\( \sqrt{10^5} = 317 \\)，遍历即可。

```swift
class Solution {
    func longestSquareStreak(_ nums: [Int]) -> Int {
        // 317 ^ 2 > 100000
        let n = 317
        var mp = [Int: Int]()
        for x in nums {
            mp[x, default: 0] += 1
        }
        var ans = -1
        for i in 2..<n {
            var tmp = 0
            var j = i
            while mp[j, default: 0] > 0 {
                tmp += 1
                j = j * j
            }
            if tmp > 1 {
                ans = max(ans, tmp)
            }
        }
        return ans
    }
}
```

## 2502. Design Memory Allocator

模拟一个内存分配器

```swift
class Allocator {
    var array: [Int]
    var n = 0

    init(_ n: Int) {
        array = [Int](repeating: 0, count: n)
        self.n = n
    }

    func allocate(_ size: Int, _ mID: Int) -> Int {
        var i = 0
        var count = 0, beg = 0
        while i < n && count < size {
            while i < n && array[i] != 0 {
                i += 1
            }
            beg = i
            var found = false
            while i < n && array[i] == 0 {
                count += 1
                if count == size {
                    found = true
                    break
                }
                i += 1
            }
            if found {
                for j in beg..<beg+size {
                    array[j] = mID
                }
                return beg
            } else {
                count = 0
            }
        }
        return -1
    }

    func free(_ mID: Int) -> Int {
        var count = 0
        for i in 0..<n {
            if array[i] == mID {
                count += 1
                array[i] = 0
            }
        }
        return count
    }
}
```

## 2503. Maximum Number of Points From Grid Queries

https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

### 思路一

如果是拿到 `query` 再去搜索会超时，所以可以提前得到每个位置能被访问到的最小 `query` 值。

显然 `(0, 0)` 这个点至少是 `grid[0][0] + 1` 才能被访问。更广泛的，对于节点 `(i, j)`，

* 首先要严格大于 `grid[i][j]`
* 其次要大于等于周围四个方向中最小的一个 `query` 值

$$
\begin{align}
  query[0][0] &= grid[0][0] + 1 \newline
  query[i][j] &= max(min \begin{cases} 
               query[i-1][j], \newline
               query[i][j-1], \newline
               query[i+1][j], \newline
               query[i][j+1],  \newline
               \end{cases},
                grid[i][j] + 1)
\end{align}
$$

因为这种迭代是动态的，一次遍历可能不够。

```swift
class Solution {
    func maxPoints(_ grid: [[Int]], _ queries: [Int]) -> [Int] {
        let m = grid.count
        let n = grid[0].count
        var query = [[Int]](repeating: [Int](repeating: Int.max, count: n), count: m)
        query[0][0] = grid[0][0] + 1
        var reLoop = true
        while reLoop {
            reLoop = false
            for i in 0..<m {
                for j in 0..<n {
                    if i == 0 && j == 0 {
                        continue
                    }
                    var tmp = Int.max
                    if i > 0 {
                        tmp = min(tmp, query[i-1][j])
                    }
                    if j > 0 {
                        tmp = min(tmp, query[i][j-1])
                    }
                    if i < m - 1 {
                        tmp = min(tmp, query[i+1][j])
                    }
                    if j < n - 1 {
                        tmp = min(tmp, query[i][j+1])
                    }
                    let new = min(max(tmp, grid[i][j] + 1), query[i][j])
                    if query[i][j] != new {
                        query[i][j] = new
                        reLoop = true
                    }
                }
            }
        }
        var ans = [Int]()
        for x in queries {
            var result = 0
            for i in 0..<m {
                for j in 0..<n {
                    if query[i][j] <= x {
                        result += 1
                    }
                }
            }
            ans.append(result)
        }
        return ans
    }
}
```

### 思路二

1. 首先，对 `queries` 按从小到大排序，注意要 **记住它们的位置**，便于输出。
2. 从小到大取每个 `query` 作为 `target`，对 `grid` 进行 `BFS` 搜索。
   - 直到当前 `queue` 中找不到比 `target` 小的数为止。
   - 换新的 `target = query`，从中断的 `BFS` 继续。
3. 直到整个 `BFS` 结束。

这样做的好处是：
  * 只需要进行一次完整的 `BFS`，效率更高
  * 对于 \\( query[i-1] < query[i] \\) 来说，前者的结果肯定包含了后者的， 所以前者的结果直接累加到后者，而不用重复搜索。
  * 对于相同的 query 直接返回


```swift
class Solution {
    func maxPoints(_ grid: [[Int]], _ queries: [Int]) -> [Int] {
        let m = grid.count
        let n = grid[0].count
        var sorted = [(Int, Int, Int)]()
        for (i, q) in queries.enumerated() {
            sorted.append((i, q, 0))
        }
        sorted = sorted.sorted(by: { $0.1 < $1.1 })

        var visited = [[Int]](repeating: [Int](repeating: 0, count: n), count: m)
        var queue: [(Int, Int, Int)] = [(0, 0, grid[0][0])]
        func _bfs(_ target: Int, _ result: inout Int) {
            while !queue.isEmpty {
                guard let idx = queue.firstIndex(where: { $0.2 < target }) else { return }
                let r = queue[idx].0
                let c = queue[idx].1
                queue.remove(at: idx)
                visited[r][c] = 1
                result += 1

                if r > 0 && visited[r-1][c] == 0 {
                    queue.append((r - 1, c, grid[r-1][c]))
                    visited[r-1][c] = 1
                }
                if c > 0 && visited[r][c-1] == 0 {
                    queue.append((r, c - 1, grid[r][c-1]))
                    visited[r][c-1] = 1
                }
                if r < m - 1 && visited[r+1][c] == 0 {
                    queue.append((r + 1, c, grid[r+1][c]))
                    visited[r+1][c] = 1
                }
                if c < n - 1 && visited[r][c+1] == 0 {
                    queue.append((r, c + 1, grid[r][c+1]))
                    visited[r][c+1] = 1
                }
            }
        }

        let q = queries.count
        for i in 0..<q {
            if i > 0 {
                // 更大的 target 走过的路包含较小的 target
                sorted[i].2 += sorted[i-1].2
                // 相同 query 不需要重复计算
                if sorted[i].1 == sorted[i-1].1 {
                    sorted[i].2 = sorted[i-1].2
                    continue
                }
            }
            _bfs(sorted[i].1, &sorted[i].2)
        }


        var ans = [Int](repeating: 0, count: q)
        for pair in sorted {
            ans[pair.0] = pair.2
        }
        return ans
    }
}
```

## EOF
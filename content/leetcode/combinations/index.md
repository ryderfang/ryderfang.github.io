---
title: "组合算法"
date: 2022-05-25T19:26:54+08:00
categories: [Combinations]
tags: []
---

## 概念

{{< katex >}}

组合，就是在排列的基础上，去除顺序的因素。对于同一组数，只计数 1。

$$
  C_n^m = \frac {P_n^m}{P_m} = \frac {n!}{m!(n-m)!} = \frac {n(n-1)(n-2)...(n-m+1)}{m!}
$$

组合总数：\\( \displaystyle\sum_{k=0}^nC_n^k = C_n^0 + C_n^1 + ... + C_n^n = 2^n \\)

性质：

$$
\begin{aligned}
C_n^m&=C_n^{n-m}\newline
C_{n}^m&=C_{n-1}^m + C_{n-1}^{m-1}
\nonumber
\end{aligned}
$$

## 例题

### 无重复组合

* [77. Combinations](https://leetcode.com/problems/combinations/)

就是求所有 \\(C_n^k\\) 的组合

```swift
func combine(_ n: Int, _ k: Int) -> [[Int]] {
    var used = [Bool](repeating: false, count: n)
    var ans = [[Int]]()
    func _p(_ index: Int, _ count: Int) {
        if count == 0 {
            ans.append(used.enumerated().filter{ $0.element }.map{ $0.offset + 1 })
            return
        }
        for i in index..<n {
            used[i] = true
            _p(i + 1, count - 1)
            used[i] = false
        }
    }
    _p(0, k)
    return ans
}
```

这里 `used.enumerated().filter{ $0.element }.map{ $0.offset + 1 }` 是过滤所有被标记使用的节点，并返回下标。

一种 `Swiftier` 的写法。

当然我们也可以不使用标记数组。

```swift
func combine(_ n: Int, _ k: Int) -> [[Int]] {
    var ans = [[Int]]()
    func _p(_ index: Int, _ res: [Int]) {
        if res.count == k {
            ans.append(res)
            return
        }
        for i in index..<n {
            if n - i < k - res.count {
                break
            }
            var tmp = res
            tmp.append(i + 1)
            _p(i + 1, tmp)
            tmp.removeLast()
        }
    }
    _p(0, [])
    return ans
}
```

一个小优化：`if n - i < k - res.count { break }`，表示即使剩余的元素全选也无法达到 \\(k\\) 个时直接返回。

### 子集

* [78. Subsets](https://leetcode.com/problems/subsets/)
* [90. Subsets II](https://leetcode.com/problems/subsets-ii/)

一个集合的所有子集，也称为幂集 (`Power Set`)，它的总数是

$$
  C_n^0 + C_n^1 + ... + C_n^n = 2^n
$$

在回溯的时候去掉 `k` 的限制即可：

```swift
func subsets(_ nums: [Int]) -> [[Int]] {
    var ans = [[Int]]()
    let n = nums.count
    func _p(_ index: Int, _ res: [Int]) {
        ans.append(res)
        for i in index..<n {
            var tmp = res
            tmp.append(nums[i])
            _p(i + 1, tmp)
            tmp.removeLast()
        }
    }
    _p(0, [])
    return ans
}
```

还有一种很秀的写法：

```swift
func subsets(_ nums: [Int]) -> [[Int]] {
    var ans = [[Int]]()
    ans.append([])
    return nums.reduce(into: ans, {
        r, c in
        r = r + r.map{ $0 + [c] }
    })
}
```

### 有重复子集

对于有重复元素的问题，最简单的方法是用 `Set` 去重

```swift
func subsetsWithDup(_ nums: [Int]) -> [[Int]] {
    var ans = Set<[Int]>()
    ans.insert([])
    for num in nums {
        for item in ans {
            var tmp = item
            tmp.append(num)
            tmp.sort()
            ans.insert(tmp)
        }
    }
    return Array(ans)
}
```

参考之前排列的回溯写法：

```swift
func subsetsWithDup2(_ nums: [Int]) -> [[Int]] {
    guard !nums.isEmpty else { return [] }

    let n = nums.count
    var ans: [[Int]] = [[]]
    let a = nums.sorted()
    func _backTracking(_ index: Int, _ result: inout [Int]) {
        guard index < n else {
            return
        }
        for i in index..<n {
            if (i > index && a[i] == a[i-1]) {
                continue
            }
            result.append(a[i])
            ans.append(result)
            _backTracking(i + 1, &result)
            result.removeLast()
        }
    }
    
    var tmp: [Int] = []
    _backTracking(0, &tmp)
    return ans
}
```

以上。
---
title: "在已排序的矩阵中找出第 k 大的数"
date: 2023-11-30T17:40:10+08:00
categories: []
tags: []
---

Leetcode 经典题：

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

> 这个问题题意很简单，在一个行和列都是非递减排序的矩阵中，求第 k 小的数。

题目下面有两个 follow up：

1. Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?

2. Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading [this paper](http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf) fun.

第一条，我没有仔细思考过，我觉得可能的解法是将整个 matrix 原地排序。（参考 [#更优解法](./select_kth_in_sorted_matrix/#更优解法)）

第二条中提到了这个论文，最近花时间看了下，是一篇非常古早的论文了（1984 年）。本质是是一种分治方法。

## 常规解法

最容易想到的是用数组读出来，然后排序。显然时间复杂度 O(n^2log(n^2))，空间复杂度 O(n^2)。

进一步利用优先队列优化一下，首先将第一行放入队列，然后每次 dequeue 一个，计数，并 enqueue 一个同一列的数。直到第 k 个结束。

这样的时间复杂度 O(nlogn)，空间复杂度 O(n)。

```swift
#if !LC_SOLUTION_EXT
class Solution {}
#endif
extension Solution {
    func kthSmallest(_ matrix: [[Int]], _ k: Int) -> Int {
        let n = matrix.count
        typealias Pair = (i: Int, j: Int, v: Int)
        var pq = PriorityQueue<Pair>([], { $0.v < $1.v })
        for j in 0..<n {
            pq.enqueue((i: 0, j: j, v: matrix[0][j]))
        }
        var cnt = 0
        var ans = 0
        while cnt < k {
            guard let last = pq.dequeue() else { break }
            if last.i < n - 1 {
                pq.enqueue((i: last.i + 1, j: last.j, v: matrix[last.i+1][last.j]))
            }
            ans = last.v
            cnt += 1
        }
        return ans
    }
}
```

已经是比较优化的一种解法了，但下面论文的给出的是一种 O(n) 的解法。

## 论文解法 

http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf

伪代码

```
function select(A, k);
    begin
        (x, y) = biselect(n, A, k, k)
        return x
    end select

function biselect(n, A, k1, k2);
    begin
        if n <= 2
        then (x, y) = (k1-th of A, k2-th of A)
        else begin
            (a, b) = biselect(n', A', k1', k2')
            ra_ = rank_(A, a)j
            rb+ = rank+(A, b)
            L = { A[i][j] | b < A[ij][j] < a}
            
            if ra_ <= k1 - 1 then x = a
            else if k1 + rb+ - n^2 <= 0 then x = b
            else x = pick(L, k1 + rb+ - n^2)

            if ra_ <= k2 - 1 then y = a
            else if k2 + rb+ - n^2 <= 0 then y = b
            else y = pick(L, k2 + rb+ - n^2)

            end
        end
        return (x, y)
    end biselect;
```

## 泛化解法

论文解法只适用于 n * n 的矩阵，而且求子矩阵比较复杂，搜索到一篇泛化成 n * m 矩阵并简化解法的文章：

> 注意：这里说矩阵元素必须是不重复的，但实际上修改算法中 `rankInMatrix` 方法即可实现对可重复问题的支持。

https://chaoxu.prof/posts/2014-04-02-selection-in-a-sorted-matrix.html

代码是用 Haskell 写的，

<details>
<summary>展开查看</summary>

{{< gist chaoxu 81ab728730e6a65524cc4262c9dd0e80 >}}
</details>

尝试用 [在线转化器](https://www.codeconvert.ai/haskell-to-c-converter) 转换成 C 语言的，发现各种狗屁不通。。

> AI 还是很难在可预见的未来代替人类程序员啊！

手动转换成 Swift：

```swift
#if !LC_SOLUTION_EXT
class Solution {}
#endif
extension Solution {
    func kthSmallest(_ matrix: [[Int]], _ k: Int) -> Int {
        let n = matrix.count
        let m = matrix[0].count
        guard k >= 1 && k <= n * m else { return -1 }

        let (result, _) = _biselect(k-1, k-1, matrix)
        return result
    }

    func _biselect(_ lb: Int, _ ub: Int, _ mat: [[Int]]) -> (Int, Int) {
        let n = mat.count
        let m = mat[0].count
        if n > m {
            return _biselect(lb, ub, mat.transposed())
        }
        var (a, b) = (mat[0][0], mat[n-1][m-1])
        if n >= 3 {
            let hm = m / 2 + 1
            let _lb = lb / 2
            let _ub = min(ub / 2 + n, n * hm - 1)
            let halfMat = mat.halfMat()
            (a, b) = _biselect(_lb, _ub, halfMat)
        }
        let ra = _rankInMatrix(mat, a: a)
        let values = _selectRange(mat, a: a, b: b)
        return (values[lb-ra], values[ub-ra])
    }

    // O(n): top-left region bound of index pairs, matrix[i][j] <= b
    func _frontier(_ mat: [[Int]], _ b: Int) -> [(Int, Int)] {
        var result: [(Int, Int)] = []
        let n = mat.count
        let m = mat[0].count
        var i = 0
        var j = m - 1
        while i <= n - 1 && j >= 0 {
            if mat[i][j] <= b {
                result.append((i, j))
                i += 1
            } else {
                j -= 1
            }
        }
        return result
    }

    // O(n): the rank of an element in the matrix
    func _rankInMatrix(_ mat: [[Int]], a: Int) -> Int {
        let n = mat.count
        let m = mat[0].count
        var i = 0
        var j = m - 1
        var rank = 0
        while i <= n - 1 && j >= 0 {
            if mat[i][j] < a {
                rank += (j + 1)
                i += 1
            } else {
                j -= 1
            }
        }
        return rank
    }

    // O(n): select all elements x in the matrix such that a <= x <= b
    func _selectRange(_ mat: [[Int]], a: Int, b: Int) -> [Int] {
        var result: [Int] = []
        for (x, y) in _frontier(mat, b) {
            for j in (0...y).reversed() {
                if mat[x][j] >= a {
                    result.append(mat[x][j])
                } else {
                    break
                }
            }
        }
        return result.sorted()
    }

}

extension Array where Element == [Int] {
    // 矩阵转置
    func transposed() -> [[Int]] {
        guard let firstRow = self.first else { return [] }
        return firstRow.indices.map { index in
            self.map { $0[index] }
        }
    }

    // Let A' be the matrix we get by removing all even index (1-indexed) columns from A,
    // and add the last column.
    func halfMat() -> [[Int]] {
        guard let firstRow = self.first else { return [] }
        let n = self.count
        let m = firstRow.count
        let hm = m / 2 + 1
        var ret = [[Int]](repeating: [Int](repeating: 0, count: hm), count: n)
        let isEven = (m % 2 == 0)
        for i in 0..<n {
            for j in 0..<hm {
                if j == hm - 1 {
                    ret[i][j] = isEven ? self[i][j * 2 - 1] : self[i][2 * j]
                } else {
                    ret[i][j] = self[i][j * 2]
                }
            }
        }
        return ret
    }
}

```

## 更优解法

上述论文解法显得非常复杂，LeetCode 上目前最好的方法是二分查找：

```swift
// MARK: Better Solution - Binary Search
extension Solution {
    func kthSmallest(_ matrix: [[Int]], _ k: Int) -> Int {
        let n = matrix.count

        func _countSmaller(_ a: Int) -> Int {
            var (i, j) = (0, n - 1)
            var count = 0
            while i < n && j >= 0 {
                if matrix[i][j] <= a {
                    count += (j + 1)
                    i += 1
                } else {
                    j -= 1
                }
            }
            return count
        }

        var (left, right) = (matrix[0][0], matrix[n-1][n-1])
        while left < right {
            let mid = left + (right - left) / 2
            let count = _countSmaller(mid)
            if count < k {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
}
```
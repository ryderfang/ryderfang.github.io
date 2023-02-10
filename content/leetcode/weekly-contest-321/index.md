---
title: "题解 Weekly Contest 321"
date: 2022-11-27T15:21:40+08:00
categories: [Contest]
tags: []
---

{{< katex >}}

第一次参加 **LeetCode Weekly Contest**，也是第一次写完整的题解，有些解法可能也不是最佳。仅供参考。

最后一道 Hard 也是结束后花了好长时间才搞定的。

> 不知道 10 分钟 AK 的大佬是怎么做到的... Orz

https://leetcode.com/contest/weekly-contest-321/

## 2485. Find the Pivot Integer

https://leetcode.com/problems/find-the-pivot-integer/

简单题，求 sum(1...x) == sum(x...n) 的 x，就是解方程：

$$
\begin{align}
  &\frac{x * (x + 1)}{2} = \frac{(n-x+1)*(x+n)}{2} \newline
  &x = sqrt(\frac{n^2 + n}{2})
\end{align}
$$

注意 `x` 是个整数即可。

```swift
class Solution {
    func pivotInteger(_ n: Int) -> Int {
        let target = (n * n + n) / 2
        let res = Int(sqrt(Double(target)))
        if res * res == target {
            return res
        } else {
            return -1
        }
    }
}
```

## 2486. Append Characters to String to Make Subsequence

https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

这里 `subsequence` 不是子串，不要求连续。那么遍历 `s` 尽可能多地找 `t` 中的字符即可。

```swift
class Solution {
    func appendCharacters(_ s: String, _ t: String) -> Int {
        let s = Array(s)
        let t = Array(t)
        var count = t.count
        var i = 0, j = 0
        while i < t.count && j < s.count {
            if t[i] == s[j] {
                i += 1
                count -= 1
            }
            j += 1
        }
        return count
    }
}
```

## 2487. Remove Nodes From Linked List

https://leetcode.com/problems/remove-nodes-from-linked-list/

链表操作，要求移除所有右侧存在比当前节点大的节点。两个注意点：

- 整个右边，并不是邻近的右侧
- 严格大于

我的解法额外增加了一个栈，便于从后向前处理。

1. 首先最后一个节点肯定会被保留，因为它没有右侧节点。
2. 令尾节点为最大的节点。
3. 向前移除所有比它小的节点。
4. 如果遇到比它大的，更新最大节点，回到 2，直到头节点。

```swift
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func removeNodes(_ head: ListNode?) -> ListNode? {
        guard let node = head else { return nil }
        var p: ListNode? = node
        var stack = [ListNode]()
        while p != nil {
            stack.append(p!)
            p = p?.next
        }
        var ans = [ListNode]()
        var maxi = stack.last!.val
        ans.append(stack.popLast()!)
        while stack.count > 0 {
            let last = stack.last!
            if last.val >= maxi {
                maxi = last.val
                ans.append(last)
            }
            stack.removeLast()
        }
        p = nil
        for x in ans {
            x.next = p
            p = x
        }
        return ans.last
    }
}
```

之前超时了一次，因为在更新数组时使用了这种写法，便于顺序处理：

`ans = [last] + ans`，改为 `ans.append(last)` 就过了。

> 数组整体的移动非常耗时！

## 2488. Count Subarrays With Median K

https://leetcode.com/problems/count-subarrays-with-median-k/

最后一题，菜鸡如我确实好久才搞定，不然也不会下午才写题解 🥲 

`Median` - 中位数，虽然对于奇偶数列都是第 `n / 2` 项，但这是因为取整的缘故。

- 偶数列，大于中位数的个数比小于中位数的个数多 1
- 奇数列，大于和小于中位数的数是一样多的

> 虽然 `subarray` 是连续的，但求中位数时，是会排序的：`after sorting`

那么我们只要找出所有区间 \\([i, j)\\) 对，使得这个区间内大于 k 的数等于小于 k 的数，或者正好多一个。

$$
\begin{align}
  &condition = \lbrace greater[j] - greater[i] - (less[j] - less[i]) == (0 | 1) \rbrace \newline
  &ans = count \lbrace condition \rbrace, i \in [0,ki], j \in (ki, n], nums[ki] == k
\end{align}
$$

需要注意的是这个区间需要包含 k，那么必然 i 在 ki  的左侧，而 j 在右侧。

为了便于计算，定义：

- `ki` 是 `k` 的位置
- `less[i]` 是 [0, i) 这个范围内小于 k 的数的个数，同时 `greater[i]` 表示大于 k 的数的个数。注意这个区间不包含 `i` 本身

由于整个数组都是非重复的，那么一个数除了 ki 这个位置之外，不是大于 k，就是小于 k。所以：

$$
\begin{align}
  &greater[i] = i - less[i], i \in [0, ki] \newline
  &greater[j] = j - 1 - less[j], j \in (ki, n]
\end{align}
$$

这样定义之后，区间 [i, j) 内 `greater` 和 `less` 的差就是：

$$
\begin{align}
  diff &= j - 1 - less[j] - (i - less[i]) - (less[j] - less[i]) \newline
       &= j - i - 1 - 2 * (less[j] - less[i])
\end{align}
$$

对于同一个 `i` 来说，`j` 每增加 1，`diff` 是如何变化的呢？我们容易得知：

\\( less[j+1] = less[j] + (nums[j] < k ? 1 : 0) \\)

- 如果 \\( less[j+1] == less[j] + 1 \\)，`diff` 会减少 1，这时 j+1 `diff = 0` 的个数其实是 j 中 `diff = 1` 的个数。 
- 如果 \\( less[j+1] == less[j] \\)，`diff` 会增加 1，同理，`diff = 0` 的个数其实是之前 `diff = -1` 的个数。

### Solution

到这里，我们发现其实并不需要计算所有的 `less`，只需要统计到 `ki` 即可。
然后计算出区间 \\( [i, ki], i \in [0, ki] \\) 内所有的 `diff` 值保存起来，向后递推，即可找到所有的解。

```swift
class Solution {
    func countSubarrays(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        guard n > 1 else { return 1 }
        var ki = 0
        // i <- [0, ki] greater[i] = i - less[i]
        // j <- (ki, n] greater[j] = j - 1 - less[j]
        // for [i, j)
        // greater[j] - greater[i] - (less[j] - less[i]) = [0, 1]
        // j - i - 1 - 2 * (less[j] - less[i])

        // less[i] is count of num < k for i ∈ [0..i)
        var less = [Int](repeating: 0, count: n+1)
        for (i, x) in nums.enumerated() {
            less[i+1] = less[i]
            if x == k {
                ki = i
                break
            } else if x < k {
                less[i+1] += 1
            }
        }
        var diff = [Int: Int]()
        // diff of [i...ki], i ∈ [0...ki]
        for i in 0...ki {
            // j = ki + 1
            let d = (ki + 1) - i - 1 - (less[ki+1] - less[i]) * 2
            diff[d, default: 0] += 1
        }
        var ans = diff[0, default: 0] + diff[1, default: 0]
        var offset = 0
        for j in ki+1..<n {
            if nums[j] > k {
                // less[j+1] == less[j]
                offset += 1
            } else {
                // less[j+1] == less[j] + 1
                offset -= 1
            }
            ans += diff[0-offset, default: 0] + diff[1-offset, default: 0]
        }
        return ans
    }
}
```

## EOF

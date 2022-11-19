---
title: "各种 Sum 相关的题"
date: 2022-11-19T16:38:40+08:00
categories: [Two-Pointers]
tags: []
---

## 1. 问题抽象

有一类跟 Son，啊不，是 `Sum` 相关的题，比如：

1. [Two Sum](https://leetcode.com/problems/two-sum/)
2. [Three Sum](https://leetcode.com/problems/3sum/)
3. [Three Sum Closest](https://leetcode.com/problems/3sum-closest/description/)
4. [Four Sum](https://leetcode.com/problems/4sum/)

差不多都是给一组数 `nums: [Int]` 和一个目标数字 `target`，然后找出 `k` 个元素和为 `target` 的组合，同时要求不重复。
这种上面几题就抽象成：

{{< katex >}}

1. `Two Sum`: \\( k = 2 \\)
2. `Three Sum`: \\( target = 0, k = 3 \\)
3. `Three Sum Closest`: \\( ans = min(sum - target), k = 3 \\)
4. `Four Sum`: \\( k = 4 \\)

## 2. Two Sum

首先 `Two Sum` 作为 LeetCode No.1 的题，可以说是非常简单，因为只要求找到一组

\\( [i, j] \\)，满足 \\( nums[i] + nums[j] == target \\) 

那么只需要遍历的时候用 map 记录下每个数字出现的位置即可。

```swift
/*
 * @lc app=leetcode id=1 lang=swift
 *
 * [1] Two Sum
 */

// @lc code=start
#if !LC_SOLUTION_EXT
class Solution {}
#endif
extension Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var mp = [Int: Int]()
        for (i, x) in nums.enumerated() {
            if let last = mp[target - x] {
                return [last, i]
            }

            if mp[x] == nil {
                mp[x] = i
            }
        }
        return []
    }
}
// @lc code=end
```

那么，如果要求所有的组合呢？就非常类似 `Three Sum` 了。

```swift
func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    return twoSumPlus(nums, target).first!
}

func twoSumPlus(_ nums: [Int], _ target: Int) -> [[Int]] {
    var sorts = [(Int, Int)]()
    let n = nums.count
    guard n >= 2 else { return [] }
    for (i, x) in nums.enumerated() {
        sorts.append((x, i))
    }
    sorts = sorts.sorted(by: { $0.0 < $1.0 })
    var l = 0, r = n - 1
    var ans = [[Int]]()
    while l < r {
        let sum = sorts[l].0 + sorts[r].0
        if sum == target {
            ans.append([sorts[l].1, sorts[r].1])
//                print(sorts[l].0, sorts[r].0)
            l += 1
            r -= 1
            while l < r && nums[l] == nums[l-1] { l += 1 }
            while l < r && nums[r] == nums[r+1] { r -= 1 }
        } else {
            sum > target ? r -= 1 : (l += 1)
        }
    }
    return ans
}
```

## 3. Three Sum

首先，都是排序，便于去重。然后，枚举一个数，用双指针的方法找另两个数。

```swift
/*
 * @lc app=leetcode id=15 lang=swift
 *
 * [15] 3Sum
 */

// @lc code=start
#if !LC_SOLUTION_EXT
class Solution {}
#endif
extension Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {
        let nums = nums.sorted()
        let n = nums.count
        guard n >= 3 else { return [] }
        var ans = [[Int]]()
        for i in 0..<n {
            // 相同数字只取第一个
            if i > 0 && nums[i] == nums[i-1] { continue }
            // target = 0
            let x = 0 - nums[i]
            var l = i + 1, r = n - 1
            // two-pointer
            while l < r {
                let sum = nums[l] + nums[r]
                if sum == x {
                    ans.append([nums[i], nums[l], nums[r]])
                    // 找到一个之后继续，可能还有其他组合
                    l += 1
                    r -= 1
                    // 去重
                    while l < r && nums[l] == nums[l-1] { l += 1 }
                    while l < r && nums[r] == nums[r+1] { r -= 1 }
                } else {
                    // 排序的好处
                    sum > x ? r -= 1 : (l += 1)
                }
            }
        }
        return ans
    }
}
// @lc code=end
```

是不是和上面的 `twoSumPlus` 非常类似！ 同理，我们可以继续求四个数的问题。

### 3.1 Closest

这个问题有一些不同：

* 只要找到一个三元组等于 target，就不需要继续找了。因为他们已经是 `Closest` 了。
* 在过大或过小时，也需要判断 diff，因为这些组合中就可能会有答案。

```swift
/*
 * @lc app=leetcode id=16 lang=swift
 *
 * [16] 3Sum Closest
 */

// @lc code=start
#if !LC_SOLUTION_EXT
class Solution {}
#endif
extension Solution {
    func threeSumClosest(_ nums: [Int], _ target: Int) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        guard n > 3 else { return nums.reduce(0, +) }
        var diff = Int.max
        var ans = Int.max
        for i in 0..<n-2 {
            if i > 0 && nums[i] == nums[i-1] { continue }
            var l = i + 1, r = n - 1
            let x = target - nums[i]
            while l < r {
                let sum = nums[l] + nums[r]
                if sum == x {
                    return target
                } else {
                    sum > x ? r -= 1 : (l += 1)
                    if abs(sum - x) < diff {
                        diff = abs(sum - x)
                        ans = sum + nums[i]
                    }
                }
            }
        }
        return ans
    }
}
// @lc code=end

```

## 4. Four Sum

```swift
/*
 * @lc app=leetcode id=18 lang=swift
 *
 * [18] 4Sum
 */

// @lc code=start
#if !LC_SOLUTION_EXT
class Solution {}
#endif
extension Solution {
    func fourSum(_ nums: [Int], _ target: Int) -> [[Int]] {
        let nums = nums.sorted()
        let n = nums.count
        guard n >= 4 else { return [] }

        var ans = [[Int]]()
        for a in 0..<n-3 {
            if a > 0 && nums[a] == nums[a-1] { continue }
            for b in a+1..<n {
                if b > a+1 && nums[b] == nums[b-1] { continue }
                let x = target - nums[a] - nums[b]
                var l = b + 1, r = n - 1
                while l < r {
                    let sum = nums[l] + nums[r]
                    if sum == x {
                        ans.append([nums[a], nums[b], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r && nums[l] == nums[l - 1] { l += 1 }
                        while l < r && nums[r] == nums[r + 1] { r -= 1 }
                    } else {
                        sum > x ? r -= 1 : (l += 1)
                    }
                }
            }
        }
        return ans
    }
}
// @lc code=end
```

需要注意的就是枚举时去重的条件：

1. `if a > 0 && nums[a] == nums[a-1] { continue }`
2. `if b > a+1 && nums[b] == nums[b-1] { continue }`

> 特别注意这里 b 可能和 a 相同！


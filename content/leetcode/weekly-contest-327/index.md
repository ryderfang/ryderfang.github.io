---
title: "题解 Weekly Contest 327"
date: 2023-02-10T22:34:44+08:00
categories: [Contest, PriorityQueue]
tags: []
---

{{< katex >}}

年前做的，一直没搞出第四道，所以也一直没写题解，最终还是参考了别人的实现。

https://leetcode.com/contest/weekly-contest-327/

## 2529. Maximum Count of Positive Integer and Negative Integer

https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

求一个排好序的数组中正数个数和负数个数中的最大值。遍历当然最简单，但时间复杂度是 `O(n)`。

```swift
class Solution {
    func maximumCount(_ nums: [Int]) -> Int {
        return max(nums.filter { $0 > 0 }.count, nums.filter { $0 < 0 }.count)
    }
}
```

那么，

> Follow up: Can you solve the problem in `O(log(n))` time complexity?

当然，用二分查找的思路：

```swift
func maximumCount(_ nums: [Int]) -> Int {
    let n = nums.count
    var pos = 0, neg = 0
    var (l, r) = (0, n - 1)
    while l <= r {
        let m = l + (r - l) / 2
        let x = nums[m]
        if x <= 0 {
            l = m + 1
        } else {
            r = m - 1
        }
    }
    pos = n - 1 - r

    (l, r) = (0, n - 1)
    while l <= r {
        let m = l + (r - l) / 2
        let x = nums[m]
        if x >= 0 {
            r = m - 1
        } else {
            l = m + 1
        }
    }
    neg = l
    print(pos, neg)
    return max(pos, neg)
}
```

奇怪的是，提交之后发现竟然不比遍历快？！🌝

下面几题都是优先队列的使用，直接不解释地给出模板：

> PriorityQueue
```swift
fileprivate struct PriorityQueue<Element> {
    private let hasHigherPriority: (Element, Element) -> Bool
    private let isEqual: (Element, Element) -> Bool

    private var elements = [Element]()

    init(_ array: [Element], _ sort: @escaping (Element, Element) -> Bool) where Element: Equatable {
        self.init(array, sort, { $0 == $1 })
    }

    init(_ array: [Element], _ hasHigherPriority: @escaping (Element, Element) -> Bool, _ isEqual: @escaping (Element, Element) -> Bool) {
        self.hasHigherPriority = hasHigherPriority
        self.isEqual = isEqual
        for x in array {
            self.enqueue(x)
        }
    }

    mutating func enqueue(_ element: Element) {
        elements.append(element)
        bubbleToHigherPriority(elements.count - 1)
    }

    func peek() -> Element? {
        elements.first
    }

    var isEmpty: Bool {
        elements.count == 0
    }

    @discardableResult
    mutating func dequeue() -> Element? {
        guard let front = peek() else { return nil }
        removeAt(0)
        return front
    }

    mutating func remove(_ element: Element) {
        for i in 0 ..< elements.count {
            if self.isEqual(elements[i], element) {
                removeAt(i)
                return
            }
        }
    }

    private mutating func removeAt(_ index: Int) {
        let removingLast = index == elements.count - 1
        if !removingLast {
            elements.swapAt(index, elements.count - 1)
        }

        _ = elements.popLast()

        if !removingLast {
            bubbleToHigherPriority(index)
            bubbleToLowerPriority(index)
        }
    }

    private mutating func bubbleToHigherPriority(_ initialUnbalancedIndex: Int) {
        precondition(initialUnbalancedIndex >= 0)
        precondition(initialUnbalancedIndex < elements.count)

        var unbalancedIndex = initialUnbalancedIndex

        while unbalancedIndex > 0 {
            let parentIndex = (unbalancedIndex - 1) / 2
            guard self.hasHigherPriority(elements[unbalancedIndex], elements[parentIndex]) else { break }
            elements.swapAt(unbalancedIndex, parentIndex)
            unbalancedIndex = parentIndex
        }
    }

    private mutating func bubbleToLowerPriority(_ initialUnbalancedIndex: Int) {
        precondition(initialUnbalancedIndex >= 0)
        precondition(initialUnbalancedIndex < elements.count)

        var unbalancedIndex = initialUnbalancedIndex
        while true {
            let leftChildIndex = unbalancedIndex * 2 + 1
            let rightChildIndex = unbalancedIndex * 2 + 2

            var highestPriorityIndex = unbalancedIndex

            if leftChildIndex < elements.count && self.hasHigherPriority(elements[leftChildIndex], elements[highestPriorityIndex]) {
                highestPriorityIndex = leftChildIndex
            }

            if rightChildIndex < elements.count && self.hasHigherPriority(elements[rightChildIndex], elements[highestPriorityIndex]) {
                highestPriorityIndex = rightChildIndex
            }

            guard highestPriorityIndex != unbalancedIndex else { break }
            elements.swapAt(highestPriorityIndex, unbalancedIndex)

            unbalancedIndex = highestPriorityIndex
        }
    }
}
```

## 2530. Maximal Score After Applying K Operations

https://leetcode.com/problems/maximal-score-after-applying-k-operations/

简单题：

```swift
class Solution {
    func maxKelements(_ nums: [Int], _ k: Int) -> Int {
        var pq = PriorityQueue<Int>(nums, >)
        var ans = 0
        for _ in 0..<k {
            if let first = pq.dequeue() {
                ans += first
                pq.enqueue(Int(ceil(Double(first) / 3)))
            }
        }
        return ans
    }
}
```

## 2531. Make Number of Distinct Characters Equal

https://leetcode.com/problems/make-number-of-distinct-characters-equal/

给定两个字符串，判断能否交换字符一次使得它们不同字符的个数相同。

暴力枚举吧！

```swift
class Solution {
    func isItPossible(_ word1: String, _ word2: String) -> Bool {
        var mp1 = [Character: Int]()
        for ch in word1 {
            mp1[ch, default: 0] += 1
        }
        var mp2 = [Character: Int]()
        for ch in word2 {
            mp2[ch, default: 0] += 1
        }
        let n1 = mp1.count
        let n2 = mp2.count
        for (k1, v1) in mp1 {
            for (k2, v2) in mp2 {
                var (t1, t2) = (n1, n2)
                if k1 == k2 {
                    if n1 == n2 { return true }
                    continue
                }
                if v1 == 1 {
                    t1 -= 1
                }
                if mp1[k2] == nil {
                    t1 += 1
                }
                if v2 == 1 {
                    t2 -= 1
                }
                if mp2[k1] == nil {
                    t2 += 1
                }
                guard t1 != t2 else { return true }
            }
        }
        return false
    }
}
```

## 2532. Time to Cross a Bridge

https://leetcode.com/problems/time-to-cross-a-bridge/

这题挺有意思的，类似于会议室时间安排类的问题，也用到了优先队列。

首先，过河有两个位置：

* 左边：工人空手向右过河去取商品

* 右边：带好商品后返程，向左过河

每次只能选一个工人过河，选取的标准是选效率最低的，也就是 \\( leftToRight + rightToLeft \\) 最多的，如果相等取充数最大的。

还有一些限制条件：

* 每次桥上只能有一个工人

* 右边的工人优先过河

* 如果右边还有待取的商品，左边等待的工人才需要过河

最终需要得到最后一个工人到达左边的时刻。

思路：

- 用两个优先队列，存储左右两边等待过河的工人。

- 过河的工人，提前计划他们回到桥边的时间，也用优先队列存储，如果在 A 工人过河之后，B 工人已经完成取货/放货，那么 B 就可以回到桥边。

- 没有工人过河时，时间快进到取货/放货工人到达桥边的时间。


{{< highlight swift "linenos=table,hl_lines=16 49 56 73 76" >}}
func findCrossingTime(_ n: Int, _ k: Int, _ time: [[Int]]) -> Int {
    struct Worker: Equatable {
        var leftToRight: Int
        var pickOld: Int
        var rightToLeft: Int
        var putNew: Int
        var index: Int
        var priority: Int
        init(_ l2r: Int, _ po: Int, _ r2l: Int, _ pn: Int, _ i: Int) {
            leftToRight = l2r
            pickOld = po
            rightToLeft = r2l
            putNew = pn
            index = i
            // since index <= 10000
            priority = (leftToRight + rightToLeft) * 10000 + index
        }
        static func == (lhs: Self, rhs: Self) -> Bool {
            return lhs.index == rhs.index
        }
    }
    struct Event: Equatable {
        var time: Int
        var worker: Worker
        init(_ time: Int, _ worker: Worker) {
            self.time = time
            self.worker = worker
        }
        static func == (lhs: Self, rhs: Self) -> Bool {
            return lhs.time == lhs.time
        }
    }
    var workers = [Worker]()
    for i in 0..<k {
        workers.append(Worker(time[i][0], time[i][1], time[i][2], time[i][3], i))
    }
    // wait on left
    var leftBridge = PriorityQueue<Worker>(workers, { $0.priority > $1.priority })
    // wait on right
    var rightBridge = PriorityQueue<Worker>([], { $0.priority > $1.priority })
    // put new, arrive left on future
    var pickNew = PriorityQueue<Event>([], { $0.time < $1.time })
    // pick old, arrive right on future
    var pickOld = PriorityQueue<Event>([], { $0.time < $1.time })
    var goods = n
    var now = 0
    while goods > 0 || !rightBridge.isEmpty || !pickOld.isEmpty {
        while !pickNew.isEmpty {
            guard let top = pickNew.peek(), top.time <= now else {
                break
            }
            pickNew.dequeue()
            leftBridge.enqueue(top.worker)
        }
        while !pickOld.isEmpty {
            guard let top = pickOld.peek(), top.time <= now else {
                break
            }
            pickOld.dequeue()
            rightBridge.enqueue(top.worker)
        }
        if let pr = rightBridge.dequeue() {
            now += pr.rightToLeft
            pickNew.enqueue(Event(now + pr.putNew, pr))
        } else if let pl = leftBridge.dequeue(), goods > 0 {
            goods -= 1
            now += pl.leftToRight
            pickOld.enqueue(Event(now + pl.pickOld, pl))
        } else {
            now = Int.max
            // forward to future
            if !pickNew.isEmpty {
                now = min(now, pickNew.peek()?.time ?? Int.max)
            }
            if !pickOld.isEmpty {
                now = min(now, pickOld.peek()?.time ?? Int.max)
            }
        }
    }

    return now
}
{{< /highlight >}}

## EOF

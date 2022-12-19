---
title: "很难写⌜正确⌟的二分查找"
date: 2022-03-08T17:52:24+08:00
categories: [Binary-Search]
tags: [search]
---

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-07-search.jpg)

“二分”查找是一种非常常用的算法。最坏的情况下时间复杂度也是 `O(log n)`，空间复杂度 `O(1)`，相比线性搜索优秀太多。

但是要“写对”，并不容易，1988 年一项调查发现，二十本专业书籍中仅有五本[^1]能准确写对“二分”查找。

<!--more-->

> 尽管二分查找的基本思想相对简单，但细节可以令人难以招架 ... — 高德纳

二分查找的前提是待查找的序列是有序的。

本身算法逻辑非常简单[^2]：

```r
function binary_search(A, n, T) is
    L := 0
    R := n − 1
    while L ≤ R do
        m := floor((L + R) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m − 1
        else:
            return m
    return unsuccessful
```

## 减少一次判断

上述伪代码每次循环都会比较 mid 与 target 是否相等，如果去掉这个比较，将之放到循环退出时，就可以在每次循环中减少一次比较，总得循环次数仅比上面的算法多一次。

```r
function binary_search_alternative(A, n, T) is
    L := 0
    R := n − 1
    while L != R do
        m := ceil((L + R) / 2)
        if A[m] > T then
            R := m − 1
        else:
            L := m
    if A[L] = T then
        return L
    return unsuccessful
```

## 关于 cell 和 floor

可以看出来，上面两个实现中在取 mid 时使用了不同的方法，一个是 `floor()`，一个是 `ceil()`，

`floor((0 + 1) / 2) = 0`

`ceil((0 + 1) / 2) = 1`

为什么会有这个不同呢？在 [StackOverflow](https://stackoverflow.com/questions/27655955/why-does-binary-search-algorithm-use-floor-and-not-ceiling-not-in-an-half-open) 上有很好的解释：

* 如果更新二元组 (l, r) -> (m + 1, m - 1) 时，这两种方法都可以，结果是一样的。
* 如果是 (l, r) -> (m, m - 1) 时，必须要使用 `ceil`，否则循环无法退出。比如 l = 0, r = 1, A = [1, 2]， target = 2 时，floor 会导致 l 一直被更新为 0，无法退出。
* 如果是 (l, r) -> (m + 1, m) 时，必须要使用 `floor`，否则同时循环无法退出。比如 l = 0, r = 1, A = [1, 2]，target = 1 时，ceil 会导致 r 一直被更新成 1。

> 总之，就是更新下边界更多时，使用 floor，更新上边界更多时，使用 ceil。

## 关于溢出

上述算法中还有一个问题，计算 `mid = floor((L + R) / 2)` 存在可能的溢出错误，这在 `C++` 中比较常见，比如 `l = r = 2^31-1`，相加就会溢出整数范围！

正常的写法是：

```python
mid = l + (r - l) // 2
```

## 如果有重复元素

如果序列中存在重复元素，比如 `[1, 2, 3, 3, 3, 4, 5]`，要查找 `T = 3`，可能会有多个结果。

如果只是判断 target 是否存在，上述的算法都没有问题。但是如果想找到 index 最小或最大的 target 位置，算法就需要做一些修改。

参考 C++ 标准库中的 `std::binary_search` 的实现[^3]：

```cpp
template <class ForwardIterator, class T>
  bool binary_search (ForwardIterator first, ForwardIterator last, const T& val)
{
  first = std::lower_bound(first,last,val);
  return (first!=last && !(val<*first));
}
```

调用了 `std::lower_bound()` 方法，这个方法就是在一个序列中找值为 val 的最小 index 位置，同理还有一个找最大 index 方法的函数 `std::upper_bound()`

```cpp
template <class ForwardIterator, class T>
  ForwardIterator lower_bound (ForwardIterator first, ForwardIterator last, const T& val)
{
  ForwardIterator it;
  iterator_traits<ForwardIterator>::difference_type count, step;
  count = distance(first,last);
  while (count>0)
  {
    it = first; step=count/2; advance (it,step);
    if (*it<val) {                 // or: if (comp(*it,val)), for version (2)
      first=++it;
      count-=step+1;
    }
    else count=step;
  }
  return first;
}
```

```cpp
template <class ForwardIterator, class T>
  ForwardIterator upper_bound (ForwardIterator first, ForwardIterator last, const T& val)
{
  ForwardIterator it;
  iterator_traits<ForwardIterator>::difference_type count, step;
  count = std::distance(first,last);
  while (count>0)
  {
    it = first; step=count/2; std::advance (it,step);
    if (!(val<*it))                 // or: if (!comp(val,*it)), for version (2)
      { first=++it; count-=step+1;  }
    else count=step;
  }
  return first;
}
```

区别就是在更新 `left = mid + 1` 时，如果想取左边界，条件是 `mid < val`；如果想取右边界，条件是 `mid <= val`。

## 处处是坑

知乎有[一篇专栏文章：<聊聊一看就会一写就跪的二分查找>](https://zhuanlan.zhihu.com/p/343138037)讲了二分中的各个坑点，我们逐一看一下：

```go
func FirstGreaterOrEqual(array []int, target int) int {
    // 初始化区间左端点： -1  ||  0  ||  1  ？
    l := 0
    // 初始化区间右端点： len(array) - 1  ||  len(array)  ||  len(array) + 1  ?
    r := len(array)
    // 当区间不为空时循环： l + 1 < r  ||  l < r  ||  l <= r  ||  l <= r + 1  ?
    for l < r {
        // 计算区间中点： l + (r - l) / 2  ||  l + (r - l + 1) / 2  ?
        m := l + (r - l) / 2
        // 将中点对应的元素同target比较： >  ||  >=  ||  <  || <=  ?
        if array[m] < target {
            // 继续查找右侧这一半： m - 1  ||  m  ||  m + 1  ?
            l = m + 1
        } else {
            // 继续查找左侧这一半： m - 1  ||  m  ||  m + 1  ?
            r = m
        }
    }
    // 这里应该是 l - 1  ||  l  ||  l + 1  ?
    // 这里应该是 r - 1  ||  r  ||  r + 1  ?
    return l
}
```

这是一段 go 语言代码，不过不影响理解它的逻辑，其实它就是在 array 中找 target 的左边界。

来一一解释作者提出的这些坑：

1. 区间左端点 `l = 0` 或者其他？

2. 区间右端点 `r = len(array)` 还是 `len(array) - 1`？

这两个是一个问题，整个区间有四种状态 `(l, r)` `[l, r]` `(l, r]` `[l, r]`

对于数组从 0 开始的语言，左闭区间是合适的。

右开右闭都是可行的，只需要在循环判断时做一下调整

* [l, r] -> l < r + 1
* [l, r) -> l < r

一般来说，我们都会选择 `l = 0 & [l, r)` 这种组合。

3. 循环结束条件是 `<` 还是 `<=` 还是 `!=`

`<` 和 `!=` 都可以，对于非递减序列来说，一般用 `<`。

如果 `l = r` 时，仍然进入循环，同时如果 `array[l] >= target`，会导致循环无法退出。
 
4. 区间中间计算

`l + (r - l + 1) / 2` 这就属于是 `ceil` 操作。这个在前面也解释过，不再赘述。

5. 判断条件

同样的，取决于问题是取最左边的位置还是最右边的，上一节也解释过。

6. 返回值

结束条件是 `l == r`，所以返回 `l` 没有问题。但是这个位置并不一定能满足 `array[l] == target`，甚至于可能越界。

返回值 `l` 表示：`[0, l)` 位置都是小于 `target` 的，而 `[l, len)` 则是大于等于 `target` 的。这里 `l` 可能等于 `len` (越界)。

> 所以在使用二分查找，来判断 target 是否存在时，要注意判断是否越界。

作者最后给了一种通用解决方案，将判断逻辑变成一个闭包方法作为参数传入，这样就可以得出多个二分变种问题的解法。

## 总之，记模板

[704. Binary Search](https://leetcode.com/problems/binary-search/description/)

可见，想写对二分不容易，那么我们只记一种正确的写法，归纳成模板即可

```python
# template
def _bsearch(a: List[int], x: int, l: int = 0, r: int = None) -> int:
    r = r or len(a)
    while l < r:
        m = l + (r - l) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    return l
```

```swift
#if !LC_SOLUTION_EXT
class Solution {}
#endif
extension Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var l = 0, r = nums.count - 1
        while l <= r {
            let mid = l + (r - l) / 2
            if nums[mid] == target {
                return mid
            }
            if nums[mid] < target {
                l = mid + 1
            } else {
                r = mid - 1
            }
        }
        return -1
    }
}
```

[^1]: [Wikipedia](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E6%90%9C%E5%B0%8B%E6%BC%94%E7%AE%97%E6%B3%95#%E5%AE%9E%E7%8E%B0%E4%B8%AD%E7%9A%84%E9%97%AE%E9%A2%98)
[^2]: https://en.wikipedia.org/wiki/Binary_search_algorithm
[^3]: http://www.cplusplus.com/reference/algorithm/binary_search/
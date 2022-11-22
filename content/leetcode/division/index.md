---
title: "除法器"
date: 2022-11-22T19:07:47+08:00
categories: [Division, Binary]
tags: []
---

{{< katex >}}

最近重新刷这道题：[29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

不使用乘法、除法和取模运算，实现两个整数的除法。

需求注意的是，输入是 32 位整数，范围 [\\(-2^{31}\\), \\(2^{31}-1\\)]，相除可能溢出。

（其中只有一种情况：也就是 \\(\frac{-2^{31}}{-1} = 2^{31}\\)）

容易让人想起大学时学的模拟电路、MIPS 除法器、ALU 之类的名词。

## 朴素实现

```swift
func divide(_ dividend: Int, _ divisor: Int) -> Int {
    guard dividend != 0 else { return 0 }
    // 2^31 - 1
    let intMax = Int(Int32.max)
    // -2^31
    let intMin = Int(Int32.min)
    // -2^31/-1 is the only chance to overflow
    if dividend == intMin && divisor == -1 {
        return intMax
    }
    var a = abs(dividend)
    let b = abs(divisor)
    var quotient = 0
    // convert dividend to binary, high to low
    var abits = [Int]()
    while a != 0 {
        abits = [a & 1] + abits
        a >>= 1
    }
    var remainder = 0
    for bit in abits {
        let cur = (remainder << 1) + bit
        quotient <<= 1
        if cur < b {
            remainder = cur
        } else {
            quotient += 1
            remainder = cur - b
        }
    }

    print(remainder)
    if (dividend > 0) != (divisor > 0) {
        quotient = -quotient
    }
    return quotient
}
```

核心逻辑就是在模拟竖式除法：

```swift
var remainder = 0
for bit in abits {
    let cur = (remainder << 1) + bit
    quotient <<= 1
    if cur < b {
        remainder = cur
    } else {
        quotient += 1
        remainder = cur - b
    }
}
```

### 计算过程

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-11-22-2BNHuJ.png)

1. 首先将被除数转换成二进制，这样可以使用位移操作代替乘法。
2. 首先取最高位作为`当前被除数`
3. 将`当前被除数`与`除数`比较
    * 大于或等于除数，那么这一位的商就是 `1`，这时将当前被除数减去除数得到余数
    * 反之，商这一位记 `0`，这种情况，被除数就是余数
    * 商的计算也是左移的过程
4. 余数左移，同时从被除数中再拿一位下来，计算新的当前被除数，重复过程 3-4
5. 直到所有位数处理完成

## 花活实现

```swift
var remainder = abs(dividend)
let down = abs(divisor)
var quotient = 0
for x in stride(from: 31, through: 0, by: -1) {
    if remainder >= (down << x) {
        quotient += (1 << x)
        remainder -= (down << x)
    }
}
if (dividend > 0) != (divisor > 0) {
    quotient = -quotient
}
```

对于 32 位整数，可以枚举商的每一位结果。用以下公式可以更容易理解整个计算过程：

$$
  diviend = divisor * quotient = divisor * (q_{31} * 2^{31} + q_{30} * 2^{30} + ... + q_0) \newline
          = (divisor \<< 31) * q_{31} + (divisor \<< 30) * q_{30} + ... + divisor * q_0
$$
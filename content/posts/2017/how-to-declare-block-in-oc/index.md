---
title: 在 ObjC 中如何定义 Block
date: 2017-05-31T19:34:55+08:00
categories: [ObjC, Block]
tags: [block]
---

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-04-07-featured-image.jpg)

来自一个神奇的域名: [http://fuckingblocksyntax.com/](http://fuckingblocksyntax.com/)

## 使用方法

### 局部变量

```objc
returnType (^blockName)(parameterTypes) = ^returnType(parameters) {...};
```

例如：
```objc
double (^multiply)(double, double) = ^double(double a, double b) {
    return a * b;
};

// 其中返回值可以省略
double (^multiply)(double, double) = ^(double a, double b) {
    return a * b;
};

// 如果参数为空，可以继续省略
void (^voidBlock)(void) = ^{
    
};
```

### 属性 property

```objc
@property (nonatomic, copy, nullability) returnType (^blockName)(parameterTypes);
```

例如：
```objc
@property (nonatomic, copy) double (^multiply)(double, double);
@property (nonatomic, copy) void (^voidBlock)(void);
```

### 方法参数

```objc
- (void)someMethodThatTakesABlock:(returnType (^nullability)(parameterTypes))blockName;
```

例如：
```objc
- (void)someMethodCallBlock:(double (^_Nonnull)(double, double))multiply {
    
}
```

这里 `_Nonnull` 修饰的是 block 本身，也就是传一个 nil 的 block，会有 warning

> Null passed to a callee that requires a non-null argument

### 参数调用

```objc
[someObject someMethodThatTakesABlock:^returnType (parameters) {...}];
```

例如：
```objc
[self someMethodCallBlock:^(double a, double b) {
    return a * b;
}];
```

这里的返回值也可以忽略。

### typedef 定义

```objc
typedef returnType (^TypeName)(parameterTypes);
TypeName blockName = ^returnType(parameters) {...};
```

例如：
```objc
typedef double (^Multiplier)(double, double);

@property (nonatomic, copy) Multiplier multiply;
```

## Hint
- [block 在 ARC 下是否声明为 copy 属性](https://stackoverflow.com/questions/23334863/should-i-still-copy-block-copy-the-blocks-under-arc)

*It is still a good idea to declare block properties as having copy semantics since a block assigned to a strong property will in fact be copied.*

Apple recommends this as well:
> You should specify copy as the property attribute, because a block needs to be copied to keep track of its captured state outside of the original scope. This isn’t something you need to worry about when using Automatic Reference Counting, as it will happen automatically, but it’s best practice for the property attribute to show the resultant behavior.

---
title: 在 ObjC 中如何定义 Block
date: 2017-05-31T19:34:55+08:00
categories: [ObjC]
tags: [Block]
---

来自一个神奇的域名

<!--more-->

{{< admonition note >}}

[http://fuckingblocksyntax.com/](http://fuckingblocksyntax.com/)

{{< /admonition >}}

## Declaration

### local variable

``` objectivec
returnType (^blockName)(parameterTypes) = ^returnType(parameters) {...};
```

### property

``` objectivec
@property (nonatomic, copy, nullability) returnType (^blockName)(parameterTypes);
```

### method parameter

``` objectivec
- (void)someMethodThatTakesABlock:(returnType (^nullability)(parameterTypes))blockName;
```

### argument to a method call

``` objectivec
[someObject someMethodThatTakesABlock:^returnType (parameters) {...}];
```

### typedef

``` objectivec
typedef returnType (^TypeName)(parameterTypes);
TypeName blockName = ^returnType(parameters) {...};
```

## Hint
- [block 在 ARC 下是否声明为 copy 属性](https://stackoverflow.com/questions/23334863/should-i-still-copy-block-copy-the-blocks-under-arc)

*It is still a good idea to declare block properties as having copy semantics since a block assigned to a strong property will in fact be copied.*

Apple recommends this as well:
> You should specify copy as the property attribute, because a block needs to be copied to keep track of its captured state outside of the original scope. This isn’t something you need to worry about when using Automatic Reference Counting, as it will happen automatically, but it’s best practice for the property attribute to show the resultant behavior.

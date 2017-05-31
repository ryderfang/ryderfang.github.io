---
layout: post
title: 在OC中如何定义Block
description: Objective-C、 Block
category: coding
---

## Declaration

- As a `local variable`:

```objc
returnType (^blockName)(parameterTypes) = ^returnType(parameters) {...};
```

- As a `property`:

```objc
@property (nonatomic, copy, nullability) returnType (^blockName)(parameterTypes);
```

- As a `method parameter`:

```objc
- (void)someMethodThatTakesABlock:(returnType (^nullability)(parameterTypes))blockName;
```

- As an `argument to a method call`:

```objc
[someObject someMethodThatTakesABlock:^returnType (parameters) {...}];
```

- As a `typedef`:

```objc
typedef returnType (^TypeName)(parameterTypes);
TypeName blockName = ^returnType(parameters) {...};
```

## Hint
- [block在ARC下是否声明为copy属性](https://stackoverflow.com/questions/23334863/should-i-still-copy-block-copy-the-blocks-under-arc)

*It is still a good idea to declare block properties as having copy semantics since a block assigned to a strong property will in fact be copied.*

Apple recommends this as well:
> You should specify copy as the property attribute, because a block needs to be copied to keep track of its captured state outside of the original scope. This isn’t something you need to worry about when using Automatic Reference Counting, as it will happen automatically, but it’s best practice for the property attribute to show the resultant behavior.
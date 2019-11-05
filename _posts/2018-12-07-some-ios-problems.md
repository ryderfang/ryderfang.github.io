---
layout: post
title: 搜集一些 iOS 面试问题 | iOS Problems
categories: [iOS, Interview]
---

## Section 1
![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-11-30/13483958.jpg)

> 前两题，了解一定的 block 内存结构知识就可以解决。

```objc
struct __block_impl_t {
    void *isa;
    int Flags;
    int Reserved;
    void *FunPtr;
};

struct __my_block_impl_x {
    struct __block_impl_t impl;
    void *Desc;
    void *tempImpl;
};

static void __my_block_func_0() {
    printf("Hello world\n");
}

static void __my_block_func_1(struct __my_block_impl_x *__cself, int a, NSString *b) {
    NSLog(@"%d %@", a, b);
    ((void (*)(void))(__cself->tempImpl))();
}

void HookBlockToPrintHelloWorld(id block) {
    struct __my_block_impl_x *t = (__bridge struct __my_block_impl_x *)block;
    t->impl.FunPtr = (void *)__my_block_func_0;
}

void HookBlockToPrintArguments(id block) {
    struct __my_block_impl_x *t = (__bridge struct __my_block_impl_x *)block;
    t->tempImpl = t->impl.FunPtr;
    t->impl.FunPtr = (void *)__my_block_func_1;
}

void HookEveryBlockToPrintArguments(void) {

}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        void (^blk1)(void) = ^{
            NSLog(@"Block1 invoke!");
        };
        HookBlockToPrintHelloWorld(blk1);
        blk1();

        void (^blk2)(int a, NSString *b) = ^(int a, NSString *b){
            NSLog(@"Block2 invoke!");
        };
        HookBlockToPrintArguments(blk2);
        blk2(123, @"aaa");
    }
    return 0;
}
```

> 第三题需要利用 fishhook 这个库，同时如果需要针对所有类型的 block 都打印参数，还需要 NSInvocation 的辅助。

完整的实现放在 GitHub 上:
[⚔️Hook Block!](https://github.com/FongRay/Snippets/blob/master/Snippets-Mac/block/main-block.mm)

## Section 2
![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-11-30/64657547.jpg)

## Section 3
![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-11-30/71527803.jpg)

* NSObject 与 `<NSObject>`

1. 一个是类（基类），一个是协议（根协议）
2. NSObject 也是符合 `<NSObject>` 协议的

```objc
@interface NSObject <NSObject> {
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wobjc-interface-ivars"
    Class isa  OBJC_ISA_AVAILABILITY;
#pragma clang diagnostic pop
}

+ (void)load;

+ (void)initialize;
- (instancetype)init
#if NS_ENFORCE_NSOBJECT_DESIGNATED_INITIALIZER
    NS_DESIGNATED_INITIALIZER
#endif
    ;

+ (instancetype)new OBJC_SWIFT_UNAVAILABLE("use object initializers instead");
+ (instancetype)allocWithZone:(struct _NSZone *)zone OBJC_SWIFT_UNAVAILABLE("use object initializers instead");
+ (instancetype)alloc OBJC_SWIFT_UNAVAILABLE("use object initializers instead");
- (void)dealloc OBJC_SWIFT_UNAVAILABLE("use 'deinit' to define a de-initializer");

- (void)finalize OBJC_DEPRECATED("Objective-C garbage collection is no longer supported");

- (id)copy;
- (id)mutableCopy;

+ (id)copyWithZone:(struct _NSZone *)zone OBJC_ARC_UNAVAILABLE;
+ (id)mutableCopyWithZone:(struct _NSZone *)zone OBJC_ARC_UNAVAILABLE;

+ (BOOL)instancesRespondToSelector:(SEL)aSelector;
+ (BOOL)conformsToProtocol:(Protocol *)protocol;
- (IMP)methodForSelector:(SEL)aSelector;
+ (IMP)instanceMethodForSelector:(SEL)aSelector;
- (void)doesNotRecognizeSelector:(SEL)aSelector;

- (id)forwardingTargetForSelector:(SEL)aSelector OBJC_AVAILABLE(10.5, 2.0, 9.0, 1.0, 2.0);
- (void)forwardInvocation:(NSInvocation *)anInvocation OBJC_SWIFT_UNAVAILABLE("");
- (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector OBJC_SWIFT_UNAVAILABLE("");

+ (NSMethodSignature *)instanceMethodSignatureForSelector:(SEL)aSelector OBJC_SWIFT_UNAVAILABLE("");

- (BOOL)allowsWeakReference UNAVAILABLE_ATTRIBUTE;
- (BOOL)retainWeakReference UNAVAILABLE_ATTRIBUTE;

+ (BOOL)isSubclassOfClass:(Class)aClass;

+ (BOOL)resolveClassMethod:(SEL)sel OBJC_AVAILABLE(10.5, 2.0, 9.0, 1.0, 2.0);
+ (BOOL)resolveInstanceMethod:(SEL)sel OBJC_AVAILABLE(10.5, 2.0, 9.0, 1.0, 2.0);

+ (NSUInteger)hash;
+ (Class)superclass;
+ (Class)class OBJC_SWIFT_UNAVAILABLE("use 'aClass.self' instead");
+ (NSString *)description;
+ (NSString *)debugDescription;

@end
```

```
@protocol NSObject

- (BOOL)isEqual:(id)object;
@property (readonly) NSUInteger hash;

@property (readonly) Class superclass;
- (Class)class OBJC_SWIFT_UNAVAILABLE("use 'type(of: anObject)' instead");
- (instancetype)self;

- (id)performSelector:(SEL)aSelector;
- (id)performSelector:(SEL)aSelector withObject:(id)object;
- (id)performSelector:(SEL)aSelector withObject:(id)object1 withObject:(id)object2;

- (BOOL)isProxy;

- (BOOL)isKindOfClass:(Class)aClass;
- (BOOL)isMemberOfClass:(Class)aClass;
- (BOOL)conformsToProtocol:(Protocol *)aProtocol;

- (BOOL)respondsToSelector:(SEL)aSelector;

- (instancetype)retain OBJC_ARC_UNAVAILABLE;
- (oneway void)release OBJC_ARC_UNAVAILABLE;
- (instancetype)autorelease OBJC_ARC_UNAVAILABLE;
- (NSUInteger)retainCount OBJC_ARC_UNAVAILABLE;

- (struct _NSZone *)zone OBJC_ARC_UNAVAILABLE;

@property (readonly, copy) NSString *description;
@optional
@property (readonly, copy) NSString *debugDescription;

@end
```

## Section 4
![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-11-30/97038988.jpg)

---
layout: post
title: 几个 iOS 面试问题 | iOS Interview
categories: [iOS, Interview]
---

## Section 1
![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-11-30/13483958.jpg)

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

## Section 2
![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-11-30/64657547.jpg)

## Section 3
![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-11-30/71527803.jpg)

## Section 4
![](https://fangr-cc-image.oss-cn-beijing.aliyuncs.com/18-11-30/97038988.jpg)

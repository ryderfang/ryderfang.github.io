# 获取 OC Class 对象


获取 `Class` 对象的方法有很多，本文主要是收集整理它们的区别以及探究具体的实现。

<!--more-->

## class 方法

有两种 class 方法，一个是实例方法，一个是类方法：

@interface NSObject <NSObject>

`- (Class)class OBJC_SWIFT_UNAVAILABLE("use 'type(of: anObject)' instead");`

`+ (Class)class OBJC_SWIFT_UNAVAILABLE("use 'aClass.self' instead");`

@end

查看 runtime 的源码：[NSObject.mm](https://opensource.apple.com/source/objc4/objc4-750/runtime/NSObject.mm.auto.html)

可以看到它们的实现：

```
+ (id)self {
    return (id)self;
}

- (id)self {
    return self;
}

+ (Class)class {
    return self;
}

- (Class)class {
    return object_getClass(self);
}
```

所以，说给类对象发 `class` 消息，得到的是类本身 `self`，也就是 

> [NSObject class] == [NSObject self]

给实例对象发 `class` 消息，相当于调用了 `object_getClass`

## object_getClass

那么这个方法的实现是怎么样的呢？

同样查看 runtime 源码：[objc-class.mm](https://opensource.apple.com/source/objc4/objc4-750/runtime/objc-class.mm.auto.html)

`Class _Nullable object_getClass(id _Nullable obj)`

```
Class object_getClass(id obj)
{
    if (obj) return obj->getIsa();
    else return Nil;
}
```

调用了 类的 `getIsa()` 方法

// [objc-object.h](https://opensource.apple.com/source/objc4/objc4-750/runtime/objc-object.h.auto.html)
```
inline Class 
objc_object::getIsa() 
{
    if (!isTaggedPointer()) return ISA();

    uintptr_t ptr = (uintptr_t)this;
    if (isExtTaggedPointer()) {
        uintptr_t slot = 
            (ptr >> _OBJC_TAG_EXT_SLOT_SHIFT) & _OBJC_TAG_EXT_SLOT_MASK;
        return objc_tag_ext_classes[slot];
    } else {
        uintptr_t slot = 
            (ptr >> _OBJC_TAG_SLOT_SHIFT) & _OBJC_TAG_SLOT_MASK;
        return objc_tag_classes[slot];
    }
}
```

## objc_getClass

这个方法和上面的 `object_getClass` 长得很像，但还是有一些区别：

* 参数不一样，一个是 `id`，一个是 `const char *`，也就是一个传入是个类对象，一个是类名

* 实现不一样，一个调用的是 `obj->getIsa()`，一个调用的是 `loop_up_class()`

// [objc-runtime.mm](https://opensource.apple.com/source/objc4/objc4-750/runtime/objc-runtime.mm.auto.html)
```
Class objc_getClass(const char *aClassName)
{
    if (!aClassName) return Nil;

    // NO unconnected, YES class handler
    return look_up_class(aClassName, NO, YES);
}
```

调用了 `look_up_class`:

// [objc-runtime-new.mm](https://opensource.apple.com/source/objc4/objc4-787.1/runtime/objc-runtime-new.mm.auto.html)
```
Class 
look_up_class(const char *name, 
              bool includeUnconnected __attribute__((unused)), 
              bool includeClassHandler __attribute__((unused)))
{
    if (!name) return nil;

    Class result;
    bool unrealized;
    {
        runtimeLock.lock();
        result = getClassExceptSomeSwift(name);
        unrealized = result  &&  !result->isRealized();
        if (unrealized) {
            result = realizeClassMaybeSwiftAndUnlock(result, runtimeLock);
            // runtimeLock is now unlocked
        } else {
            runtimeLock.unlock();
        }
    }

    if (!result) {
        // Ask Swift about its un-instantiated classes.

        // We use thread-local storage to prevent infinite recursion
        // if the hook function provokes another lookup of the same name
        // (for example, if the hook calls objc_allocateClassPair)

        auto *tls = _objc_fetch_pthread_data(true);

        // Stop if this thread is already looking up this name.
        for (unsigned i = 0; i < tls->classNameLookupsUsed; i++) {
            if (0 == strcmp(name, tls->classNameLookups[i])) {
                return nil;
            }
        }

        // Save this lookup in tls.
        if (tls->classNameLookupsUsed == tls->classNameLookupsAllocated) {
            tls->classNameLookupsAllocated =
                (tls->classNameLookupsAllocated * 2 ?: 1);
            size_t size = tls->classNameLookupsAllocated *
                sizeof(tls->classNameLookups[0]);
            tls->classNameLookups = (const char **)
                realloc(tls->classNameLookups, size);
        }
        tls->classNameLookups[tls->classNameLookupsUsed++] = name;

        // Call the hook.
        Class swiftcls = nil;
        if (GetClassHook.get()(name, &swiftcls)) {
            ASSERT(swiftcls->isRealized());
            result = swiftcls;
        }

        // Erase the name from tls.
        unsigned slot = --tls->classNameLookupsUsed;
        ASSERT(slot >= 0  &&  slot < tls->classNameLookupsAllocated);
        ASSERT(name == tls->classNameLookups[slot]);
        tls->classNameLookups[slot] = nil;
    }

    return result;
}
```

## NSClassFromString

这个在 `Foundation.framework` 中的实现，并没有开源，

函数原型是

```
FOUNDATION_EXPORT Class _Nullable NSClassFromString(NSString *aClassName);
```

与 `objc_getClass` 参数一样，传入 Class 的名字，返回 Class 地址。

有大佬通过研究汇编分析出它的具体实现：[从汇编代码探究 NSClassFromString 实现](https://xiaozhuanlan.com/topic/5781026934)


最后，做个试验：

```
Student *stu = [Student new];
Class cls = [stu class];
NSLog(@"%p %p %p %p %p", cls, [Student class], objc_getClass("Student"), object_getClass(stu), NSClassFromString(@"Student"));
```

```
0x10000e7b8 0x10000e7b8 0x10000e7b8 0x10000e7b8 0x10000e7b8
```

可以看出来，这四种方法拿到的结果是一样的。



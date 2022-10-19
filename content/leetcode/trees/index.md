---
title: "树的结构与算法系列 一"
date: 2022-06-03T14:57:43+08:00
categories: [Tree, Data Structure]
tags: []
draft: false
---

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-06-03-simon-wilkes-S297j2CsdlM-unsplash.jpg "Photo by [Simon Wilkes](https://unsplash.com/@simonfromengland) on [Unsplash](https://unsplash.com/)")

树是一种重要的数据结构，在计算机科学与工程实践中都应用广泛。

这一系统将总结目前所有树相关的结构与算法，重点关注它们的 `Swift` 实现。

## 分类

常见的树有：

* 二叉树（满二叉树）
* AVL 树
* B/B+ 树
* Trie 树 （字典树）
* ...

## 数据结构

以二叉树为例，树的数据结构中包含三个属性：值，左子树节点，右子树节点。

![](https://ryder-1252249141.cos.ap-shanghai.myqcloud.com/uPic/2022-10-19-carbon.png)

## 构造

一般测试数据的输入是数组，我们需要将数组转换成树结构。同时，为了便于输出验证，也需要将树再转回数组。
其实就是层次遍历及其逆向构造树的过程。

```swift
public extension TreeNode {
    func array() -> [Int?] {
        var ans: [Int?] = []
        var queue: [TreeNode?] = [self]
        while !queue.isEmpty {
            if let node = queue.removeFirst() {
                ans.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            } else {
                ans.append(nil)
            }
        }
        // remove nils at last
        while ans.last == nil {
            ans.removeLast()
        }
        return ans
    }

    // level traversal
    static func arrayToTree(_ nums: [Int?]) -> TreeNode? {
        guard nums.count > 0 else { return nil }
        guard let rootVal = nums[0] else { return nil }
        let root = TreeNode(rootVal)
        var queue: [TreeNode?] = [root]
        var i = 1
        let sz = nums.count
        while !queue.isEmpty && i < sz {
            let node = queue.removeFirst()
            if let val = nums[i] {
                let left = TreeNode(val)
                node?.left = left
                queue.append(left)
            }
            i += 1
            if i >= sz {
                break
            }
            if let val = nums[i] {
                let right = TreeNode(val)
                node?.right = right
                queue.append(right)
            }
            i += 1
        }
        return root
    }
}
```

## 遍历

通常有三种遍历方法：前序、中序和后序。

区分的方法就看访问根节点是在前、中还是后。

### 递归

递归的逻辑比较简单，写法也非常统一。

```swift
// MARK: - Recursive Traversal
public extension TreeNode {
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        var ans = [Int]()
        func _inorder(_ node: TreeNode?, _ res: inout [Int]) {
            guard let node = node else { return }
            _inorder(node.left, &res)
            res.append(node.val)
            _inorder(node.right, &res)
        }
        _inorder(root, &ans)
        return ans
    }

    func preorderTraversal(_ root: TreeNode?) -> [Int] {
        var ans = [Int]()
        func _preorder(_ node: TreeNode?, _ res: inout [Int]) {
            guard let node = node else { return }
            res.append(node.val)
            _preorder(node.left, &res)
            _preorder(node.right, &res)
        }
        _preorder(root, &ans)
        return ans
    }

    func postorderTraversal(_ root: TreeNode?) -> [Int] {
        var ans = [Int]()
        func _postorder(_ node: TreeNode?, _ res: inout [Int]) {
            guard let node = node else { return }
            _postorder(node.left, &res)
            _postorder(node.right, &res)
            res.append(node.val)
        }
        _postorder(root, &ans)
        return ans
    }
}
```

### 非递归

非递归的写法，大多数都是用栈实现的。但是各种写法的差异也比较大，特别是有些加了各种标记和回溯逻辑，比较难理解。
以下是我觉得相对容易理解的。

* 首先，前序和中序逻辑是非常类似的，区别仅在于输出结果的时机：

> 针对一个子树，都是先一直往左走，找到最左边的节点为止。前序遍历是边找边输出，而中序则是结束的时候才输出。之后，再转向右子树。

```swift
// MARK: - Iteratively Traversal
public extension TreeNode {
    func inorderTraversal_i(_ root: TreeNode?) -> [Int] {
        var ans = [Int]()
        var stack = [TreeNode]()
        var node = root
        while !stack.isEmpty || node != nil {
            while node != nil {
                stack.append(node!)
                node = node?.left
            }
            let top = stack.popLast()
            // 区别
            ans.append(top!.val)
            node = top!.right
        }
        return ans
    }

    func preorderTraversal_i(_ root: TreeNode?) -> [Int] {
        var ans = [Int]()
        var stack = [TreeNode]()
        var node = root
        while !stack.isEmpty || node != nil {
            while node != nil {
                stack.append(node!)
                // 区别
                ans.append(node!.val)
                node = node!.left
            }
            let top = stack.popLast()
            node = top!.right
        }
        return ans
    }
```

* 后序遍历会相对麻烦一点，但也和上面的写法尽量类似：

> 先一直向右走，边走边输出节点（插到开头，所以最好用链表实现），然后再向左走。

```swift
public extension TreeNode {
    func postorderTraversal_i(_ root: TreeNode?) -> [Int] {
        var ans = [Int]()
        var stack = [TreeNode]()
        var node = root
        while !stack.isEmpty || node != nil {
            while node != nil {
                stack.append(node!)
                // 这里每次插入开头
                ans.insert(node!.val, at: 0)
                // 先右后左
                node = node?.right
            }
            let top = stack.popLast()
            node = top!.left
        }
        return ans
    }
}
```

更多 [树相关的内容](/categories/tree/) 敬请期待 👀...

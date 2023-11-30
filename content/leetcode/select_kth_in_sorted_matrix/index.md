---
title: "在已排序的矩阵中找出第 k 大的数"
date: 2023-11-30T17:40:10+08:00
categories: []
tags: []
---

Leetcode 经典题：https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

> 这个问题题意很简单，在一个行和列都是非递减排序的矩阵中，求第 k 小的数。

题目下面有两个 follow up：

1. Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?

2. Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading [this paper](http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf) fun.

第一条，我没有仔细思考过，我觉得可能的解法是将整个 matrix 原地排序。

第二条中提到了这个论文，最近花时间看了下，是一篇非常古早的论文了（1984 年）。本质是是一种分治方法。

## 常规解法

最容易想到的是用数组读出来，然后排序。显然时间复杂度 O(n^2log(n^2))，空间复杂度 O(n^2)。

进一步利用优先队列优化一下，首先将第一行放入队列，然后每次 dequeue 一个，计数，并 enqueue 一个同一列的数。直到第 k 个结束。

这样的时间复杂度 O(nlogn)，空间复杂度 O(n)。

```swift
#if !LC_SOLUTION_EXT
class Solution {}
#endif
extension Solution {
    func kthSmallest(_ matrix: [[Int]], _ k: Int) -> Int {
        let n = matrix.count
        typealias Pair = (i: Int, j: Int, v: Int)
        var pq = PriorityQueue<Pair>([], { $0.v < $1.v })
        for j in 0..<n {
            pq.enqueue((i: 0, j: j, v: matrix[0][j]))
        }
        var cnt = 0
        var ans = 0
        while cnt < k {
            guard let last = pq.dequeue() else { break }
            if last.i < n - 1 {
                pq.enqueue((i: last.i + 1, j: last.j, v: matrix[last.i+1][last.j]))
            }
            ans = last.v
            cnt += 1
        }
        return ans
    }
}
```

已经是比较优化的一种解法了，但下面论文的给出的是一种 O(n) 的解法。

## 论文解法 

http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf

伪代码

```

```

## 泛化解法

论文解法只适用于 n * n 的矩阵，而且求子矩阵比较复杂，搜索到一篇泛化成 n * m 矩阵并简化解法的文章：

https://chaoxu.prof/posts/2014-04-02-selection-in-a-sorted-matrix.html

代码是用 Haskell 写的，用 [在线转化器](https://www.codeconvert.ai/haskell-to-c-converter) 转换成 C 语言的。

```haskell
import Data.List
import Control.Applicative
import Control.Arrow
import Control.Monad
import RankSelection
-- this provides selectRank, which outputs the kth largest element of a list
-- selectRank :: Ord a => [a] -> Int -> a

type Matrix a = (Int->Int->a, Int, Int)

-- The input is an matrix sorted in both row and column order
-- This selects the kth smallest element. (0th is the smallest)
selectMatrixRank :: Ord a => Int -> Matrix a -> a
selectMatrixRank k (f,n,m)
 | k >= n*m || k < 0 = error "rank doesn't exist"
 | otherwise         = fst $ fst $ biselect k k (f', min n (k+1), min m (k+1))
 where f' x y= (f x y, (x, y))

biselect :: Ord a => Int -> Int -> Matrix a -> (a,a)
biselect lb ub (f',n',m') = join (***) (selectRank values) (lb-ra, ub-ra)
 where mat@(f,n,m)
        | n' > m'   = (flip f', m', n')
        | otherwise = (f', n', m')
       (a, b)
        | n < 3     = (f 0 0, f (n-1) (m-1))
        | otherwise = biselect lb' ub' halfMat
       (lb', ub')   = (lb `div` 2, min ((ub `div` 2) + n) (n * hm - 1))
       (ra, values) = (rankInMatrix mat a, selectRange mat a b)
       halfMat
        | even m = (\x y->f x (if y < hm - 1 then 2 * y else 2 * y - 1), n, hm)
        | odd  m = (\x y->f x (2*y), n, hm)
       hm = m `div` 2 + 1

-- the rank of an element in the matrix
rankInMatrix :: Ord a => Matrix a -> a -> Int
rankInMatrix mat a = sum (map (\(_,y)->1+y) $ frontier mat a)-1

-- select all elements x in the matrix such that a <= x <= b 
selectRange :: Ord a => Matrix a -> a -> a -> [a]
selectRange mat@(f,_,_) a b = concatMap search (frontier mat b)
 where search (x,y) = takeWhile (>=a) $ map (f x) [y,y-1..0]

frontier :: Ord a => Matrix a -> a -> [(Int,Int)]
frontier (f,n,m) b = step 0 (m-1)
 where step i j 
        | i > n-1 || j < 0 = []
        | f i j <= b       = (i,j):step (i+1) j
        | otherwise        = step i (j-1)
```

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int (*f)(int, int);
    int n;
    int m;
} Matrix;

int selectMatrixRank(int k, Matrix mat);
int biselect(int lb, int ub, Matrix mat);
int rankInMatrix(Matrix mat, int a);
int selectRange(Matrix mat, int a, int b);

int main() {
    // Example usage
    Matrix mat;
    mat.f = &f;
    mat.n = 3;
    mat.m = 3;
    int result = selectMatrixRank(4, mat);
    printf("%d\n", result);
    return 0;
}

int f(int x, int y) {
    // Define your matrix function here
    // Example implementation:
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    return matrix[x][y];
}

int selectMatrixRank(int k, Matrix mat) {
    if (k >= mat.n * mat.m || k < 0) {
        printf("rank doesn't exist\n");
        exit(1);
    }
    int a, b;
    if (mat.n < 3) {
        a = mat.f(0, 0);
        b = mat.f(mat.n - 1, mat.m - 1);
    } else {
        int lb = k / 2;
        int ub = (k / 2) + mat.n;
        int ra, values;
        int halfMatN, halfMatM;
        if (mat.n > mat.m) {
            halfMatN = mat.m;
            halfMatM = mat.n;
            int halfMat[halfMatN][halfMatM];
            for (int i = 0; i < halfMatN; i++) {
                for (int j = 0; j < halfMatM; j++) {
                    halfMat[i][j] = mat.f(i, (j < halfMatM - 1) ? 2 * j : 2 * j - 1);
                }
            }
            int lbPrime = lb / 2;
            int ubPrime = (ub / 2) + halfMatN;
            int raPrime, valuesPrime;
            biselect(lbPrime, ubPrime, halfMat, &raPrime, &valuesPrime);
            ra = rankInMatrix(mat, raPrime);
            values = selectRange(mat, raPrime, valuesPrime);
        } else {
            halfMatN = mat.n;
            halfMatM = mat.m;
            int halfMat[halfMatN][halfMatM];
            for (int i = 0; i < halfMatN; i++) {
                for (int j = 0; j < halfMatM; j++) {
                    halfMat[i][j] = mat.f(i, 2 * j);
                }
            }
            int lbPrime = lb / 2;
            int ubPrime = (ub / 2) + halfMatN;
            int raPrime, valuesPrime;
            biselect(lbPrime, ubPrime, halfMat, &raPrime, &valuesPrime);
            ra = rankInMatrix(mat, raPrime);
            values = selectRange(mat, raPrime, valuesPrime);
        }
        a = values;
        b = values;
    }
    return a;
}

int biselect(int lb, int ub, Matrix mat, int *ra, int *values) {
    int lbPrime = lb / 2;
    int ubPrime = (ub / 2) + mat.n;
    int raPrime, valuesPrime;
    biselect(lbPrime, ubPrime, mat, &raPrime, &valuesPrime);
    *ra = raPrime;
    *values = valuesPrime;
}

// the rank of an element in the matrix
int rankInMatrix(int** mat, int n, int m, int a) {
    int rank = 0;
    for (int i = 0; i < n; i++) {
        for (int j = m - 1; j >= 0; j--) {
            if (mat[i][j] == a) {
                return rank;
            }
            rank++;
        }
    }
    return -1;
}

// select all elements x in the matrix such that a <= x <= b 
int* selectRange(int** mat, int n, int m, int a, int b, int* size) {
    int* result = malloc(n * m * sizeof(int));
    int index = 0;
    for (int i = 0; i < n; i++) {
        for (int j = m - 1; j >= 0; j--) {
            if (mat[i][j] >= a && mat[i][j] <= b) {
                result[index] = mat[i][j];
                index++;
            }
        }
    }
    *size = index;
    return result;
}

int** frontier(int** mat, int n, int m, int b, int* size) {
    int** result = malloc(n * sizeof(int*));
    int index = 0;
    for (int i = 0; i < n; i++) {
        for (int j = m - 1; j >= 0; j--) {
            if (mat[i][j] <= b) {
                result[index] = malloc(2 * sizeof(int));
                result[index][0] = i;
                result[index][1] = j;
                index++;
            }
        }
    }
    *size = index;
    return result;
}

int main() {
    // Example usage
    int n = 3;
    int m = 4;
    int** mat = malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        mat[i] = malloc(m * sizeof(int));
    }
    mat[0][0] = 1;
    mat[0][1] = 2;
    mat[0][2] = 3;
    mat[0][3] = 4;
    mat[1][0] = 5;
    mat[1][1] = 6;
    mat[1][2] = 7;
    mat[1][3] = 8;
    mat[2][0] = 9;
    mat[2][1] = 10;
    mat[2][2] = 11;
    mat[2][3] = 12;

    int rank = rankInMatrix(mat, n, m, 7);
    printf("Rank: %d\n", rank);

    int size;
    int* range = selectRange(mat, n, m, 3, 9, &size);
    printf("Range: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", range[i]);
    }
    printf("\n");

    int frontierSize;
    int** frontierResult = frontier(mat, n, m, 7, &frontierSize);
    printf("Frontier: ");
    for (int i = 0; i < frontierSize; i++) {
        printf("(%d, %d) ", frontierResult[i][0], frontierResult[i][1]);
    }
    printf("\n");

    // Free memory
    for (int i = 0; i < n; i++) {
        free(mat[i]);
    }
    free(mat);
    free(range);
    for (int i = 0; i < frontierSize; i++) {
        free(frontierResult[i]);
    }
    free(frontierResult);

    return 0;
}

```
# ========================== #
# Segment Tree Min Max Query #
# ========================== #

import sys, math
input = sys.stdin.readline

# Segment Tree, Min/Max Query
A, TREE = []
def BuildTree():
    global A, TREE
    N = 1 << (math.ceil(math.log2(len(A))))
    A += [0] * (N - len(A))
    
    TREE = [0 for _ in range(N << 1)]
    for i in range(N):
        TREE[N + i] = (i, i)

    for i in range(N - 1, 0, -1):
        min_L, max_L = TREE[(i << 1)]
        min_R, max_R = TREE[(i << 1) | 1]

        if A[min_L] < A[min_R]: min_ = min_L
        else: min_ = min_R

        if A[max_L] > A[max_R]: max_ = max_L
        else: max_ = max_R

        TREE[i] = (min_, max_)

def Query(L, R):
    global A, TREE
    min_, max_ = L, L
    L += len(TREE) >> 1
    R += len(TREE) >> 1

    while L <= R:
        if L == R:
            min_L, max_L = TREE[L]
            if A[min_L] < A[min_]: min_ = min_L
            if A[max_L] > A[max_]: max_ = max_L
            break
        if L & 1 == 1:
            min_L, max_L = TREE[L]
            if A[min_L] < A[min_]: min_ = min_L
            if A[max_L] > A[max_]: max_ = max_L
            L += 1; continue
        if R & 1 == 0:
            min_R, max_R = TREE[R]
            if A[min_R] < A[min_]: min_ = min_R
            if A[max_R] > A[max_]: max_ = max_R
            R -= 1; continue
        
        L >>= 1
        R >>= 1

    return min_, max_

def ModifyValue(X, val):
    global A, TREE
    A[X] += val
    X += len(TREE) >> 1; X >>= 1

    while X:
        min_L, max_L = TREE[(X << 1)]
        min_R, max_R = TREE[(X << 1) | 1]

        if A[min_L] < A[min_R]: min_ = min_L
        else: min_ = min_R

        if A[max_L] > A[max_R]: max_ = max_L
        else: max_ = max_R

        TREE[X] = (min_, max_)
        X >>= 1

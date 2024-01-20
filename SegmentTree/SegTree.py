################################
##### Segment Tree (Basic) #####
################################

import sys, math

# Build Segment Tree
def Build(A, default=0):
    N = 1 << (math.ceil(math.log2(len(A))))
    A += [default] * (N - len(A))
    assert len(A) == N

    TREE = [default for _ in range(2 * N)]
    for i in range(N):
        TREE[N + i] = A[i]
    for i in range(N - 1, 0, -1):
        TREE[i] = TREE[i << 1] + TREE[(i << 1) | 1]
    return TREE

# Query : Sum of A[L], A[L + 1], ..., A[R]
def Query(TREE, L, R):
    res = 0
    L += len(TREE) >> 1
    R += len(TREE) >> 1
    while L <= R:
        if L == R: res += TREE[L]; break
        if L & 1 == 1: res += TREE[L]; L += 1; continue
        if R & 1 == 0: res += TREE[R]; R -= 1; continue
        L >>= 1; R >>= 1
    return res

# Modify Single Value : Add val to A[i]
def ModifyValue(TREE, i, val):
    i += len(TREE) >> 1
    while i:
        TREE[i] += val
        i >>= 1
    return TREE

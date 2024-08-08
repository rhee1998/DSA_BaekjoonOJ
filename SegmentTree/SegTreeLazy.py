##############################################
##### Segment Tree with Lazy Propagation #####
##############################################

import sys, math
from collections import deque
input = sys.stdin.readline

TREE, RANG, LAZY = [], [], []

# Build Segment Tree
def Build(A, default=0):
    global TREE, RANG, LAZY
    N = 1 << (math.ceil(math.log2(len(A))))
    A += [default] * (N - len(A))

    TREE = [default for _ in range(2 * N)]
    RANG = [0 for _ in range(2 * N)]
    LAZY = [0 for _ in range(2 * N)]

    for i in range(N):
        TREE[N + i] = A[i]
        RANG[N + i] = (i, i)

    for i in range(N - 1, 0, -1):
        TREE[i] = TREE[i << 1] + TREE[(i << 1) | 1]
        RANG[i] = (RANG[i << 1][0], RANG[(i << 1) | 1][1])

# Update Lazy
def UpdateLazy(node):
    global TREE, RANG, LAZY
    if LAZY[node] != 0:
        S, E = RANG[node]
        TREE[node] += LAZY[node] * (E - S + 1)
        if S != E:
            LAZY[node << 1] += LAZY[node]
            LAZY[(node << 1) | 1] += LAZY[node]
        LAZY[node] = 0

# Modify Range : Add val to A[L], A[L + 1], ..., A[R]
def UpdateRange(L, R, val):
    global TREE, RANG, LAZY
    que, back = deque([1]), []
    while que:
        node = que.popleft()
        S, E = RANG[node]; UpdateLazy(node)
        
        if L > E or R < S:
            continue

        if L <= S and E <= R:
            TREE[node] += (E - S + 1) * val
            if S != E:
                LAZY[node << 1] += val
                LAZY[(node << 1) | 1] += val
            continue

        que.append((node << 1))
        que.append((node << 1) | 1)
        back.append(node)
    
    while back:
        node = back.pop()
        try: TREE[node] = TREE[(node << 1)] + TREE[(node << 1) | 1]
        except: continue

# Query : Sum of A[L], A[L + 1], ..., A[R]
def Query(L, R):
    global TREE, RANG, LAZY
    res = 0
    que = deque([1])
    while que:
        node = que.popleft()
        S, E = RANG[node]; UpdateLazy(node)

        if L > E or R < S: continue
        if L <= S and E <= R: res += TREE[node]; continue

        que.append((node << 1))
        que.append((node << 1) | 1)

    return res

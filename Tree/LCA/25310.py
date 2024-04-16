# 25310 곰곰이의 아르바이트 [P2]
import sys, math
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
G = {v : [] for v in range(N)}
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b); G[b].append(a)

# Define Sparse Array
INF = 10**30
MIN, MAX, K = INF, 0, math.ceil(math.log2(N))
sparse = [[None for _ in range(N)] for _ in range(K + 1)]
rank = [0 for _ in range(N)]

# BFS to obtain sparse[0] & rank
visited = [False for _ in range(N)]
sparse[0][0], visited[0] = 0, True
que = deque([0])

while que:
    curr = que.popleft()
    for next in G[curr]:
        if visited[next] == True: continue
        
        sparse[0][next] = curr
        rank[next] = rank[curr] + 1
        que.append(next); visited[next] = True

# Iterate to obtain sparse array
for k in range(len(sparse) - 1):
    for i in range(N):
        x = sparse[k][i]
        sparse[k + 1][i] = sparse[k][x]

# Move up n steps from x
def MoveUp(x, n):
    if n == 0: return x
    if n >= rank[x]: return 0

    k = 0
    while n > 0:
        if n % 2 == 1:
            x = sparse[k][x]
        n, k = n >> 1, k + 1
    return x

# Lowest Common Ancestor (LCA)
def LCA(x, y):
    diff = rank[x] - rank[y]
    if diff > 0: return LCA(MoveUp(x, abs(diff)), y)
    if diff < 0: return LCA(x, MoveUp(y, abs(diff)))

    if x == y: return x

    k = len(sparse) - 1
    while k >= 0:
        if sparse[k][x] == sparse[k][y]:
            k = k - 1; continue
        x, y = sparse[k][x], sparse[k][y]

    assert sparse[0][x] == sparse[0][y]
    return sparse[0][x]

# Query
for _ in range(Q):
    a, b, c = map(int, input().split())
    a, b, c = a - 1, b - 1, c - 1

    ab, bc, ca = LCA(a, b), LCA(b, c), LCA(c, a)
    if ab == bc == ca:
        x = rank[a] - rank[ab]
        y = rank[b] - rank[ab]
        z = rank[c] - rank[ab]
    elif ab == bc:
        x = rank[a] - rank[ca]
        y = rank[ca] - rank[ab] + rank[b] - rank[ab]
        z = rank[c] - rank[ca]
    elif bc == ca:
        x = rank[a] - rank[ab]
        y = rank[b] - rank[ab]
        z = rank[ab] - rank[bc] + rank[c] - rank[bc]
    else:
        x = rank[bc] - rank[ab] + rank[a] - rank[ab]
        y = rank[b] - rank[bc]
        z = rank[c] - rank[bc]

    w = x + 2 * y + z
    ans = ((w + 1) * w) // 2 - ((y + 1) * y) // 2 - (x + z) * y
    sys.stdout.write(f'{ans}\n')

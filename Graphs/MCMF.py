# ========================= #
# Minimum Cost Maximum Flow #
# ========================= #

# 11408 열혈강호 5
import sys
from collections import deque
input = sys.stdin.readline
INF = 10**20

N, M = map(int, input().split())
S, E, V = 0, N + M + 1, N + M + 2

G = {v: {} for v in range(V)}
for i in range(1, N + 1):
    G[S][i] = [1, 0, 0]
    G[i][S] = [0, 0, 0]

    inp = [int(x) for x in input().split()[1:]]
    work_list = [x + N for x in inp[0::2]]
    cost_list = inp[1::2]

    for work, cost in zip(work_list, cost_list):
        G[i][work] = [1,  cost, 0]
        G[work][i] = [0, -cost, 0]

for j in range(N + 1, V - 1):
    G[j][E] = [1, 0, 0]
    G[E][j] = [0, 0, 0]

while True:
    # SPFA
    dist = [INF   for _ in range(V)]
    prev = [-1    for _ in range(V)]
    in_Q = [False for _ in range(V)]

    que = deque([S])
    dist[S], in_Q[S] = 0, True

    while que:
        curr = que.popleft()
        in_Q[curr] = False

        for next in G[curr].keys():
            [capacity, cost, flow] = G[curr][next]

            if flow < capacity and dist[curr] + cost < dist[next]:
                dist[next] = dist[curr] + cost
                prev[next] = curr
                
                if in_Q[next] == False:
                    que.append(next)
                    in_Q[next] = True

    # Break if shortest path is not found
    if prev[E] == -1: break

    # Update flow distribution
    curr_, flow_ = E, INF
    while curr_ != S:
        prev_ = prev[curr_]
        flow_ = min([flow_, G[prev_][curr_][0] - G[prev_][curr_][2]])
        curr_ = prev_

    curr_ = E
    while curr_ != S:
        prev_ = prev[curr_]
        G[prev_][curr_][2] += flow_
        G[curr_][prev_][2] -= flow_
        curr_ = prev_

# Total Flow
total_flow = 0
for i in G[S].keys():
    total_flow += G[S][i][2]

# Total Cost
total_cost = 0
for curr in G.keys():
    for next in G[curr].keys():
        if curr < next:
            total_cost += G[curr][next][1] * G[curr][next][2]

sys.stdout.write(f'{total_flow}\n{total_cost}')

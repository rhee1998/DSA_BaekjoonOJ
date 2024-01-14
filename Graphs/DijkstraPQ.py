###############################################
##### Dijkstra's Algorithm [O((V+E)logV)] #####
###############################################
import heapq

def Dijkstra(start, N, G, INF=10**30):
    # --------------------------------------------------
    # Input(s)  : starting node ID, number of nodes, graph
    # Output(s) : minimum distances from start to each node
    # --------------------------------------------------
    # Initialize PQ
    que = []
    heapq.heappush(que, (0, start))

    # Initialize result
    dists = [INF for _ in range(N)]
    dists[start] = 0

    # Iterate over PQ
    while que:
        cost, curr = heapq.heappop(que)
        if dists[curr] < cost: continue
        for next, dist in G[curr]:
            tmp = cost + dist
            if tmp < dists[next]:
                dists[next] = tmp
                heapq.heappush(que, (dists[next], next))
    return dists


def DijkstraPath(start, N, G, INF=10**30):
    # --------------------------------------------------
    # Input(s)  : starting node ID, number of nodes, graph
    # Output(s) : minimum distances from start to each node with path
    # --------------------------------------------------
    # Initialize PQ
    que = []
    heapq.heappush(que, (0, start, [start]))

    # Initialize result
    dists = [INF for _ in range(N)]
    paths = [[] for _ in range(N)]

    dists[start], paths[start] = 0, [start]

    # Iterate over PQ
    while que:
        cost, curr, path = heapq.heappop(que)
        if dists[curr] < cost: continue
        for next, dist in G[curr]:
            tmp = cost + dist
            if tmp < dists[next]:
                dists[next] = tmp
                paths[next] = path + [next]
                heapq.heappush(que, (dists[next], next, paths[next]))
    
    return dists, paths

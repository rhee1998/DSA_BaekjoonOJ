######################
##### Union Find #####
######################

parent = [v for v in range(V)]
rank = [0 for _ in range(V)]

def FindRoot(x):
    while x != parent[x]:
        x = parent[x]
    return x

def Union(x, y):
    px, py = FindRoot(x), FindRoot(y)

    if rank[px] < rank[py]: px, py = py, px
    if rank[px] == rank[py]: rank[px] += 1

    parent[py] = px
    return

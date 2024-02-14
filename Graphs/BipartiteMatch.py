# =============== #
# Bipartite Match #
# =============== #
import sys

def BipartiteMatch(x, graph):
    # ==================================================
    # Input(s)
    # - x        : node from A
    # - graph    : graph containing connection information from A to B
    # - visited  : bool list of visited indices in A
    # - selected : selected[y] == x if x from A is connected to y from B
    #
    # Output(s)
    # - boolean value indicating whether match is successful
    # ==================================================
    if visited[x]:
        return False
    visited[x] = True

    for y in graph[x]:
        if selected[y] == -1 or BipartiteMatch(selected[y], graph):
            selected[y] = x
            return True
    
    return False

# Sample Code
selected = [-1 for _ in range(len(B))]
for i in range(len(A)):
    visited = [False for _ in range(len(A))]
    BipartiteMatch(i, graph=G)

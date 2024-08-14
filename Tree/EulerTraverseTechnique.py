# ======================== #
# Euler Traverse Technique #
# ======================== #
import sys, math

# Euler Traverse Technique
def EulerTraverse(G, root=0):
    V = G.keys()
    visited, dfs = [False for _ in range(len(V))], {}
    
    stack, dfs_cnt = [], 0
    visited[root] = True; stack.append(root)

    while stack:
        curr = stack[-1]
        if not dfs.get(curr) is None:
            dfs[curr] = (dfs[curr], dfs_cnt - 1)
            stack.pop(); continue
        else:
            dfs[curr] = dfs_cnt; dfs_cnt += 1

        for next in G[curr]:
            if visited[next]: continue
            
            visited[next] = True
            stack.append(next)

    return dfs

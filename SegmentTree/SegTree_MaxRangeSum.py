# ========================================== #
# Segment Tree Maximum Consecutive Range Sum #
# ========================================== #
import sys, math
input = sys.stdin.readline

# Segment Tree, Max Consecutive Range Sum
# TREE[range=[S, E]] = (sum_XY, sum_SX, sum_XE, sum_SE)

TREE = []
def MergeNode(node_L, node_R):
    XY_L, SX_L, XE_L, SE_L = node_L
    XY_R, SX_R, XE_R, SE_R = node_R

    XY_ = max([XY_L, XY_R, XE_L + SX_R])
    SX_ = max([SX_L, SE_L + SX_R])
    XE_ = max([XE_R, XE_L + SE_R])
    SE_ = SE_L + SE_R

    return (XY_, SX_, XE_, SE_)

def BuildTree(A):
    global TREE
    N = 1 << (math.ceil(math.log2(len(A))))
    A += [0] * (N - len(A))
    
    TREE = [0 for _ in range(N << 1)]
    for i in range(N):
        TREE[N + i] = (A[i], A[i], A[i], A[i])

    for i in range(N - 1, 0, -1):
        TREE[i] = MergeNode(TREE[(i << 1)], TREE[(i << 1) | 1])

def Query(L, R, INF=10**30):
    global TREE
    L += len(TREE) >> 1
    R += len(TREE) >> 1

    stack_L, stack_R = [], []
    while L <= R:
        if L == R: stack_L.append(TREE[L]); break
        if L & 1 == 1: stack_L.append(TREE[L]); L += 1; continue
        if R & 1 == 0: stack_R.append(TREE[R]); R -= 1; continue
        L >>= 1; R >>= 1

    while stack_R:
        stack_L.append(stack_R.pop())

    node = (-INF, -INF, -INF, 0)
    for node_ in stack_L:
        node = MergeNode(node, node_)

    return node

def ModifyValue(X, val):
    # Change A[X] = val
    global TREE
    X += len(TREE) >> 1
    TREE[X] = (val, val, val, val)
    X >>= 1

    while X:
        TREE[X] = MergeNode(TREE[(X << 1)], TREE[(X << 1) | 1])
        X >>= 1

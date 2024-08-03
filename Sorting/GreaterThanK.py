# Number of elements larger than k
def GreaterThanK(A, K):
    # A should be sorted in ascending order
    if K > A[-1]: return 0
    if K < A[0]: return len(A)

    res = 0
    S, E = 0, len(A) - 1
    while S < E:
        M = (S + E) // 2
        if A[M] > K:
            res += E - M
            S, E = S, M
        else:
            S, E = M + 1, E
    if A[S] > K: res += 1
    return res

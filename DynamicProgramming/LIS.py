# =========================================== #
# Longest Increasing Subsequence [O(n log n)] #
# =========================================== #
import sys
from collections import deque

def LIS(A):
    # ==================================================
    # Input(s)
    # - A : input sequence
    #
    # Output(s)
    # - lis : longest increasing subsequence
    # ==================================================

    loc, tmp = [], []
    for i, a in enumerate(A):
        if tmp == [] or a > tmp[-1]:
            loc.append(len(tmp))
            tmp.append(a)
            continue

        lo, hi = 0, len(tmp) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if a > tmp[mi]: lo, hi = mi + 1, hi
            else: lo, hi = lo, mi

        loc.append(lo)
        tmp[lo] = a

    lis, idx = deque([]), len(tmp) - 1
    for i in range(len(A) - 1, -1, -1):
        if loc[i] == idx:
            lis.appendleft(A[i])
            idx -= 1

    return lis

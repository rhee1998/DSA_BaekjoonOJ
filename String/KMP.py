# ================================== #
# KMP (Knuth-Morris-Pratt) Algorithm #
# ================================== #
import sys
input = sys.stdin.readline

def FailListKMP(P):
    # ==================================================
    # Input(s)
    # - P    : pattern of interest
    #
    # Output(s)
    # - fail : fail[j] is maximum of k <= j such that P[:k] == P[j-k+1:j+1]
    # ==================================================
    assert len(P) > 0
    fail = [0 for _ in range(len(P))]

    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = fail[j - 1]
        
        if P[i] == P[j]:
            j += 1
            fail[i] = j

    return fail

def FindPatternsKMP(T, P, fail=None):
    # ==================================================
    # Input(s)
    # - T    : target string
    # - P    : pattern of interest
    # - fail : fail[j] is maximum of k <= j such that P[:k] == P[j-k+1:j+1]
    #
    # Output(s)
    # - res  : list of starting positions where P is found
    # ==================================================
    if fail is None:
        fail = FailListKMP(P)
    
    j, res = 0, []
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = fail[j - 1]

        if T[i] == P[j]: j += 1
        if j == len(P):
            res.append(i - j + 1)
            j = fail[j - 1]

    return res

# ================================== #
# KMP (Knuth-Morris-Pratt) Algorithm #
# ================================== #
import sys
input = sys.stdin.readline

def FailListKMP(P):
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

##################################
##### Generalized Merge Sort #####
##################################

def Compare(x, y):
    # --------------------------------------------------
    # Input(s)  : variables to compare
    # Output(s) : True if x < y else False
    # --------------------------------------------------
    idx = 0
    while idx < len(x):
        if x[idx] < y[idx]: return True
        elif x[idx] > y[idx]: return False
        else: idx += 1
    return True

def GeneralizedMergeSort(A):
    # --------------------------------------------------
    # Input(s)  : array to sort
    # Output(s) : sorted array
    # --------------------------------------------------
    L = len(A)
    if L <= 1: return A

    F = GeneralizedMergeSort(A[:L//2])
    B = GeneralizedMergeSort(A[L//2:])
    fidx, bidx, R = 0, 0, []

    while fidx < L//2 and bidx <= L - L//2:
        if Compare(F[fidx], B[bidx]):
            R.append(F[fidx]); fidx += 1
        else:
            R.append(B[bidx]); bidx += 1
    
    R += F[fidx:] + B[bidx:]
    return R

######################
##### Merge Sort #####
######################

def MergeSort(A):
    # --------------------------------------------------
    # Input(s)  : array to sort
    # Output(s) : sorted array
    # --------------------------------------------------
    L = len(A)
    if L <= 1: return A

    F, B = MergeSort(A[:L//2]), MergeSort(A[L//2:])
    fidx, bidx, R = 0, 0, []

    while fidx < L//2 and bidx < L - L//2:
        if F[fidx] < B[bidx]:
            R.append(F[fidx]); fidx += 1
        else:
            R.append(B[bidx]); bidx += 1
    
    R += F[fidx:] + B[bidx:]
    return R

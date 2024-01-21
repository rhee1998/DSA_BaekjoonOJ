# Merge
def Merge(A, B):
    # A and B should be sorted in ascending order
    aidx, bidx, R = 0, 0, []
    while aidx < len(A) and bidx < len(B):
        if A[aidx] < B[bidx]: R.append(A[aidx]); aidx += 1
        else: R.append(B[bidx]); bidx += 1
    return R + A[aidx:] + B[bidx:]

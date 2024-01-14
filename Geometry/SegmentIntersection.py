################################
##### Segment Intersection #####
################################

def Compare(A, B):
    if A[0] < B[0] or (A[0] == B[0] and A[1] < B[1]): return +1
    if A[0] > B[0] or (A[0] == B[0] and A[1] > B[1]): return -1
    return 0

def CCW(A, B, C):
    # Determines whether A -> B -> C movement is counter-clockwise(ccw)
    # Returns : +1 if ccw / -1 if cw / 0 if straight
    AB = (B[0] - A[0], B[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])
    res = AB[0] * BC[1] - AB[1] * BC[0]
    if res > 0: return 1
    if res < 0: return -1
    return 0

def Intersect(A, B, C, D):
    # Determines whether segments AB and CD intersect
    ccw_ABC, ccw_ABD = CCW(A, B, C), CCW(A, B, D)
    ccw_CDA, ccw_CDB = CCW(C, D, A), CCW(C, D, B)

    if ccw_ABC * ccw_ABD > 0: return False
    if ccw_CDA * ccw_CDB > 0: return False

    if ccw_ABC * ccw_ABD < 0: return True
    if ccw_CDA * ccw_CDB < 0: return True

    if Compare(A, B) < 0: A, B = B, A
    if Compare(C, D) < 0: C, D = D, C

    if Compare(B, C) > 0 or Compare(D, A) > 0: return False
    return True

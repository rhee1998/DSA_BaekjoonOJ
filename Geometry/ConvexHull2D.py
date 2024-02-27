# ================ #
# Convex Hull (2D) #
# ================ #

# Basic Geometrical Functions
def ComparePoints2D(A, B):
    if A[0] < B[0] or (A[0] == B[0] and A[1] < B[1]): return +1
    if A[0] > B[0] or (A[0] == B[0] and A[1] > B[1]): return -1
    return 0

def CCW(A, B, C):
    AB = (B[0] - A[0], B[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])
    res = AB[0] * BC[1] - AB[1] * BC[0]
    
    if res > 0: return 1
    if res < 0: return -1
    return 0

def DistSquare(A, B):
    AB = (B[0] - A[0], B[1] - A[1])
    return AB[0]**2 + AB[1]**2

# Generalized Merge Sort
def Compare(A, B, O):
    ccw = CCW(O, A, B)
    OA2, OB2 = DistSquare(O, A), DistSquare(O, B)
    
    if ccw == 1 or (ccw==0 and OA2 < OB2):
        return True
    return False

def GeneralizedMergeSort(A, O):
    L = len(A)
    if L <= 1: return A

    F = GeneralizedMergeSort(A[:L//2], O)
    B = GeneralizedMergeSort(A[L//2:], O)
    fidx, bidx, R = 0, 0, []

    while fidx < L//2 and bidx < L - L//2:
        if Compare(F[fidx], B[bidx], O):
            R.append(F[fidx]); fidx += 1
        else:
            R.append(B[bidx]); bidx += 1
    
    R += F[fidx:] + B[bidx:]
    return R

# Convex Hull (2D)
def ConvexHull2D(pts):
    # Remove duplicates
    D, P = {}, []
    for pt in pts:
        if not D.get(pt) is None: continue
        D[pt] = 1; P.append(pt)

    # Trivial cases
    if len(P) <= 2: return P

    # Sort points
    O = P[0]
    for i, pt in enumerate(P):
        if ComparePoints2D(pt, O) > 0: O = pt
    P.remove(O)
    P = GeneralizedMergeSort(P, O)

    # Graham's method (stack)
    CH = [O, P[0]]
    for pt in P[1:]:
        while len(CH) >= 2:
            if CCW(CH[-2], CH[-1], pt) > 0: break
            else: CH.pop()
        CH.append(pt)

    return CH

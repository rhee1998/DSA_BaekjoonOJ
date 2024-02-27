# ======================= #
# Counter Clockwise (CCW) #
# ======================= #

def CCW(A, B, C):
    # ==================================================
    # Input(s)
    # - A, B, C    : tuples containing (x, y) coordinates
    #
    # Output(s)
    # - integer    : +1 if CCW / -1 if CW / 0 if straight
    # ==================================================
    AB = (B[0] - A[0], B[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])
    res = AB[0] * BC[1] - AB[1] * BC[0]

    if res > 0: return 1
    if res < 0: return -1
    return 0

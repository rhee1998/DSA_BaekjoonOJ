# ======================= #
# Basic Matrix Operations #
# ======================= #

# Matrix Addition
def MatAdd(A, B, MOD=MOD):
    N, M = len(A), len(A[0])
    R = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            R[i][j] = (A[i][j] + B[i][j]) % MOD
    
    return R

# Matrix Multiplication
def MatMul(A, B, MOD=MOD):
    N, M, K = len(A), len(A[0]), len(B[0])
    R = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        for k in range(K):
            tmp = 0
            for j in range(M):
                tmp = (tmp + A[i][j] * B[j][k]) % MOD
            R[i][j] = tmp
    
    return R

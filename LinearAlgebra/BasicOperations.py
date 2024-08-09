# ======================= #
# Basic Matrix Operations #
# ======================= #

# Identity Matrix
def MatIdentity(N):
    I = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        I[i][i] = 1
    
    return I

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
            R[i][k] = tmp
    
    return R

# Power of Matrix
def MatPow(A, K, MOD=MOD):
    N = len(A)
    if K == 0: return MatIdentity(N)
    if K == 1: return A

    tmp = MatPow(A, K // 2, MOD=MOD)
    tmp = MatMul(tmp, tmp, MOD=MOD)
    
    if K % 2 == 0: return tmp
    return MatMul(A, tmp, MOD=MOD)

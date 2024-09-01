# =============================================== #
# Discrete Square Root (Tonelli-Shanks Algorithm) #
# =============================================== #
import sys, math
input = sys.stdin.readline

# Power Function (Non-Recursive)
def pow(N, k, mod):
    if N % mod == 0: return 0

    res, tmp = 1, N % mod
    while k:
        if k & 1:
            res = (res * tmp) % mod
        tmp = (tmp * tmp) % mod
        k >>= 1

    return res


# Modulo Inverse
def inverse(N, P):
    return pow(N, P - 2, mod=P)


# Legendre (N | P)
def legendre(N, P):
    if N % P == 0: return 0
    if pow(N, (P - 1) // 2, mod=P) == 1: return 1
    return -1


# Find a Non-Quadratic Residual of P
# i.e. Legendre(n | P) = -1
def non_quad_residual(P):
    for n in range(100):    # 100 is sufficiently large for long long int P
        x = pow(n, (P - 1) // 2, mod=P)
        if x == P - 1: return n


# Square Root of N Modulo P : Tonelli-Shanks Algorithm
def sqrt_mod(N, P, non_quad=None):
    # N is not a quadratic residual
    if legendre(N, P) == -1: return []

    # N is 0 or 1
    if N % P == 0: return [0, 0]
    if N % P == 1: return [1, P - 1]

    # P == 3 mod 4
    if P % 4 == 3:
        r = pow(N, (P + 1) // 4, mod=P)
        return sorted([r, P - r])

    # P == 1 mod 4 (General Case)
    D, S = P - 1, 0
    while not (D & 1):
        D >>= 1; S += 1
    
    if non_quad is None:
        non_quad = non_quad_residual(P)
    z = pow(non_quad, D, mod=P)

    b_list = [z]
    for _ in range(S - 1):
        b_list.append((b_list[-1] * b_list[-1]) % P)

    t = pow(N, D, mod=P)
    r = pow(N, (D + 1) // 2, mod=P)
    while t != 1:
        tmp, k = t, 1
        for j in range(1, S):
            tmp = (tmp * tmp) % P
            if tmp == 1: k = j; break
        
        b = b_list[S - 1 - k]

        t = (t * b) % P
        t = (t * b) % P
        r = (r * b) % P

    return sorted([r, P - r])

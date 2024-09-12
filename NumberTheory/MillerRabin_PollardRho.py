# =========================== #
# Miller-Rabin Primality Test #
# Pollard-Rho Factorization   #
# =========================== #
import sys, math, random, itertools
input = sys.stdin.readline

# Greatest Common Divisor
def gcd(x, y):
    x, y = abs(x), abs(y)
    if x < y: x, y = y, x
    while y > 0: x, y = y, x % y
    
    return x

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

# Miller Rabin Primality Test
def miller_rabin(N, a):
    # n should be odd
    # Returns True if n is a probable prime
    d, s = N - 1, 0
    while d & 1 == 0:
        d >>= 1; s += 1

    x = pow(a, d, mod=N)
    if x == 1 or x == N - 1: return True

    for _ in range(s - 1):
        x = (x * x) % N
        if x == N - 1: return True
    
    return False


A_LIST_INT16  = [2, 7, 61]
A_LIST_INT128 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 33, 37, 41, 43, 47]

def is_prime(N, a_list=A_LIST_INT128):
    if N == 1: return False
    for a in a_list:
        if N == a: return True
        if N % a == 0: return False
        if not miller_rabin(N, a): return False
    return True

# Pollard-Rho Algorithm for Factorization (Non-Recursive)
def pollard_rho(N):
    if is_prime(N): return N
    if N == 1: return 1
    if N % 2 == 0: return 2

    visited = {}
    while True:
        # Select Random (x, c)
        x = random.randrange(2, N)
        c = random.randrange(1, N)

        if visited.get((x, c)): continue
        else: visited[x, c] = True

        # Floyd's Cycle Detection
        y, d = x, 1
        while d == 1:
            x = (x * x + c) % N
            y = (y * y + c) % N
            y = (y * y + c) % N
            d = gcd(abs(x - y), N)

        # Update N & (prn) Repeat
        if is_prime(d): return d
        else: N = d; continue

def factorize(N):
    factor_dict = {}
    while N > 1:
        p = pollard_rho(N)
        
        factor_dict[p] = 0
        while N % p == 0:
            factor_dict[p] += 1
            N //= p

    return factor_dict

def phi(N):
    res = N
    while N > 1:
        p = pollard_rho(N)
        res = (res // p) * (p - 1)
        while N % p == 0: N //= p

    return res

def divisor_list(N):
    factor_dict = factorize(N)
    p_list = [p for p in factor_dict.keys()]
    e_list = [list(range(factor_dict[p] + 1)) for p in p_list]

    res = []
    for e_sample in list(itertools.product(*e_list)):
        tmp = 1
        for p, e in zip(p_list, e_sample):
            tmp *= (p ** e)
        res.append(tmp)

    return sorted(res)

# =========== #
# Sample Code #
# =========== #
N = (10**9 + 7) * (10**9 + 9)
factor_dict = factorize(N)
for p in sorted(factor_dict.keys()):
    print(f'{p} : {factor_dict[p]}')

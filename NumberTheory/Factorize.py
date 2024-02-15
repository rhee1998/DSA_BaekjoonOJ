# ============= #
# Factorization #
# ============= #
import sys, math

def Factorize(x, primes=None):
    # ==================================================
    # Input(s)
    # - x      : number to factorize
    # - primes : list of primes
    # 
    # Output(s)
    # - res    : dictionary with primes as keys and their factors as values
    # ==================================================
    if primes is None:
        # PrimeList is included in Sieve.py
        primes = PrimeList(math.ceil(math.sqrt(x)))

    res = {}
    for p in primes:
        if p * p > x:
            if x > 1:
                res[x] = 1
            break

        while x % p == 0:
            x //= p
            try: res[p] += 1
            except: res[p] = 1
    
    return res

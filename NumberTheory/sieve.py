# ===================== #
# Sieve of Eratosthenes #
# ===================== #

def Sieve(N):
    # ==================================================
    # Input(s)
    # - N        : maximum number to study primality
    #
    # Output(s)
    # - is_prime : is_prime[idx] = 1 if idx is prime, otherwise 0
    # ==================================================
    is_prime = [0, 0] + [1] * (N - 1)
    
    for i in range(2, N + 1):
        if is_prime[i] == 1:
            for j in range(i * 2, N + 1, i):
                is_prime[j] = 0

    return is_prime

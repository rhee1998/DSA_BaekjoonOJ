# =============== #
# Extended Euclid #
# =============== #
import sys, math

# Find Solution for ax + by = g(a, b)
def diophantine_special(a, b):
    assert a != 0 and b != 0

    sgn_x = 1 if a > 0 else -1
    sgn_y = 1 if b > 0 else -1
    
    a, b, swap = abs(a), abs(b), a < b
    if swap: a, b = b, a

    sol = [[1, 0], [0, 1]]
    while True:
        q, r = a // b, a % b
        if r == 0: g = b; break

        sol.append([
            sol[-2][0] - q * sol[-1][0],
            sol[-2][1] - q * sol[-1][1]
        ])

        a, b = b, r

    x, y = sol[-1]
    if swap: x, y = y, x
    return g, (x * sgn_x, y * sgn_y)

diophantine_special(6, 15)      # (3, (-2, 1))

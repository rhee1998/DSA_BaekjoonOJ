# =========================== #
# Greatest Common Denominator #
# =========================== #

def GCD(x, y):
    x, y = abs(x), abs(y)
    if x < y:
        x, y = y, x
    
    while y > 0:
        x, y = y, x % y
    
    return x

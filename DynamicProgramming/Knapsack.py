############################
##### Knapsack Problem #####
############################

def Knapsack(WMAX, W, V):
    # --------------------------------------------------
    # Input(s)
    # - WMAX (int) : maximum allowed total weight
    # - W (list) : [0] + list of weights
    # - V (list) : [0] + list of values
    # Output(s) : maximum total value
    # --------------------------------------------------
    prev = [0 for _ in range(WMAX + 1)]
    curr = [0 for _ in range(WMAX + 1)]
    for i in range(1, len(W)):
        for wmax in range(WMAX + 1):
            if W[i] > wmax:
                curr[wmax] = prev[wmax]
            else:
                curr[wmax] = max([prev[wmax], prev[wmax - W[i]] + V[i]])

        prev, curr = curr, [0 for _ in range(WMAX + 1)]
    return prev[-1]

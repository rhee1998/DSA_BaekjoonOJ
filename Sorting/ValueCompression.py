# ================= #
# Value Compression #
# ================= #

def CompareValues(a, b):
    return a < b

# Coordinate compression
def Compress(A):
    # Values in A should be unique
    X = GeneralizedMergeSort(A, CompareValues)
    dict_ = {x: j for j, x in enumerate(X)}
    A = [dict_[x] for x in A]

    return A, dict_

# Example
A = [1, 3, 9, 7, 5]
B, dict_ = Compress(A)

print(B)        # [0, 1, 4, 3, 2]
print(dict_)    # {1: 0, 3: 1, 5: 2, 7: 3, 9: 4}

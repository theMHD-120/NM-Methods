import time
import numpy as np

"""
|| in the name of ALLAH ||
the Homework 2, Question 8, Numerical Methods
<<< LU Factorization method for linear equations >>>
seyed mahdi mahdavi mortazavi
stdNo: 40030490
"""

t1 = time.time()


def ForwardHubstitution(Lower, B):
    n = len(B)
    Y = np.zeros(n)
    for i in range(n):
        sum = np.sum(Lower[i, :i] * Y[:i])
        Y[i] = (B[i] - sum) / Lower[i, i]
    return Y


def BackwardSubstitution(Upper, Y):
    n = len(Y)
    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        summ = np.sum(Upper[i, i + 1:] * X[i + 1:])
        X[i] = (Y[i] - summ) / Upper[i, i]
    return X


def LUFactorizationMethod(CoMatrix, Vector):
    n = len(CoMatrix)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    # ---------------------------
    for i in range(n):  # Upper Triangular
        for k in range(i, n):
            summation = np.sum(L[i, :i] * U[:i, k])
            U[i, k] = CoMatrix[i][k] - summation
            # ---------------------------
            for k in range(i, n):
                if i == k:
                    L[i, i] = 1
                else:
                    summation = np.sum(L[k, :i] * U[:i, i])
                    L[k, i] = (CoMatrix[k][i] - summation) / U[i, i]
    # ---------------------------
    Y = ForwardHubstitution(L, Vector)
    result_vec = BackwardSubstitution(U, Y)
    return result_vec  # returns the result vector


# --------------------- General Part ---------------------
CoeMatrix: list = [[2, -1, 1], [3, 3, 9], [3, 3, 5]]  # Matrix of Coefficient;
VecMatrix: list = [-1, 0, 4]                          # Matrix of Vectors;
# ---------------------------
print("---------- <<< With LU Factorization Method >>> ----------")
result = LUFactorizationMethod(CoeMatrix, VecMatrix)
len_of_res = len(result)
for i in range(len_of_res):
    print(f"X{i} is: {result[i]};")

print('-------------------------------------------------------------------')
t2 = time.time()
print('Total execution time is: ', t2 - t1)
print("The END;")
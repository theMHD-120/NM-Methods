import time

"""
|| in the name of ALLAH ||
the coding quiz 3 from chapter 6, numerical methods
<<< implementing Linear equations with Gaussian method >>>
seyed mahdi mahdavi mortazavi
stdNo: 40030490
"""

t1 = time.time()
x_list = []  # a list that includes X1 to Xn


def GaussianMethod(matrix):
    matrix_len = len(matrix)
    len_of_rows = len(matrix[0])  # length of the rows of matrix;
    # ---------------------------
    for i in range(1, matrix_len):
        for k in range(i, len(matrix)):
            curr_row = matrix[k]
            pre_row = matrix[i - 1]
            coefficient = -1 * (curr_row[i - 1] / pre_row[i - 1])

            for j in range(len_of_rows):
                curr_row[j] += pre_row[j] * coefficient
    # ---------------------------
    for i in range(matrix_len):
        matrix[i] = matrix[i][-1::-1]
    # ---------------------------
    for i in range(1, matrix_len + 1):
        row = matrix[matrix_len - i]
        for j in range(len(x_list)):
            row[j + 1] *= x_list[j]
            row[0] -= row[j + 1]
            row[j + 1] = row[j + 2]
        if row[1] != 0:
            x_list.append(row[0] / row[1])


theMatrix = [[1, 1, 1, 0], [1, 2, 4, -1], [1, 3, 9, 2]]
GaussianMethod(theMatrix)
x_list_len = len(x_list)
for i in range(1, x_list_len + 1):
    print(f"The X{i} is: ", x_list[x_list_len - i])

t2 = time.time()
print("The total execution time is: ", t2 - t1)
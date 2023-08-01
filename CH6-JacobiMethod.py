import time

"""
|| in the name of ALLAH ||
the coding quiz 3 from chapter 6, numerical methods
<<< implementing Linear equations with Jacobi method >>>
seyed mahdi mahdavi mortazavi
stdNo: 40030490

Note: this code is only works for 3*3 matrices; 
You can change my algorithm to improve that.
"""

t1 = time.time()


def JacobiMethod(n: int, tole: float, theMatrix: list, start_point: tuple, end_point: tuple):
    Xn = start_point[0]
    Yn = start_point[1]
    Zn = start_point[2]
    while (abs(Xn - end_point[0]) > tole) and (abs(Yn - end_point[1]) > tole) and (abs(Zn - end_point[2]) > tole):
        print(Xn - end_point[0])
        Xn_temp = (1 / theMatrix[0][0]) * (theMatrix[0][3] - theMatrix[0][1] * Yn - theMatrix[0][2] * Zn)
        Yn_temp = (1 / theMatrix[1][1]) * (theMatrix[1][3] - theMatrix[1][0] * Xn - theMatrix[1][2] * Zn)
        Zn_temp = (1 / theMatrix[2][2]) * (theMatrix[2][3] - theMatrix[2][0] * Xn - theMatrix[2][1] * Yn)
        Xn = Xn_temp
        Yn = Yn_temp
        Zn = Zn_temp
    return Xn, Yn, Zn


equation_matrix = [[1, 3, -6, -11], [8, -2, 1, 7], [-2, 5, 1, 11]]
print(JacobiMethod(5, 0.01, equation_matrix, (0, 0, 0), (1, 2, 3)))

t2 = time.time()
print(f"The total execution time is: {t2 - t1} seconds;")
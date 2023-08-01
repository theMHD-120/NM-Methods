import pandas as pd

"""
|| in the name of ALLAH ||
the Question 11 from Homework 1 (HW1) --- Chapter 3
<<< implementing a natural cubic spline interpolator >>>
seyed mahdi mahdavi mortazavi
stdNo: 40030490
"""


def get_points_as_number(points_list):
    list_of_points = []
    # ------------------------
    for point_list in points_list:
        if type(point_list[0]) == str:
            point_str = str(point_list[0])
            point_str = point_str[1:len(point_str) - 1]
            list_of_points.append(tuple(map(float, point_str.split(','))))
    # ------------------------
    return list_of_points


def get_two_dimesional_matrix(n_points, the_matrix):
    index = 0
    two_dimesional_matrix = []
    # ------------------------
    for k in range(n_points):
        row = the_matrix[index: index + n_points]
        two_dimesional_matrix.append(row)
        index += n_points
    # ------------------------
    return two_dimesional_matrix


def get_inverse_of_matrix(matrix):
    matrix_len = len(matrix)
    identity_matrix = [[0.0] * matrix_len for _ in range(matrix_len)]
    # ------------------------
    for i in range(matrix_len):
        identity_matrix[i][i] = 1.0
    # ------------------------
    matrix_to_inverse = [row[::] + identity_matrix[i] for i, row in enumerate(matrix)]
    for i in range(matrix_len):
        pivot = matrix_to_inverse[i][i]
        # ........................
        for j in range(matrix_len * 2):
            matrix_to_inverse[i][j] /= pivot
        # ........................
        for k in range(matrix_len):
            if k != i:
                factor = matrix_to_inverse[k][i]
                for j in range(matrix_len * 2):
                    matrix_to_inverse[k][j] -= factor * matrix_to_inverse[i][j]
    # ------------------------
    return [row[matrix_len:] for row in matrix_to_inverse]


def FindMjs(the_points_list):
    number_of_points = len(the_points_list)
    list_of_mjs = [0]  # [m0, m1, m2, ..., mn] and m0 = mn = 0;
    # ------------------------
    left_zeros = 0
    right_zeros = number_of_points - 3
    #  the 2 top variables are for coefficients_matrix;
    # ------------------------
    if number_of_points > 2:
        unknowns_matrix = [0]
        information_matrix = [0]
        coefficients_matrix = [2]
        for n in range(number_of_points - 1):
            coefficients_matrix.append(0)
        # ........................
        for j in range(1, number_of_points - 1):
            yj = the_points_list[j][1]
            yjmin = the_points_list[j - 1][1]  # yjmin = yj minus: y(j - 1)
            yjplus = the_points_list[j + 1][1]  # yjplus : y(j + 1)
            hj = (the_points_list[j][0] - the_points_list[j - 1][0])  # hj = xj - x(j-1)
            hjplus = (the_points_list[j + 1][0] - the_points_list[j][0])  # hjplus: h(i+1) = x(j+1) - xj
            # ........................
            muj = (hj / (hj + hjplus))
            landaj = (hjplus / (hj + hjplus))
            dj = ((6 / (hj + hjplus)) * (((yjplus - yj) / hjplus) - ((yj - yjmin) / hj)))
            # ........................
            unknowns_matrix.append(f'm{j}')
            information_matrix.append(dj)
            for i in range(left_zeros):
                coefficients_matrix.append(0)
            coefficients_matrix.append(muj)
            coefficients_matrix.append(2)
            coefficients_matrix.append(landaj)
            for i in range(right_zeros):
                coefficients_matrix.append(0)
            right_zeros -= 1
            left_zeros += 1
        # ........................
        unknowns_matrix.append(0)
        information_matrix.append(0)
        for n in range(number_of_points - 1):
            coefficients_matrix.append(0)
        coefficients_matrix.append(2)
        # ------------------------
        two_dimesional_coefficients = get_two_dimesional_matrix(number_of_points, coefficients_matrix)
        inverse_of_coefficients = get_inverse_of_matrix(two_dimesional_coefficients)
        for i in range(1, number_of_points - 1):
            for j in range(1, number_of_points - 1):
                the_mj = inverse_of_coefficients[i][j] * information_matrix[i]
                list_of_mjs.append(the_mj)
    # ------------------------
    list_of_mjs.append(0)
    return list_of_mjs


def CubicSplineInterpolator(x: float, points_list: list):
    interpolation_res = 0  # Sj(x)
    mj_list = FindMjs(points_list)  # to find Mj for cubic spline formula (with solving matrix);
    # ------------------------
    for j in range(len(points_list) - 1):
        mj = mj_list[j]
        xj = points_list[j][0]
        yj = points_list[j][0]
        mjplus = mj_list[j + 1]  # mjplus: m(j+1)
        yjplus = points_list[j + 1][1]  # yjplus: y(j+1)
        hjplus = (points_list[j + 1][0] - xj)  # hjplus: h(i+1)
        interpolation_res += (yj + ((((yjplus - yj) / hjplus) - (((2 * mj) + mjplus) / 6) * hjplus) * (x - xj)) + (
                    (mj / 2) * ((x - xj) ** 2)) + (((mjplus - mj) / (6 * hjplus)) * ((x - xj) ** 3)))
    # ------------------------
    return interpolation_res


for i in range(5):
    list_of_points_as_list = []
    col_of_numbers = pd.read_csv('q11BenchMark.csv', usecols=['number'])
    number = float(col_of_numbers.values[i])
    p1_col = pd.read_csv('q11BenchMark.csv', usecols=['p1'])
    list_of_points_as_list.append(list(p1_col.values[i]))
    p2_col = pd.read_csv('q11BenchMark.csv', usecols=['p2'])
    list_of_points_as_list.append(list(p2_col.values[i]))
    p3_col = pd.read_csv('q11BenchMark.csv', usecols=['p3'])
    list_of_points_as_list.append(list(p3_col.values[i]))
    p4_col = pd.read_csv('q11BenchMark.csv', usecols=['p4'])
    list_of_points_as_list.append(list(p4_col.values[i]))
    # ------------------------
    list_of_points = get_points_as_number(list_of_points_as_list)
    result = CubicSplineInterpolator(number, list_of_points)
    # ------------------------
    print(f"< ------------------------------ Group point {i + 1} ------------------------------ >")
    print(f"Interpolation result of group points {i + 1} is < {result} >;")
    input("Press enter to continue...")
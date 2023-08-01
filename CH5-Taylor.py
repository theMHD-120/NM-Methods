import math as mt
import sympy as sp

"""
Chapter 5:
The taylor method for differential equations
...
Note: this code is doesn't work correctly; 
You can debug my algorithm.
"""

x_list = []  # a list that contains the X0 to Xn
y_list = []  # a list that contains the Y0 to Yn


def Kth_deriva(func, k_th, index):  # to get the k-th derivative of a function;
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    xy_func_str = sp.expand(func, (x, y))
    # ---------------------------
    for i in range(k_th):
        deriva_x = sp.diff(xy_func_str, x)
        deriva_y = sp.diff(xy_func_str, y) * xy_func_str
        # deriva_y = str(deriva_y).replace(str(deriva_y), str(xy_func_str))
        xy_func_str = str(deriva_x) + '+' + str(deriva_y)
        xy_func_str = sp.expand(xy_func_str, (x, y))
        print(xy_func_str)
    y_func_str = xy_func_str.subs(x, x_list[index])
    return y_func_str.subs(y, y_list[index])


def Taylor(k, n, l, u, f):
    h = (u - l) / n
    for i in range(1, n + 1):
        y_list.append(y_list[i - 1])
        for j in range(1, k + 1):
            y_list[i] += ((h ** k) / mt.factorial(k)) * Kth_deriva(f, j - 1, i - 1)
        x_list.append(x_list[i - 1] + h)


num_of_points = int(input('Enter number of points: '))
order = int(input("Enter the order of Taylor: "))
lower_bound = float(input('Enter lower bound: '))
upper_bound = float(input('Enter upper bound: '))
the_first_y = float(input('Enter Y0: '))
funct = input("Enter the function: ")
# ---------------------------
x_list.append(lower_bound)
y_list.append(the_first_y)
Taylor(order, num_of_points, lower_bound, upper_bound, funct)
print(x_list)
print(y_list)

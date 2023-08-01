import sympy as sp
import matplotlib.pyplot as plt
"""
A guide file for using numerical analysis python methods and functions.
"""

"""
|| in the name of ALLAH ||
<<< Name of algorithm or project >>>
Name (Nickname or Fullname) of developer 
some public Specification about developer (such as student number or ...)
"""

# Using .isalnum method for a list
theList = ['a', 'A', '2', '34']
for i in theList:
    if i.isalnum():
        print("yes!")
# ---------------------------

# A GOLDEN POINT WITH SYMPY !!!!!
# GET FUNCTION WITH INPUT !!!!!
f = input()
x0 = float(input())
x = sp.Symbol('x')
first_derv = sp.diff(f, x)  # gives a string that includes the first derivative of the function.
print(first_derv.subs(x, x0))  # prints the count of first derivative of the function in x == x0.

x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x, y)
plt.show()
# ---------------------------

'''
differential:
    expand for f with two variables (x, y)
    xy_func_str = sp.expand(f, (x, y))
    y_func_str = xy_func_str.subs(x, 2)
    funct_count = y_func_str.subs(y, 3)
    
random:
    point = round(uniform(0, 2), 4)
    
time:
    t1 = time.time()
    t2 = time.time()
    total_time = t2 - t1

the MATRIXXes:
-calculate determinant:
    x_list = [[1,2],[4,5]]
    m = sp.Matrix(x_list)
    print(sp.det(m))
'''
import math as mt
import pandas as pd

"""
|| in the name of ALLAH ||
the Question 12 from Homework 1 (HW1) --- Chapter 2
<<< implementing Secant's method for non-linear equations >>>
seyed mahdi mahdavi mortazavi
stdNo: 40030490
"""


def Derivative(f, row: int, lowb: float, uppb: float):
    derivative = (f(row, uppb) - f(row, lowb)) / (uppb - lowb)
    return derivative


def SecantMethod(func, row_num: int, lowerb: float, upperb: float, tole: float):
    step = 1
    prev_res = 0  # reached result (x) in previous step;
    # -----------------------
    while True:
        x = upperb - (func(row_num, upperb) / Derivative(func, row_num, lowerb, upperb))
        print(f"Step {step}: x = {x} ||| y = {func(row_num, x)}")
        if abs(x - prev_res) <= tole:
            return x
        # .......................
        prev_res = x
        lowerb, upperb = upperb, x
        step += 1


def Function(row: int, x: float):
    res = 0
    all_datas = pd.read_csv('q12BenchMark.csv')
    # -----------------------
    for col in all_datas.columns:
        column = pd.read_csv('q12BenchMark.csv', usecols=[col])
        coefficient = float(column.values[row])
        # .......................
        if col == 'x3':
            res += coefficient * (x ** 3)
        elif col == 'x2':
            res += coefficient * (x ** 2)
        elif col == 'x1':
            res += coefficient * x
        elif col == 'bias':
            res += coefficient
        elif col == 'ex':
            res += coefficient * mt.exp(x)
        elif col == 'cosx':
            res += coefficient * mt.cos(x)
        elif col == 'sinx':
            res += coefficient * mt.sin(x)
        else:
            return res


for i in range(5):
    lb_list = pd.read_csv('q12BenchMark.csv', usecols=['LB'])
    lb = float(lb_list.values[i])
    ub_list = pd.read_csv('q12BenchMark.csv', usecols=['UB'])
    ub = float(ub_list.values[i])
    tol_list = pd.read_csv('q12BenchMark.csv', usecols=['TOL'])
    tol = float(tol_list.values[i])
    # -----------------------
    print(f"< ------------------------------ Equation {i + 1} ------------------------------ >")
    root = SecantMethod(Function, i, lb, ub, tol)
    print(f"Root of equation {i + 1} is < {root} >;")
    input("Press enter to continue...")
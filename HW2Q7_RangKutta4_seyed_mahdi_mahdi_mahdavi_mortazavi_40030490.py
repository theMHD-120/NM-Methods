import time
import math as mt
import matplotlib.pyplot as plt

"""
|| in the name of ALLAH ||
the Homework 2, Question 7, Chapter5, Numerical Methods
<<< implementing Rung Kutta method for differential equations >>>
seyed mahdi mahdavi mortazavi
stdNo: 40030490
"""

t1 = time.time()

t_list = []  # a list that contains the t0 to Xn
y_list = []  # a list that contains the Y0 to Yn


def RangKutta(f, upb, lowb, h):
    num_of_points = int((upb - lowb) / h)
    # ---------------------------
    for i in range(num_of_points):
        k1 = h * f(t_list[i], y_list[i])
        k2 = h * f(t_list[i] + h / 2, y_list[i] + k1 / 2)
        k3 = h * f(t_list[i] + h / 2, y_list[i] + k2 / 2)
        k4 = h * f(t_list[i] + h, y_list[i] + k3)
        t_list.append(t_list[i] + h)
        y_list.append(y_list[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)


print("----------- <<< For the equation 1 of question 3 >>> -----------")
lower_bound = float(input('Enter lower bound: '))
upper_bound = float(input('Enter upper bound: '))
the_first_y = float(input('Enter Y0: '))  # Y0
h_height = float(input('Enter the h: '))
# ---------------------------
funct = lambda t, y: (t * mt.e ** (3 * t)) - 2 * y
t_list.append(lower_bound)
y_list.append(the_first_y)
RangKutta(funct, upper_bound, lower_bound, h_height)
print("For equation 1 of question 3 ...")
for i in range(len(t_list)):
    print(f"X{i} = {t_list[i]} ||| Y{i} = {y_list[i]};")
plt.plot(t_list, y_list, color='r')
plt.show()
input("Enter to continue...")


print("----------- <<< For the equation 2 of question 3 >>> -----------")
lower_bound = float(input('Enter lower bound: '))
upper_bound = float(input('Enter upper bound: '))
the_first_y = float(input('Enter Y0: '))  # Y0
h_height = float(input('Enter the h: '))
t_list = []
y_list = []
# ---------------------------
funct = lambda t, y: mt.e ** (t - y)
t_list.append(lower_bound)
y_list.append(the_first_y)
RangKutta(funct, upper_bound, lower_bound, h_height)
print("For equation 2 of question 3 ...")
for i in range(len(t_list)):
    print(f"X{i} = {t_list[i]} ||| Y{i} = {y_list[i]};")
plt.plot(t_list, y_list, color='r')
plt.show()
input("Enter to continue...")


print("----------- <<< For the equation 3 of question 3 >>> -----------")
lower_bound = float(input('Enter lower bound: '))
upper_bound = float(input('Enter upper bound: '))
the_first_y = float(input('Enter Y0: '))  # Y0
h_height = float(input('Enter the h: '))
t_list = []
y_list = []
# ---------------------------
funct = lambda t, y: (1 + t) / (1 + y)
t_list.append(lower_bound)
y_list.append(the_first_y)
RangKutta(funct, upper_bound, lower_bound, h_height)
print("For equation 3 of question 3 ...")
for i in range(len(t_list)):
    print(f"X{i} = {t_list[i]} ||| Y{i} = {y_list[i]};")
plt.plot(t_list, y_list, color='r')
plt.show()

print('-------------------------------------------------------------------')
t2 = time.time()
print('Total execution time is: ', t2 - t1)
print("The END;")
"""
https://www.bragitoff.com/2019/08/non-linear-curve-fitting-using-python/
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def fitting(x, a, b):
    return a * np.exp(b * x)


x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([1, 9, 50, 300, 1500])

plt.plot(x_data, y_data, 'bo', label='experimental-data')

initial_guess = [1.0, 1.0]

popt, pcov = curve_fit(fitting, x_data, y_data, initial_guess)
print(popt)

x_fit = np.arange(.0, 5.0, .01)

plt.plot(x_fit,
         fitting(x_fit, *popt),
         'r',
         label='fit params: a=%5.3f, b=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

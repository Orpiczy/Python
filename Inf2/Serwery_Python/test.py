from numpy.polynomial import polynomial as poly
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as nla
from scipy import linalg as sla
import numpy.polynomial.chebyshev as cheb

a = [-624, 4, 780, -5, -156, 1]
polynomial = lambda x: x ** 5 - 156 * x ** 4 - 5 * x ** 3 + 780 * x ** 2 + 4 * x - 624
w3_coef = [0] * 6
w3_coef[0] = a[0] + a[2] / 2 + 3 * a[4] / 4
w3_coef[1] = a[1] + 3 * a[3] / 4 + 5 * a[5] / 8
w3_coef[2] = a[2] / 2 + 3 * a[4] / 4
w3_coef[3] = a[3] / 4 + 5 * a[5] / 16
w3_coef[4] = a[4] / 8
w3_coef[5] = a[5] / 16

w3_coef_inv = [0] * 6
for count, elem in enumeration(w3_coef):
    w3_coef_inv[count] = w3_coef[-1 - count]

cheb_roots = cheb.chebroots(np.array(w3_coef).T)
cheb_roots_disparity = sum(abs(np.array([polynomial(elem) for elem in cheb_roots])))

print(cheb_roots)
print(np.array(w3_coef).T)

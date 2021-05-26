#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as nplin
from copy import deepcopy

m = 50
n = 12

t_ar = np.array(np.linspace(0, 1, 50))
t = t_ar.reshape(50, 1)
b = np.cos(np.multiply(t, 4))
A = np.vander(t_ar)
A = np.fliplr(A)
At = np.transpose(A)
x_1 = np.linalg.solve(At @ A, np.dot(At, b))
x_2 = np.linalg.lstsq(A, b, rcond=-1)[0]

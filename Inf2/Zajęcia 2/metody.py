#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import numpy.linalg as nplin

m = 5
A = {}
b = {}
x = {}
cond_A = {}
res_x = {}
m_val = [10, 20, 50, 100, 1000]
for m in m_val:
    A[m] = np.random.randint(1, 20, size=(m, m))
    b[m] = np.random.randint(1, 20, size=(m, 1))
    x[m] = np.linalg.solve(A[m], b[m])
    res_x[m] = np.linalg.norm(b[m] - np.dot(A[m], x[m]))
    cond_A[m] = np.linalg.cond(A[m])

U, S, V = nplin.svd(A[10])


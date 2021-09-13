# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:07:32 2021

@author: erina
"""
# 最適なパラメータWを求める
# W = (XtX) **-1 Xty
import numpy as np
X = np.array([
    [1, 2, 3],
    [1, 2, 5],
    [1, 3, 4],
    [1, 5, 9]
    ])
y = np.array([
    [1],
    [5],
    [6],
    [8]
    ])

Xt = X.T
XtX = np.dot(Xt, X)
XtX_inv = np.linalg.inv(XtX)
Xty = np.dot(Xt, y)
W = np.dot(XtX_inv, Xty)
print(W)
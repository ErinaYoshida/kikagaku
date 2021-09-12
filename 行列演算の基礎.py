# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:46:29 2021

@author: erina
"""

import numpy as np

# ベクトルの定義
x = np.array([[1], [2], [3]])
#print(x.shape)  # (3, 1):3行1列のベクトル

# 行列の定義
X = np.array([[1, 2], [3, 4]])

# 転置
Xt = X.T

# 逆行列
X_inv = np.linalg.inv(X)

# 行列積
XX_inv = np.dot(X, X_inv)

# n行m列を変数に格納
B = np.array([[1, 2, 3], [2, 3, 4]])  # 2行3列
row, col = B.shape  # row=2, col=3

# 行ごとに処理したいときの例
for b in B:
    print(b)
    print("-----")
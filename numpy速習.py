# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 20:46:11 2021

@author: erina
"""
# 単回帰分析　部屋の広さxから家賃ｙの予測
# y = ax + b をモデルとしてデータを中心化し、最適なパラメータaを求める
import numpy as np

# ベクトルの定義は[[]]で。[]では転置で変になる
x = np.array([[1, 2, 3]])
y = np.array([[2, 3.9, 6.1]])

# データの中心化。.mean()で平均を求めて引く
xc = x - x.mean()
yc = y - y.mean()

# 要素積を求める
xx = xc * xc
xy = xc * yc

# 最適なパラメータaの出力。.sum()で合計
print(xy.sum() / xx.sum())
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 15:29:53 2021

@author: erina
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample.csv")

# 代表的な統計値を取得
#print(df.describe())

# データの中心化
df_c = df - df.mean()
#print(df_c.describe())

x = df_c["x"]
y = df_c["y"]

#plt.scatter(x,y)

# 最適なパラメータaを求める
xx = x * x
xy = x * y
a = xy.sum() / xx.sum()


# 散布図の表示
plt.scatter(x, y, label="y")  # 実測値
# 直線を引く
plt.plot(x, x*a, c="red", label="y_hat")  # 予測値
# 凡例の表示
plt.legend()

# 40平米の家賃はいくらか予測
# y - y.mean() = a(x - x.mean()) ⇒ y = a(x - x.mean()) + y.mean()
x_new = 40
mean = df.mean()
xc_new = x_new - mean["x"]

yc = a * xc_new
y_hat = yc + mean["y"]
print(y_hat)

# 部屋の広さから家賃を予測する関数を定義
def predict(x):
    # 定数項(本来ならここもデータから算出させる)
    a = 10069.022519284063
    xm = 37.622220
    ym = 121065.0
    # データの中心化
    xc = x - xm
    # 予測
    y_hat = a * xc + ym
    return y_hat

print(predict(40))

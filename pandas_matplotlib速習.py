# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:19:02 2021

@author: erina
"""

import pandas as pd
df = pd.read_csv("sample.csv")  # df:DataFrame 行と列が複数あるデータ型

# 先頭から~行表示
print(df.head())  # デフォルトでは5行(0~4行)表示
print(df.head(3))  #先頭から3行表示

# 後ろから~行表示
print(df.tail())  # デフォルトでは5行(95~99行)表示
print(df.tail(3))  # 後ろから3行表示

# 行で区切って表示
print(df[:4])  # スライスと同じ

# .iloc[行, 列]
print(df.iloc[:10, 0])

# カラム名を指定して取得
x = df["x"]  # x, yはSeries型(1列) Serisesが集まるとdf
y = df["y"]


import matplotlib.pyplot as plt
# 散布図(scatter)
plt.scatter(x, y, c="green")  # c="色"で色を指定
#plt.show  # グラフの表示

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(1, 2, 1)  # 1×2のキャンバスを広げて1区画目を使う
ax.scatter(x, y)
# タイトルを挿入
ax.set_title("abc")
# x軸のラベルを挿入
ax.set_xlabel("あいう", fontname="MS Gothic")  #日本語対応のフォントを指定しないと豆腐になる
# y軸のラベルを挿入
ax.set_ylabel("y")

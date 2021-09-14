# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 22:41:24 2021

@author: erina
"""

import numpy as np
import pandas as pd

### 1 データの読み込み

# CSVファイルを読み込み
df = pd.read_csv("/content/housing.csv")
# .infoでDataFrameの情報を確認 ※non-null:欠損値がない
df.info()
df.describe()

### 2 データの確認

import seaborn as sns
# x1をヒストグラムで可視化
sns.distplot(df["x1"], bins=10)  # bins=で幅の調整
sns.set()  # 目盛の表示

# 相関係数の算出 ※どのxがyと相関がありそうか見る 0:全く相関がない 1:正の相関 2:負の相関
df.corr()

# df全てを可視化
#sns.pairplot(df)
# yとx6に正の相関、x13に負の相関がありそう
# 実際はもっと細かく確認してからモデルつくる

### 3 入力変数と出力変数の切り分け

df.head(3)

# .iloc[行, 列]
# x
df.iloc[:, :-1]

# y
df.iloc[:, -1]

df["y"]

# .drop("カラム名", axis=0)  行方向にカラム名を削除　axis=1なら列方向
#x
df.drop("y", axis=1)

### 4 モデル構築と検証

x = df.drop("y", axis=1)
t = df["y"]

from sklearn.linear_model import LinearRegression
# モデルの宣言(インスタンス化)
model = LinearRegression()
# 学習
model.fit(x, t)

# 検証
model.score(x, t)  # データの分布に対してどれくらい当てはまりの良いモデルか
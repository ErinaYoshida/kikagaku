import numpy as np
import sklearn
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

# scikit-learnで実装
from sklearn.linear_model import LinearRegression

# モデルの宣言(インスタンス化)
model = LinearRegression(fit_intercept=False)
# fit_intercept=Falseで切片の計算を有りに変更している

#  モデルの学習(パラメータの調整)
model.fit(X, y)

# 調整後のパラメータの確認
model.coef_

# 予測精度の確認(決定係数1に近いほど良い 0 ~ 1 ※負の値をとることもある)
model.score(X, y)

# 新しいデータxを定義
x_new = np.array([[1, 3, 6]])

# yの予測値y_predを求める
y_pred = model.predict(x_new)

# .fitで学習 ⇒ .scoreで精度の確認 ⇒ .predictで予測
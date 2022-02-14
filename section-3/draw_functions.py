import numpy as np  # NumPyの導入。以降npという名前でNumPyを使用できる。
import matplotlib.pyplot as plt
a = [0, 1, 2, 3, 4, 5]
b = np.array(a)  # リストからNumPyの配列を作る
print(b) 

x = np.linspace(-5, 5)  # -5から5まで50に区切る
print(x)
print(len(x))  # xの要素数


x = np.linspace(-5, 5)  # -5から5まで
y = 2*x + 1  # xに2をかけて1を足しy座標とする
plt.plot(x, y)  # x、yをプロット
plt.show()  # グラフの表示

# ーーーーーーーーーーーーーーーーーーーーーー

x =  np.linspace(-3, 3)   # xの範囲を指定
y_1 = 1.5*x  # xに演算を行いy_1とする
y_2 = -2*x + 1  # xに演算を行いy_2とする

# 軸のラベル
plt.xlabel("x value", size=14)
plt.ylabel("y value", size=14)

# グラフのタイトル
plt.title("My Graph")

# グリッドの表示
plt.grid()

# プロット 凡例と線のスタイルを指定
plt.plot(x, y_1, label="y1")
plt.plot(x, y_2, label="y2", linestyle="dashed")
plt.legend() # 凡例を表示

plt.show()

# ーーーーーーーーーーーーーーーーーーーー

x = np.linspace(-4, 4)  # -4から4まで
y_1 = 2*x + 1
y_2 = x**2 - 4
y_3 = 0.5*x**3 - 6*x

plt.plot(x, y_1, label="1st")
plt.plot(x, y_2, label="2nd")
plt.plot(x, y_3, label="3rd")
plt.legend()

plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()
plt.show()
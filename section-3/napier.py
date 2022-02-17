# べき乗とネイピア数
import numpy as np  # NumPyの導入。以降npという名前でNumPyを使用できる
import matplotlib.pyplot as plt

x = np.linspace(-2,2)

y_2 = 2**x
y_3 = 3**x

plt.plot(x,y_2, label="2^x")
plt.plot(x,y_3, label="3^x")
plt.legend()

plt.xlabel("x", size = 14)
plt.xlabel("y", size = 14)
plt.grid()
plt.show()

# --------------------------

x = np.linspace(-2,2)
e = np.e

y_2 = 2**x
y_e = e**x
y_3 = 3**x

plt.plot(x,y_2, label="2^x")
plt.plot(x,y_e, label="e^x")
plt.plot(x,y_3, label="3^x")
plt.legend()

plt.xlabel("x", size = 14)
plt.xlabel("y", size = 14)
plt.grid()
plt.show()

# -----------------------
x = np.linspace(-2, 2)
dx = 0.1  # xの微小な変化
e = np.e  # ネイピア数

y_e = e**x  # 元のべき乗の関数
y_de = (e**(x+dx) - e**x) / dx  # yの微小な変化/xの微小な変化

plt.plot(x, y_e, label="e^x")
plt.plot(x, y_de, label="de")
plt.legend()

plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()
plt.show()


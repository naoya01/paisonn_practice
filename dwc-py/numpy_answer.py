import numpy as np

a = np.arange(15).reshape(3,5)
print(a)
print(a.shape)
print(type(a))
print(a.dtype)

data = np.zeros(8)
data[4] = 1
print(data)

data = np.arange(10,50)
print(data)

data = np.arange(40)
data = data[::-1]
print(data)

l = np.arange(10)
print(l)
print(l[4:8])
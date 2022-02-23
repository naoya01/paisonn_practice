import numpy as np

a = np.arange(15).reshape(3,5)
print(a)
print(a.shape)
print(type(a))
print(a.dtype)

# ---------------------------

data = np.zeros(8)
data[4] = 1
print(data)

# ---------------------------

data = np.arange(10,50)
print(data)

# ---------------------------

data = np.arange(40)
data = data[::-1]
print(data)

# ---------------------------

l = np.arange(10)
print(l)
print(l[4:8])

print(l[-7:-2])

print(l[2:8:2])

# ---------------------------

data = np.arange(9).reshape(3,3)
print(data)

# ---------------------------

data = np.nonzero([1,2,0,0,4,0])
print(data)

# ---------------------------

data = np.eye(3)
print(data)

# ---------------------------

data = np.random.random((3,3,3))
print(data)

# ---------------------------

data = np.random.random((10,10))
datamin, datamax = data.min(),data.max()
print(datamin,datamax)

# ---------------------------

data = np.random.random((10,10))
m = data.mean()
print(m)

# ---------------------------

data = np.ones((10,10))
data[1:-1,1:-1] = 0
print(data)

# ---------------------------

data = np.ones((8,8))
data = np.pad(data, pad_width=1, mode='constant', constant_values=0)
print(data)

# ---------------------------

data = np.diag(1+np.arange(4),k=0)
print(data)

# ---------------------------

data = np.zeros((8,8),dtype=int)
data[1::2,::2] = 1
data[::2,1::2] = 1
print(data)

# ---------------------------

print(np.unravel_index(10,(3,5,2)))

# ---------------------------

data = np.random.random((5,5))
datamax,datamin = data.max(),data.min()
data = (data - datamin)/(datamax - datamin)
print(data)

# ---------------------------

data = np.dot(np.ones((5,3)),np.ones((3,2)))
print(data)

# ---------------------------

data = np.arange(11)
data[(3 < data) & (data <= 8)] *= -1
print(data)

# ---------------------------

data1 = np.random.randint(0,10,10)
data2 = np.random.randint(0,10,10)
print(np.intersect1d(data1,data2))

# ---------------------------

np.emath.sqrt(-1)

# ---------------------------

today = np.datetime64('today','D')
day_after_tomorrow = np.datetime64('today','D') + np.timedelta64(2,'D')
print(today)
print(day_after_tomorrow)

# ---------------------------

data = np.arange('2022-02','2022-03',dtype='datetime64[D]')
print(data)

# ---------------------------

data = np.random.uniform(0,10,10)
print(data)
print(data - data%1)
print(np.floor(data))
print(np.ceil(data)-1)

# ---------------------------
data = np.zeros((5,5))
data += np.arange(5)
print(data)

# ---------------------------

data = np.linspace(0,1,11,endpoint=False)[1:]
print(data)

# ---------------------------
data = np.random.random(10)
data.sort()
print(data)
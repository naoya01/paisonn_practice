array = [0 ,1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
a = array[0]
b = array[1]
c = array[2]
for i in range(3, 100):
  c = a + b
  a = b
  b = c
  if (i == 4):
    print(c)
    break
# -*- coding: utf-8 -*-


# 変数
a = 123
print(a)

b = 123.45
print(b)

c = "こんにちは、Python"
print(c)

dog_name = "Poch"
print(dog_name)


# 四則演算
a = 7
b = 3

c = a + b #足し算
print(c)

d = a - b  # 引き算
print(d)

e = a * b  # 掛け算
print(e)

f = a / b  # 割り算（小数）
print(f)

g = a // b  # 割り算（整数）
print(g)

h = a % b  # 余り
print(h)

a = "Hello"
b = "World"

c = a + b
print(c) #"HelloWorld"


# Bool値
a = True
b = False

print(a)
print(b)

# 比較演算子
c = 3
d = 4

e = c > d  # cがdよりも大きいかどうか
print(e)

f = c < d  # cがdよりも小さいかどうか
print(f)

g = c >= d  # cがd以上かどうか
print(g)

h = c <= d  # cがd以下かどうか
print(h)

i = c == d  # cとdが等しいかどうか
print(i)

j = c != d  # cとdが等しくないか
print(j)

# 論理演算子
a = 3
b = 4
c = 5

d = a < b and b < c  # 両者がTrueであればTrue
print(d)

e = a < b or b > c  # 片方がTrueであればTrue
print(e)

f = not a < b  # Bool値を反転
print(f)
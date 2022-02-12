# -*- coding: utf-8 -*-

a = [2011, 2012, 2013, 2014, 2015]

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

b = 2016
c = [b, 2017, 20.1, "Hello", "Hi"]
print(c[1:4])  # 先頭から1番目以上、4番目未満の範囲

d =[[2012, 2013, 2014], [2015, 2016, 2017]]
print(d[0])

e = ["Py", 543.21, 79, "thon", [2018, 2019, 2020]]
print(e)

# 要素の変更
e[2] = 99
print(e)

# 要素の追加
e.append(2021)
print(e)


a = [2012, 2013, 2014]  # リスト[]
b = (2012, 2013, 2014)  # タプル()

print(a)
print(b)

print(a[1])
print(b[1])

a[1] = 2016
print(a)
# b[1] = 2016  # エラーが発生
# print(b)

a.append(2015)
print(a)
# b.append(2015)  # エラーが発生
# print(b)
# プルの要素を変更したり、タプルに要素を追加しようとするとエラーが発生

# 辞書
a = {"Taro":1985,"Hanako":1986}
print(a["Taro"])

a["Hanako"] = 1987
print(a)

a["Jiro"] = 1989
print(a)


# if文
a = 5
if a == 5:
  print("3+4")
  print(3+4)
else:
  print("3✖️4")
  print(3*4)

b = 4
if b < 3:
  print("Hello")
elif b < 5:
  print("Hi")
else:
  print("Yeah")

time = 20
if time < 12:
    print("Good morning!")
elif time < 17:
    print("Good afternoon!")
elif time < 21:
    print("Good evening!")
else:
    print("Good night!")


# for
a = [2001, 2002, 2003, 2004, 2005]
for i in a:  # iにはリストaの各要素が入る
    print(i + 10)  # 行頭にインデントを入れる

for i in range(0, 6):  # iには0以上6未満の整数が入る
    print(i * 2)

# while
print("--- 10未満 ---")
a = 0
while a < 10:  # aが10未満である間ループ
    print(a)
    a += 1  # aに1を加える

print("--- 10と等しくない ---")
b = 0
while b != 10:  # bが10と等しくない限りループ
    print(b)
    b += 1

# 分岐とループの組み合わせ
a = []  # 空のリスト
for i in range(0, 10):
    if i%2 == 0:  # 偶数であれば
        a.append(i)

print (a)

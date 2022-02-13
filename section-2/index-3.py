# -*- coding: utf-8 -*-

# 関数

def say_hello():
  print("Hello world")

say_hello()

def say_gm():
  print("Good morning")

say_gm()
say_gm()
say_gm()
# 何回も呼び出せる

# 引数
def say_number(a):
  print(a)

say_number(123)

def add(a,b,c):
  d = a + b + c
  print(d)

add(3,4,5)


# 返り血
def get_number():
  a = 123
  return a

b = get_number()
print(b)

def add(a,b):
  c = a + b
  return c

result1 = add(11,2)
print(result1)

result2 = add(1,4)
print(result2)


# 変数のスコープ
glob_1 = 123 #グローバル変数(関数外の変数)

def show_number():
  loc_1 = 456 #ローカル変数(関数内の変数)
  print(glob_1,loc_1)

show_number()


# クラス

class Calc:
  def add(self,a,b): #addメソッド
    print(a +  b)

  def multiply(self, a, b):  #multiplyメソッド
    print(a * b)

cl = Calc()
cl.add(2,3)
cl.multiply(4,5)


class Box:
    def set_number(self, n1, n2):
        self.num1 = n1 # num1がインスタンス変数
        self.num2 = n2
        
bx = Box()
bx.set_number(123, 456)

print(bx.num1)  # インスタンス変数の値を表示
print(bx.num2)

bx.num1 = 999  # 値を変更
print(bx.num1)

class Dog:
    def set_dog(self, n, a):
        self.name = n
        self.age = a
        
dog1 = Dog()
dog1.set_dog("Pochi", 5)

dog2 = Dog()
dog2.set_dog("Hachi", 12)

dogs = [dog1, dog2]  # リストに格納
for d in dogs:
    print(d.name, d.age)
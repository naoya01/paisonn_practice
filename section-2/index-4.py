# -*- coding: utf-8 -*-

# __init__メソッド
class Calc:  # Calcクラス
  def __init__(self, a):  # __init__メソッド
    self.a = a

  def add(self, b):  # addメソッド
    print(self.a + b)

  def multiply(self, b):  # multiplyメソッド
    print(self.a * b)

cl = Calc(3)  # インスタンスclを生成
cl.add(4)  # 3 + 4
cl.multiply(4) # 3 × 4

class Calc:  # Calcクラス
  def __init__(self, a):  # __init__メソッド
    self.a = a

  def __call__(self, c):  # __call__メソッド
    print(self.a * c + c)

  def add(self, b):  # addメソッド
    print(self.a + b)

  def multiply(self, b):  # multiplyメソッド
    print(self.a * b)

cl = Calc(3)  # インスタンスclを生成

# インスタンス名clを使って__call__メソッドを呼ぶ
cl(5)  # 3 × 5 + 5

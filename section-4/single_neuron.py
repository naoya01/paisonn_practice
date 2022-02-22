class Neuron:
    def __init__(self):  # 初期設定
        self.input_sum = 0.0

    def set_input(self, inp):
        self.input_sum += inp
        print (self.input_sum)

# ニューラルネットワーク
class NeuralNetwork:
    def __init__(self):  # 初期設定
        self.neuron = Neuron()  #ニューロンのインスタンス

    def commit(self, input_data):  # 実行
        for data in input_data:
            self.neuron.set_input(data)

# ニューラルネットワークのインスタンス
neural_network = NeuralNetwork()

# 実行
input_data = [1.0, 2.0, 3.0]
neural_network.commit(input_data)


import numpy as np

# シグモイド関数
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

# ニューロン
class Neuron:
    def __init__(self):  # 初期設定
        self.input_sum = 0.0
        self.output = 0.0

    def set_input(self, inp):
        self.input_sum += inp

    def get_output(self):
        self.output = sigmoid(self.input_sum)
        return self.output

# ニューラルネットワーク
class NeuralNetwork:
    def __init__(self):  # 初期設定
        self.neuron = Neuron()  #ニューロンのインスタンス

    def commit(self, input_data):  # 実行
        for data in input_data:
            self.neuron.set_input(data)
        return self.neuron.get_output()

# ニューラルネットワークのインスタンス
neural_network = NeuralNetwork()

# 実行
input_data = [1.0, 2.0, 3.0]
print(neural_network.commit(input_data))
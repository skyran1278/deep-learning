# coding: utf-8
import os
import matplotlib.pyplot as plt
from matplotlib.image import imread

# 解決相對路徑的問題
# python 的相對是指整個目錄的相對
# 而不是執行程式的相對
# img = imread('../dataset/lena.png')  # 画像の読み込み
# img = imread('./dataset/lena.png')  # 相對於 deep-learning-from-scratch
my_path = os.path.abspath(os.path.dirname(__file__))
# 過程演示
# print(__file__)
# print(os.path.dirname(__file__))
# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(__file__))
# print(my_path)
path = os.path.join(my_path, "./../dataset/lena.png")
img = imread(path)  # 絕對路徑

plt.imshow(img)

plt.show()

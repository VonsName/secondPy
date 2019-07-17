# __author:  Administrator
# __date:  2019/7/15/015

import numpy as np

file_path = "C:\\Users\\Administrator\\Desktop\\nump.csv"
t1 = np.loadtxt(file_path, delimiter=",", dtype="int")
# t2 = np.loadtxt(file_path, delimiter=",", dtype="int", unpack=True)
print(t1)
print("**************")
# print(t2)

# print(t1[2])  # 第三行的数据

# print("***********")
# 取连续的多行
# print(t1[2:])  # 第三行后面所有的

# 取不连续的多行
# print(t1[[1, 3, 4]])  # 第2,4,5行

# 取列
# print(t1[:, 2])  # 第三列 [34 89  4 55  3]
# print(t1[1, 2])  # 第2行第三列 89

# 连续多列,第三列后所有的列
#  [[34 56]
#   [89 90]
#   [ 4  5]
#   [55 78]
#   [ 3  4]]
# print(t1[:, 2:])


# 不连续多列,第一列和第三列
# print(t1[:, [0, 2]])

# 多行多列 第三行第四列
# print(t1[2, 3])

# 第二行以及后面所有的行的第三列
# [[89]
#  [ 4]
#  [55]
#  [ 3]]
# print(t1[1:, [2]])

# 多行多列 第二行第三列以及后面所有的数据
# [[89 90]
#  [ 4  5]
#  [55 78]
#  [ 3  4]]
# print(t1[1:, 2:])

# 第一行到第三行 第一列到第三列
print(t1[0:3, 0:3])

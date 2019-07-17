# __author:  Administrator
# __date:  2019/7/15/015
import numpy as np

file_path = "C:\\Users\\Administrator\\Desktop\\nump.csv"
t1 = np.loadtxt(file_path, delimiter=",", dtype=int)
# 创建一个和t1一样的行,1列的数组 值全部为0
h_np_zeros = np.zeros((t1.shape[0], 1), dtype=int)
# 水平拼接 在t1数组里面拼接上np_zeros的数据 每行增加一列
t1 = np.hstack((t1, h_np_zeros))
v_ones = np.ones((1, t1.shape[1]))

# 垂直拼接 增加一行
t1 = np.vstack((t1, v_ones)).astype(int)
print(t1)
# axis=1 表示每行
# axis=0 表示每列
np_max = np.max(t1, axis=0)
np_max_index = np.argmax(t1, axis=0)
print(np_max)
print(np_max_index)

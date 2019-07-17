# __author:  Administrator
# __date:  2019/7/12/012
import numpy as np

np_array = np.array([1, 2, 3])
print(type(np_array))
print(np_array)
print([1, 2, 3])
t2 = np.array(range(10))
print(t2)
# 返回的是一个数组
t3 = np.arange(2, 10, 2)
print(type(t3))
print(t3)
print(range(2, 10, 2))

# int32 数组存放的数组的类型
print(t3.dtype)

t5 = np.arange(10, dtype="int64")
print(t5.dtype)

# 改变数组存放的数据类型
t6 = t5.astype("i1")
print(t6.dtype)

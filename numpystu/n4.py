# __author:  Administrator
# __date:  2019/7/15/015
import numpy as np


def me(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]
        nan_num = np.count_nonzero(t1 != t1)
        print(temp_col)
        # [0. 4. 8.]
        # [1. 5. 9.]
        # [ 2. nan 10.]
        # [ 3. nan 11.]
        if nan_num != 0:
            # 当前一列不为nan的数组
            temp_col_median = temp_col[temp_col == temp_col]
            # print(temp_col_median) # [ 2. 10.]
            # 计算中值
            median = np.median(temp_col_median, axis=0)
            # 把中值赋值给nan的位置
            temp_col[temp_col != temp_col] = median
    print(t1)


# print(t1)

if __name__ == '__main__':
    print("000000000000")
    t = np.arange(12).reshape((3, 4)).astype(float)
    t[1, 2:] = np.nan
    print(t)
    print("*******")
    me(t)

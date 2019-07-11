# __author:  Administrator
# __date:  2019/7/10/010

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 11)
y = 2 * x + 5

# 图片大小
plt.figure(figsize=(20, 8), dpi=80)
# 绘图
plt.plot(x, y)

# 设置x的刻度
# plt.xticks(x)

# 设置y的刻度
plt.yticks(y)

# 保存图片
# plt.savefig("./j.png")

# 展示
plt.show()

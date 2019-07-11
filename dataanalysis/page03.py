# __author:  Administrator
# __date:  2019/7/11/011

import random

from matplotlib import font_manager
from matplotlib import pyplot as plt

m_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\msyh.ttc")
x = range(11, 31)
y = [random.randint(1, 5) for i in range(11, 31)]
y1 = [random.randint(1, 8) for i in range(11, 31)]
_x = list(x)[::1]
_y = list(y)[::1]
_xlabel = ["{}岁".format(i) for i in x]
# 设置x的刻度
plt.xticks(_x, _xlabel, fontproperties=m_font, rotation=90)

# 绘制网格
plt.grid(alpha=0.5)  # alpha 表示透明度
plt.plot(x, y, label="我", color='orange', linestyle=':')
plt.plot(x, y1, label="他")

# 添加图例 loc 设置位置
plt.legend(prop=m_font, loc="upper right")
plt.show()

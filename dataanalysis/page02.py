# __author:  Administrator
# __date:  2019/7/11/011

import random

from matplotlib import font_manager
from matplotlib import pyplot as plt

# 设置显示中文 无效
# font = {'family': 'monospace',
#         'weight': 'bold',
#         'size': 12}
# matplotlib.rc("font", **font)

# 设置中文字体
m_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\msyh.ttc")
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
plt.plot(x, y)
# 转换成列表并设置步长为10
_x = list(x)
_xlables = ["10点{}分".format(i) for i in range(60)]
_xlables += ["11点{}分".format(i) for i in range(60)]

# rotation旋转
plt.xticks(_x[::5], _xlables[::5], rotation=45, fontproperties=m_font)

plt.xlabel("时间", fontproperties=m_font)
plt.ylabel("温度", fontproperties=m_font)
plt.title("温度时间变化率", fontproperties=m_font)

plt.show()

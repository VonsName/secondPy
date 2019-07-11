# __author:  Administrator
# __date:  2019/7/11/011
# 03多次条形图
from matplotlib import pyplot as plt
from matplotlib import font_manager

m_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\msyh.ttc")

a = ["战狼2", "妖猫传", "斗牛骑士", "驯龙高手3", "天下无贼"]
b = [55.66, 35, 45, 88, 23.33]

plt.xticks(fontproperties=m_font)
plt.yticks(fontproperties=m_font)
# plt.bar(a, b, width=0.3)
plt.barh(a, b, height=0.5, color='r')
plt.grid()
plt.show()

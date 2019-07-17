# __author:  Administrator
# __date:  2019/7/11/011
# 03多次条形图
from matplotlib import pyplot as plt
from matplotlib import font_manager

m_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\msyh.ttc")

a = ["战狼2", "妖猫传", "斗牛骑士", "驯龙高手3", "天下无贼"]
b = [55.66, 35, 45, 88, 23.33]
c = [23.66, 20, 55.4, 30, 76.33]
d = [25.66, 75, 31, 67, 53.33]
a1 = list(range(len(a)))
a2 = [i + 0.2 for i in a1]
a3 = [i + 0.2 * 2 for i in a1]
print(range(len(a)))
plt.xticks(a2, a, fontproperties=m_font)
plt.yticks(fontproperties=m_font)
# plt.bar(a, b, width=0.3)
# plt.barh(a, b, height=0.5, color='r')
plt.bar(range(len(a)), b, width=0.2, label="14日")
plt.bar(a2, c, width=0.2, label="15日")
plt.bar(a3, d, width=0.2, label="16日")
plt.grid()
plt.legend(prop=m_font)
plt.show()

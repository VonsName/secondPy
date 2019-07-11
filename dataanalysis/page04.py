# __author:  Administrator
# __date:  2019/7/11/011
from matplotlib import pyplot as plt
from matplotlib import font_manager

m_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\msyh.ttc")
y1 = [18, 12, 13, 23, 15, 14, 25, 23, 26, 18, 20, 23, 15, 13, 40, 25, 10, 20, 22, 13, 28, 20]
y2 = [23, 15, 13, 40, 25, 10, 20, 22, 13, 28, 20, 18, 12, 13, 23, 15, 14, 25, 23, 26, 18, 20]

x = range(1, 23)
x1 = range(33, 55)
_x = list(x) + list(x1)
_xlabel = ["3月{}日".format(i) for i in x]
_xlabel += ["10月{}日".format(i - 32) for i in x1]
plt.xticks(_x[::2], _xlabel, fontproperties=m_font, rotation=90)

# 散点图
plt.scatter(x, y1, label="3月")
plt.scatter(x1, y2, label="10月")

plt.xlabel("时间", fontproperties=m_font)
plt.ylabel("温度", fontproperties=m_font)
plt.title("标题", fontproperties=m_font)
plt.legend(prop=m_font, loc="upper center")
plt.show()

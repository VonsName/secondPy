# __author:  Administrator
# __date:  2019/7/18/018

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

m_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\msyh.ttc")

df = pd.read_csv("./starbucks_store_worldwide.csv")
# data = df.groupby(by="Country").count()["Brand"].sort_values(ascending=False)[:10]
# x = data.index
# y = data.values
# plt.bar(x, y)
# plt.show()

cn_city = df[df["Country"] == "CN"].groupby(by="City").count()["Brand"].sort_values(ascending=False)[:10]

x = cn_city.index
y = cn_city.values
plt.barh(x, y, color="orange")
plt.xticks(fontproperties=m_font)
plt.yticks(fontproperties=m_font)
plt.show()

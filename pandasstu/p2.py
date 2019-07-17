# __author:  Administrator
# __date:  2019/7/17/017
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("./IMDB-Movie-Data.csv")
# print(df.head(1))
# print(df.info())
runtime_minutes_ = df["Runtime (Minutes)"].values
# print(runtime_minutes_)
rating_ = df["Rating"].values
# print(runtime_minutes_)

minutes__max = runtime_minutes_.max()
minutes__min = runtime_minutes_.min()

num = (minutes__max - minutes__min) // 5
plt.hist(runtime_minutes_, num)
# plt.figure(figsize=(80, 20), dpi=80)
plt.xticks(range(minutes__min, minutes__max + 5, 10))
plt.show()

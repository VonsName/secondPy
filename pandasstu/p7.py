# __author:  Administrator
# __date:  2019/7/18/018

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("./books.csv")
o_year = df[pd.notnull(df["original_publication_year"])].groupby("original_publication_year").count()["id"]
# print(o_year)
# print(df.notnull())
year_ = df[pd.notnull(df["original_publication_year"])]
count__mean = df["average_rating"].groupby(by=year_["original_publication_year"]).mean()
x = count__mean.index
y = count__mean.values
plt.plot(range(len(x)), y)
plt.xticks(list(range(len(x)))[::10], x[::10].astype(int), rotation=45)
plt.show()

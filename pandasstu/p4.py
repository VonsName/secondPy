# __author:  Administrator
# __date:  2019/7/17/017
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("./IMDB-Movie-Data.csv")

genre_ = df["Genre"].str.split(",").tolist()
# title = list(set(df["Title"]))
# print(len(title))
# print(len(list(set(title))))
# print(df.shape[0])
genre_list = list(set([i for j in genre_ for i in j]))
df_zero = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list, dtype=int)
# print(df_zero)
for i in range(df.shape[0]):
    df_zero.loc[i, genre_[i]] = 1

print(df_zero)

zero_sum = df_zero.sum(axis=0).sort_values()
# print(zero_sum)
x = zero_sum.index
y = zero_sum.values
plt.bar(x, y)
plt.xticks(rotation=270)
plt.show()

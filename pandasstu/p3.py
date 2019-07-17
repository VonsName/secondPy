# __author:  Administrator
# __date:  2019/7/17/017

import pandas as pd

df = pd.read_csv("./IMDB-Movie-Data.csv")
# print(df.info())

# print(df["Actors"].values)
# print(len(list(set(df["Director"].values))))
print(len(df["Director"].unique()))  # unique() 可以去重
split__tolist = df["Actors"].str.split(",").tolist()
ac_list = [i for j in split__tolist for i in j]  # 相当于双重遍历 list 里面还有list,先遍历出j 然后在j里面遍历出每个i
print(len(set(ac_list)))

# for j in split__tolist:
#     print(j)
#     break

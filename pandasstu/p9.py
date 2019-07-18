# __author:  Administrator
# __date:  2019/7/18/018
import numpy as np
import pandas as pd

df = pd.read_csv("./911.csv")
tmp_list_ = df["title"].str.split(":").tolist()
# print(type(df["title"].str.split(":")))
t_list = list(set([i[0] for i in tmp_list_ if len(i) > 0]))
# print(t_list)

# print(df["title"].str)
zero_df = pd.DataFrame(np.zeros((df.shape[0], len(t_list))), columns=t_list, dtype=int)
for t in t_list:
    zero_df[t][df["title"].str.contains(t)] = 1

print(zero_df.sum(axis=0))

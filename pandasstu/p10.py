# __author:  Administrator
# __date:  2019/7/18/018

import numpy as np
import pandas as pd

df = pd.read_csv("./911.csv")

# time_stamp_ = pd.to_datetime(df["timeStamp"])
# print(time_stamp_)

df["timeStamp"] = pd.to_datetime(df["timeStamp"])
df.set_index("timeStamp", inplace=True)
# print(df.head())
m__count = df.resample("M").count()["title"]
# print(m__count.head())

# __author:  Administrator
# __date:  2019/7/17/017
import pandas as pd

df = pd.read_csv("./starbucks_store_worldwide.csv")
# groupby = df.groupby(by="Country")
# DataFrameGroupBy 可以进行聚合 遍历
# print(groupby) #pandas.core.groupby.generic.DataFrameGroupBy
# for i, j in groupby:
#     print(i)
#     print(j)
#     print("*"*50)

# print(groupby.count())
# brand__count = groupby["Brand"].count()
#
# print(brand__count["CN"])
# print(brand__count["US"])

# cn_ = df[df["Country"] == "CN"]
# cn__groupby_p = cn_.groupby(by="State/Province")
# print(cn__groupby_p.count()["Brand"])

# 根据多个列进行分组
# print(df.groupby(by=[df["Country"], df["State/Province"]]).count()["Brand"])
# print(df.groupby(by=["Country", "State/Province"]).count()["Brand"])
# print(df["Country"].groupby(by=[df["Country"], df["State/Province"]]).count())


# 04:13
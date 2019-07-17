# __author:  Administrator
# __date:  2019/7/15/015

import pandas as pd

# client = MongoClient()

file_path = "C:\\Users\\Administrator\\Desktop\\nump.csv"
df = pd.read_csv(file_path)
# print(t1)

dict_i = {"name": ["lisi", "wangwu", "zhangsan"], "age": [35, 25, 16], "tel": ["133131", "133131", "133131"]}
d1 = pd.DataFrame(dict_i)
# print(d1)
print(d1.ndim)  # d1.ndim 数据的维度
print(d1.head(1))  # 默认展示前5行
print(d1.tail(1))  # 尾部
# print(d1.info())
print(d1.describe())
print("**************")

# 根据值的列age排序 ascending=False 表示倒序
d1 = d1.sort_values(by="age", ascending=False)
print(d1)
print("*******************")
# 取前面第一行 方括号写字符串表示取某一列 方括号写数字表示取某一行
print(d1[:1]["age"])
print(type(d1[:1]["age"]))

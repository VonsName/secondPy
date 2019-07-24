# __author:  Administrator
# __date:  2019/7/24/024
from sklearn.datasets import load_iris, fetch_20newsgroups
from sklearn.model_selection import train_test_split

li = load_iris()
# # 特征值
# print(li.data)
# # 目标值
# print(li.target)

# # 包含训练集和测试集
# x_train, x_test, y_train, y_test = train_test_split(li.data, li.target, test_size=0.25)
# print("训练集特征值和目标值", x_train, y_train)
# print("测试集特征值和目标值", x_test, y_test)
news = fetch_20newsgroups(subset="all")
print(news.data)
print(news.target)
# 28:28

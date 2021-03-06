# __author:  Administrator
# __date:  2019/7/25/025

import pandas as pd
from sklearn.datasets import load_boston
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib


def knn():
    """
    K-近邻预测用户签到位置
    :return:
    """
    train_data = pd.read_csv("./train.csv")
    # 通过条件缩小数据范围
    # train_data.query("x>1.0 & x<1.5 & y>2.5 & y<2.75")

    time_v = pd.to_datetime(train_data["time"], unit="s")

    time_v = pd.DatetimeIndex(time_v)
    train_data["day"] = time_v.day
    train_data["hour"] = time_v.hour
    train_data["weekday"] = time_v.weekday

    # 删除时间特征 sklean axis=1表示列
    train_data.drop(["time"], axis=1)
    # 分组求和 groupby后place_id会变为行索引
    place_id__count = train_data.groupby("place_id").count()
    # 过滤row_id>3 reset_index把place_id变为不再是作为索引
    tf = place_id__count[place_id__count.row_id > 3].reset_index()
    # 从train_data里面筛选出row_id>3的出数据
    train_data = train_data[train_data["place_id"].isin(tf.place_id)]
    # y表示目标值
    y = train_data["place_id"]
    # x表示特征值
    x = train_data.drop(["place_id"], axis=1)
    x = train_data.drop(["row_id"], axis=1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # # 标准化
    # std = StandardScaler()
    # x_train = std.fit_transform(x_train)
    # x_test = std.transform(x_test)

    # knn K值取太小 容易受异常点影响 K值取太大 容易受样本数量影响
    kn = KNeighborsClassifier()
    # 输入数据
    # kn.fit(x_train, y_train)

    # 预测结果
    # y_predict = kn.predict(x_test)
    # print("预测目标位置:", y_predict)
    # # 准确率
    # print("准确率:", kn.score(x_test, y_test))

    param = {"n_neighbors": [3, 5, 10]}

    # 进行网格搜索 cv表示交叉验证的次数
    gsc = GridSearchCV(kn, param_grid=param, cv=2)
    gsc.fit(x_train, y_train)
    print("测试集上的准确率:", gsc.score(x_test, y_test))
    print("交叉验证中最好的结果:", gsc.best_score_)
    print("选择的最好的模型:", gsc.best_estimator_)
    print("每个超参数每次交叉验证的结果:", gsc.cv_results_)


def decision():
    """
    决策树对泰坦尼克的生死
    :return:
    """
    titanic_data = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")

    # 特征值
    x = titanic_data[['pclass', 'age', 'sex']]

    x["age"].fillna(x["age"].mean(), inplace=True)

    # 目标值
    y = titanic_data['survived']
    # print(x)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 字典特征抽取
    dic = DictVectorizer(sparse=False)
    x_train = dic.fit_transform(x_train.to_dict(orient="records"))
    # print(dic.get_feature_names())
    # print(x_train)

    x_test = dic.transform(x_test.to_dict(orient="records"))

    # 使用决策树进行预测
    dtc = DecisionTreeClassifier(max_depth=10)
    dtc.fit(x_train, y_train)
    print("预测的准确率", dtc.score(x_test, y_test))

    # 导出决策树的结构
    export_graphviz(dtc, "./decision.dot", feature_names=["年龄", "pclass", "age", "sex", "女性", "男性"])

    # 使用随机森林
    # param = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 10, 15, 25, 30]}
    # rf = RandomForestClassifier()
    # gc = GridSearchCV(rf, param, cv=2)
    # gc.fit(x_train, y_train)
    # print("准确率", gc.score(x_test, y_test))
    # print("选择的参数模型", gc.best_params_)


# 03 线性回归策略

def my_linear():
    """
    线性回归预测
    :return:
    """

    lb = load_boston()
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)

    # 标准化
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    std_y = StandardScaler()
    # 需要传二维的
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))
    y_test = std_y.transform(y_test.reshape(-1, 1))

    # 使用正规方程求解
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    print(lr.coef_)

    # 保存训练好的模型
    # joblib.dump(lr, "./lr.pkl")
    # 加载保存的模型
    # joblib.load("./lr.pkl")

    # 预测测试集,得到预测的目标值
    y_predict = std_y.inverse_transform(lr.predict(x_test))
    print("正规方程预测价格每个房子的:", y_predict)
    # 预测值与目标值的误差
    print("正规方程的均方误差:", mean_squared_error(std_y.inverse_transform(y_test), y_predict))

    # 使用梯度下降求解
    sgd = SGDRegressor()
    sgd.fit(x_train, y_train)
    print(sgd.coef_)
    y_predict_sgd = std_y.inverse_transform(sgd.predict(x_test))
    print("SGD预测价格每个房子的:", y_predict_sgd)
    # 预测值与目标值的误差
    print("SGD的均方误差:", mean_squared_error(std_y.inverse_transform(y_test), y_predict_sgd))

    # 带有正则化的线性回归 岭回归
    ridge = Ridge(alpha=1.0)
    ridge.fit(x_train, y_train)
    print(ridge.coef_)
    y_predict_ridge = std_y.inverse_transform(ridge.predict(x_test))
    print("ridge预测价格每个房子的:", y_predict_ridge)
    # 预测值与目标值的误差
    print("ridge的均方误差:", mean_squared_error(std_y.inverse_transform(y_test), y_predict_ridge))


if __name__ == '__main__':
    # knn()
    # decision()
    my_linear()

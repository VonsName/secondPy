# __author:  Administrator
# __date:  2019/7/25/025
# 朴素贝叶斯 - 特征独立的条件下
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report



# 09
def ps():
    """
    朴素贝叶斯文本分类
    :return:
    """
    news = fetch_20newsgroups(subset="all")
    data = news.data
    target = news.target
    x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.25)

    # 对数据集进行特征抽取
    tf = TfidfVectorizer()
    # 以训练集当中的词的列表进行每篇文章重要性统计
    x_train = tf.fit_transform(x_train)
    x_test = tf.transform(x_test)

    # 使用朴树贝叶斯进行预测
    mi = MultinomialNB(alpha=1.0)
    mi.fit(x_train, y_train)
    # 预测目标值
    predict_y = mi.predict(x_test)
    # 预测的准确率
    mi_score = mi.score(x_test, y_test)
    print(mi_score)

    # 精确率与召回率
    report = classification_report(y_test, predict_y, target_names=news.target_names)


if __name__ == '__main__':
    ps()

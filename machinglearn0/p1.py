# __author:  Administrator
# __date:  2019/7/18/018

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer

dic_ = [{'city': '北京', 'tem': 100}, {'city': '上海', 'tem': 89}, {'city': '重庆', 'tem': 50}]


def dictvec():
    """
    对字典进行特征值化
    :return:None
    """
    dicy = DictVectorizer(sparse=False)
    data = dicy.fit_transform(dic_)
    print(dicy.get_feature_names())
    print(data)


def countvec():
    """
    对文本进行特征值化
    :return:None
    """
    # ["life is is short,i like python", "life is too long,i dislike python"]
    l = ["人生 苦短,我 喜欢 python", "人生 路漫漫,我 不喜欢 python"]
    cv = CountVectorizer()
    data = cv.fit_transform(l)
    print(data.toarray())
    print(cv.get_feature_names())


if __name__ == '__main__':
    # dictvec()
    countvec()

# 06:14

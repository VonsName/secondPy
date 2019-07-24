# __author:  Administrator
# __date:  2019/7/18/018

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import jieba

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
    l = ["人生 苦短 苦短,我 喜欢 python", "人生 路漫漫,我 不喜欢 python"]
    cv = CountVectorizer()
    data = cv.fit_transform(l)
    print(data.toarray())
    print(cv.get_feature_names())

    # cut = jieba.cut("我喜欢python啊,你呢")
    # print(cut)


def cutword():
    cut1 = jieba.cut("数学家们已经研究过200多种这样的代数结构，其中最主要德若当代数和李代数是不服从结合律的代数的例子。这些工作的绝大部分属于20世纪，它们使一般化和抽象化的思想在现代数学中得到了充分的反映。")
    cut2 = jieba.cut("中国数学家在抽象代数学的研究始于30年代。当中已在许多方面取得了有意义和重要的成果，其中尤以曾炯之、华罗庚和周炜良的工作更为显著。")
    cut3 = jieba.cut("后又引进交叉积的概念并用决定有限维枷罗瓦扩张的布饶尔群。最后导致代数的主定理的证明，代数数域上的中心可除代数是循环代数。")
    print(cut1, cut2, cut3)


def tfidf():
    pass


if __name__ == '__main__':
    # dictvec()
    # countvec()
    cutword()

# __author:  Administrator
# __date:  2019/7/22/022

import jieba
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Imputer
from sklearn.decomposition import PCA


def cutword():
    cut1 = jieba.cut("数学家们已经研究过200多种这样的代数结构，其中最主要德若当代数和李代数是不服从结合律的代数的例子。这些工作的绝大部分属于20世纪，它们使一般化和抽象化的思想在现代数学中得到了充分的反映。")
    cut2 = jieba.cut("中国数学家在抽象代数学的研究始于30年代。当中已在许多方面取得了有意义和重要的成果，其中尤以曾炯之、华罗庚和周炜良的工作更为显著。")
    cut3 = jieba.cut("后又引进交叉积的概念并用决定有限维枷罗瓦扩张的布饶尔群。最后导致代数的主定理的证明，代数数域上的中心可除代数是循环代数。")

    l1 = list(cut1)
    l2 = list(cut2)
    l3 = list(cut3)

    c1 = ' '.join(l1)
    c2 = ' '.join(l2)
    c3 = ' '.join(l3)

    return c1, c2, c3


def tfidf():
    c01, c02, c03 = cutword()
    tv = TfidfVectorizer()
    data = tv.fit_transform([c01, c02, c03])
    print(tv.get_feature_names())
    print(data.toarray())


def minscale():
    """
    归一化处理,通过对原始数据进行变换把数据映射到(默认0-1)之间
    如果数据异常点大 对数据的影响较大
    :return: None
    """
    mm = MinMaxScaler(feature_range=(2, 3))
    data = mm.fit_transform([[90, 2, 5, 35], [60, 3, 15, 3], [75, 2, 9, 3]])
    print(data)
    return None


def stdscale():
    """
    标准化缩放
    :return:
    """
    sd = StandardScaler()
    # 每列的平均值为0
    data = sd.fit_transform([[3., -1., 3.], [5., 6., 2.], [4., 2., -1.]])
    print(data)


def imp():
    """
    缺失值处理
    :return:
    """
    ip = Imputer(missing_values='NaN', strategy='mean', axis=0)
    data = ip.fit_transform([[1, 2], [np.nan, 3], [2, 6]])
    print(data)


def var():
    """
    特征选择 删除低方差的特征
    :return:
    """
    vt = VarianceThreshold(threshold=1.0)
    data = vt.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])
    print(data)


def pca():
    """
    主成分分析 进行特征降维
    :return:
    """
    pc = PCA(n_components=0.9)
    data = pc.fit_transform([[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]])
    print(data)


# 数据降维 06:27
if __name__ == '__main__':
    # tfidf()
    # minscale()
    # stdscale()
    # pd = pd.DataFrame(np.arange(12).reshape(3, 4))
    # print(pd)
    # print(pd.mean(axis=0))
    # stdscale()
    # imp()
    # var()
    pca()

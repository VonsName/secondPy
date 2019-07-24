# __author:  Administrator
# __date:  2019/7/24/024
import pandas as pd
from sklearn.decomposition import PCA


def t():
    prior = pd.read_csv("./order_products__prior.csv")
    orders = pd.read_csv("./orders.csv")
    aisles = pd.read_csv("./aisles.csv")
    products = pd.read_csv("./products.csv")
    _mg = pd.merge(prior, products, on=["product_id", "product_id"])
    _mg = pd.merge(_mg, orders, on=["order_id", "order_id"])
    _mg = pd.merge(_mg, aisles, on=["aisle_id", "aisle_id"])
    cross = pd.crosstab(_mg['user_id'], _mg['aisle'])
    # print(cross)
    # 主成分分析
    pca = PCA(n_components=0.9)
    data = pca.fit_transform(cross)
    print(data)


if __name__ == '__main__':
    t()

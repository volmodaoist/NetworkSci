import os,sys
import networkx as nx
import matplotlib.pyplot as plt

sys.path.append("../")
sys.path.append("../../")

from utils import *
from config import *
from Graph import *



g1 = create_graph(0)
g2 = create_graph(1)

g1.plot_graph()
g2.plot_graph()

# g1.plot_degree()
# g2.plot_degree()

## 测试官方文档里面提供的测量相似度的所有方法
## https://networkx.org/documentation/stable/reference/algorithms/similarity.html

# 通过比较编辑距离, 分析两个图的相似度, 计算编辑距离是一个NP难题
# print("Graph edit distance: {:.2f}".format(nx.graph_edit_distance(g1,g2)))

# WL hash 判定同构
# h1 = nx.weisfeiler_lehman_graph_hash(g1)
# h2 = nx.weisfeiler_lehman_graph_hash(g2)
# print(h1)
# print(h2)

# print(nx.degree_histogram(g1))
# print(nx.degree_histogram(g2))

# print(max(nx.degree_centrality(g1).values()))
# print(max(nx.degree_centrality(g2).values()))

def centrality(g, isSorted = False):
    node, centrality = [], []
    node_x_centrality = nx.degree_centrality(g).items()
    for k,v in node_x_centrality:
        node.append(k)
        centrality.append(v)
    if isSorted:
        plt.stem(sorted(centrality, reverse = True))
    else:
        plt.stem(node, centrality)
    plt.show()


# 查看并对比两个图的中心性
centrality(g1, True)
centrality(g2, True)   
## 计算两个图的相似度
import os,sys
import networkx as nx
import matplotlib.pyplot as plt

sys.path.append("../")
sys.path.append("../../")

from config import *
from Graph import *


# 打开文件并建图
def create_graph(idx):
    g = nx.Graph()
    with open("../in/in-{}.txt".format(idx)) as gf:
        edges =  int(gf.readline())
        for line in gf.readlines():
            u,v, w = (int(e) for e in line.split(" "))
            g.add_edge(u, v, weight = w)
    return Graph(g)


g1 = create_graph(0)
g2 = create_graph(1)

g1.plot_graph()
g2.plot_graph()

## 测试官方文档里面提供的测量相似度的所有方法
## https://networkx.org/documentation/stable/reference/algorithms/similarity.html

# 计算编辑距离是一个NP难题
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

def centrality(g):
    node, centrality = [], []
    for k,v in nx.degree_centrality(g).items():
        node.append(k)
        centrality.append(v)
    plt.stem(node, centrality)
    plt.show()


# 查看并对比两个图的中心性
centrality(g1)
centrality(g2)   
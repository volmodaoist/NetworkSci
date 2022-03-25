import functools
import networkx as nx
import matplotlib.pyplot as plt

""" 
  先把能够想到都列出来
    1. 度序列与度分布
    2. 距离/最短路径 + 最短路径分布
    3. 介数
    4. 集聚系数
    5. 社团
    6. 连通块
    7. 幂律分布
"""
class Graph(nx.classes.graph.Graph):
    def __init__(self, incoming_graph_data=None, **attr):
        super().__init__(incoming_graph_data, **attr)
    
    def average_degree(self):
        return nx.average_neighbor_degree(self)

    def average_clustering(self):
        return nx.average_clustering(self)

    # 通过直方图展示度分布
    def hist_degree(self):
        node_x_degree = self.degree()
        node, degree = zip(*node_x_degree)
        plt.hist(degree, node)
        plt.show()

        """
        有没有办法把图片花在一个子图上面, 然后再把这个子图传给figure容器呢?
        """

    def get_static_prop():
        pass
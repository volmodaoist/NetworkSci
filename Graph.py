from turtle import color
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from config import *
from mpl_toolkits.mplot3d import Axes3D 

""" 
  先把最基本的列出来,随后慢慢补充:
    1. 平均度 + 柱状图展示每个节点的度分布
    2. 平均集聚系数 + 柱状图展示每个节点的集聚系数
    3. 介数 + 三维散点图按颜色区分介数
    ...
"""
class Graph(nx.classes.graph.Graph):
    def __init__(self, incoming_graph_data = None, seed = INIT_SEED, **attr):
        super().__init__(incoming_graph_data, **attr)
        self.seed = seed

    # 绘制图结构本身
    def plot(self, with_labels = True):
        ps = nx.drawing.layout.spring_layout(self, seed = self.seed)
        nx.draw(self, ps, with_labels = with_labels)
        plt.show()

    # 获取平均度
    def get_average_degree(self):
        cnt, ans = 0, 0 
        average_degree_each = nx.algorithms.average_neighbor_degree(self).values()
        for x in average_degree_each:
            cnt += 1
            ans += x
        return ans / cnt
    
    # 获取平均集聚系数
    def get_average_clustering(self):
        return nx.algorithms.average_clustering(self)

    # 获取各条连边的介数
    def get_edges_betweeness(self, printable = False):
        edges_x_betweeness = nx.edge_betweenness(self)
        U,V,B = [],[],[]
        for (u,v), bwn in edges_x_betweeness.items():
            U.append(u)
            V.append(v)
            B.append(bwn)
            if printable  == True:
                print("介数:{}->{} = {}".format(u, v, bwn))
        return U,V,B


    # 通过柱状图展示度分布
    def bar_degree(self):
        node_x_degree = self.degree()
        node, degree = zip(*node_x_degree)
        plt.xlabel("Ordered Node Number")
        plt.ylabel("Node degree")
        plt.bar(node, degree)
        plt.show()

    # 通过柱状图展示集聚系数
    def bar_clustering(self):
        node_x_clustering = nx.clustering(self)
        node, clustering = zip(*node_x_clustering.items())
        plt.xlabel("Ordered Node Number")
        plt.ylabel("Clustering")
        plt.bar(node, clustering)
        plt.show()

    # 通过柱状图展示介数
    def bar_betweeness(self):
        U,V,B = self.get_edges_betweeness()
        ax = plt.axes(projection='3d')
        ax.scatter3D(U, V, B, c = B)
        ax.set_xlabel("Node U")
        ax.set_ylabel("Node V")
        ax.set_zlabel("Betweeness")
        ax.set_title("Betweeness of each edge")
        plt.show()


    ########################################## 
    ### 获取所有静态性质, 这些性质可以分类两批: #
    ###     1. 静态节点属性                   #
    ###     2. 静态连表属性                   #
    ##########################################
    def get_static_prop(self):
        print("平均度:", self.get_average_degree())
        print("平均集聚系数:", self.get_average_clustering())
        print("特征路径长度:", nx.algorithms.average_shortest_path_length(self))
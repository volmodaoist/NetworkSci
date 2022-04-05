from cProfile import label
import os,sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

sys.path.append("../")
sys.path.append("../../")

from config import *
from Graph import *
from NetAttacker import *


# 打开文件并建图
def create_graph(idx):
    g = nx.Graph()
    with open("../in/in-{}.txt".format(idx)) as gf:
        edges =  int(gf.readline())
        for line in gf.readlines():
            u,v, w = (int(e) for e in line.split(" "))
            g.add_edge(u, v, weight = w)
    return Graph(g)


# 使用稠密图表示法, 把图对象转化得到图矩阵
def create_graph_matrix(graph_nums):
    graph_list = []
    for i in range(graph_nums):
        g = create_graph(i)
        graph_list.append(nx.adjacency_matrix(g).todense())
    return graph_list




def batch_compare(graph_nums):
    sl, rl = [], []
    for i in range(graph_nums):
        g = create_graph(i)
        s = specific_attack(g)
        r = random_attack(g)
        sl.append(s)
        rl.append(r)
        print("聚合图: ag{}.json".format(i), end = "\t")
        print("蓄意攻击: ", s, end = "\t")
        print("随机攻击: ", r, end = "\n")

    return np.array([i for i in range(graph_nums)]), np.array(sl), np.array(rl)


if __name__ == "__main__":
    gl, sl, rl = batch_compare(30)
    width = 0.25
    plt.xticks(gl)
    plt.xlabel("Labels")
    plt.ylabel("Number of attacks")
    plt.bar(gl - width / 2, sl, width, label = "Specific Attack")
    plt.bar(gl + width / 2, rl, width, label = "Random Attack")
    plt.legend()
    plt.show()


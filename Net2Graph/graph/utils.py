import os,sys
import networkx as nx

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

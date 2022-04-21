import os,sys
import networkx as nx
import matplotlib.pyplot as plt

sys.path.append("../")
sys.path.append("../../")


from utils import *
from config import *
from Graph import *


if __name__ == "__main__":
    rows, cols = 3, 3
    for i in range(rows * cols):
        g = create_graph(i)
        plt.subplot(rows, cols, i + 1)
        ps = nx.drawing.layout.spring_layout(g, seed = INIT_SEED)
        nx.draw(g, ps, with_labels = True)
        plt.axis("on")    
    plt.show()

    for i in range(rows * cols):
        g = create_graph(i)
        g.get_static_prop()
        plt.subplot(rows, cols, i + 1) 
        centrality = sorted(nx.degree_centrality(g).values(), reverse = True)        
        plt.stem(centrality)
    plt.suptitle("Centrality")
    plt.show()


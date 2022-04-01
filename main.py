import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from NetGenerator import *

if __name__ == '__main__':
    ng = NetGenerator(0)
    ng.flip()
    
    ng.new_ERNet(50, 0.1)
    ng.netlist_push()


    ng.new_RGNet(20, 3)
    ng.netlist_push()

    ng.new_WSNet(30, 4, 0.5)
    ng.netlist_push()

    ng.new_BANet(100, 1)
    ng.netlist_push()

    net_list = ng.get_curr_netlist()

    tg = Graph(net_list[0])
    # tg.bar_degree()
    # tg.bar_clustering()
    # tg.bar_betweeness()
    tg.get_static_prop()
    # tg.plot()

    # for i,g in enumerate(net_list):
    #     plt.subplot(2, 2, i + 1)
    #     ps = nx.drawing.layout.spring_layout(g, seed = seed)
    #     nx.draw(g, ps, with_labels = True)
    #     plt.axis('on')
    #     plt.title(str(g))
    # plt.show()
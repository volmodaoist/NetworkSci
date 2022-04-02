import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append("./")
sys.path.append("../")

from config import *
from NetGenerator import *



## 测试中心性, 集聚系数, 度分布等属性
if __name__ == "__main__":
    ng = NetGenerator(0)
    ng.flip()

    ## 测试数据
    ####################################
    ng.new_ERNet(50, 0.1)
    ng.netlist_push()                   

    ng.new_RGNet(20, 3)
    ng.netlist_push()

    ng.new_WSNet(30, 4, 0.5)
    ng.netlist_push()

    ng.new_BANet(100, 1)
    ng.netlist_push()
    ####################################


    net_list = ng.get_curr_netlist()
    plt.figure(figsize = (16,16))
    def plot_prop(prop, plot_func):
        for i,g in enumerate(net_list):
            g.flip()
            data_tuple = getattr(g, "plot_" + prop)()
            plt.subplot(2, 2, i + 1)
            plot_func(*(data_tuple))
            plt.title(str(g))
        plt.show()

    # 逐个测试
    # plot_prop("centrality", plt.stem)
    # plot_prop("clustering", plt.bar)
    # plot_prop("degree", plt.bar)

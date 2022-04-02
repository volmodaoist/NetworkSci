import sys
from matplotlib import projections
import numpy as np
import matplotlib.pyplot as plt

sys.path.append("./")
sys.path.append("../")

from config import *
from NetGenerator import *
from mpl_toolkits.mplot3d import Axes3D 



## 测试每条连边的测试并且采用三维散点图可视化
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

    fig = plt.figure(figsize = (16,16))
    axes = [
       fig.add_subplot(2, 2, 1, projection = '3d'),
       fig.add_subplot(2, 2, 2, projection = '3d'),
       fig.add_subplot(2, 2, 3, projection = '3d'),
       fig.add_subplot(2, 2, 4, projection = '3d') 
    ]
    
    for i,g in enumerate(net_list):
        g.flip()
        U,V,B = g.plot_betweeness()
        axes[i].scatter3D(U, V, B , c = B)
        axes[i].set_xlabel("Node U")
        axes[i].set_ylabel("Node V")
        axes[i].set_zlabel("Betweeness")
    plt.suptitle("Betweeness of each edge")
    plt.show()

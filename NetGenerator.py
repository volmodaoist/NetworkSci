import networkx as nx
import matplotlib.pyplot as plt

from Graph import Graph

from config import *

"""
创建一个类,能够生成以下三种网络;
    1. 随机网络
    2. 小世界网络
    3. 无标度网络
实现SI、SIS、SIR模型仿真;
实验为了可复现性, 必须提供随机数种子控制器接口!
"""
        
class NetGenerator:
    def __init__(self, seed = INIT_SEED) -> None:
        self.seed = seed
        self.show = True
        self.curr_network = None
        self.curr_netlist = list()
    
    # 默然打开, 调用这个函数能够利用异或翻转绘图开关的状态
    def flip(self):
        self.show = self.show ^ True

    # 获取当前生成器的随机数的种子, 设定种子是为了使得结果具有可复现性
    def get_seed(self):
        return self.seed
    

    """ 
    以下四种方法能够获取类实例对象 <class 'networkx.classes.graph.Graph'>
        ng.new_ERNet(...)
        ng.new_RGNet(...)
        ng.new_WSNet(...)
        ng.new_BANet(...) 
    通过添加当前网络,能把多个网络存储于列表中一并分析
    """


    def new_RGNet(self, nodes, degree, with_labels = True):
        """
        @pram node : 网络节点个数
        @pram degree : 每个节点的度值 
        """
        rg = nx.generators.random_regular_graph(degree, nodes, seed = self.seed)
        self.curr_network = Graph(rg, seed = self.seed)
        if self.show == True:
            ps = nx.drawing.layout.spring_layout(rg, seed = self.seed)
            nx.draw(rg, ps, with_labels = with_labels)
            plt.show()
        return rg
    
    def new_WSNet(self, nodes, degree, prob_rewire, with_labels = True):
        """
        @pram node : 网络节点个数
        @pram degree : 每个节点的度值 
        @pram prob_rewire :  
        """
        ws = nx.generators.watts_strogatz_graph(nodes, degree, prob_rewire, seed = self.seed)
        self.curr_network = Graph(ws, seed = self.seed)
        if self.show == True:
            ps = nx.drawing.layout.spring_layout(ws, seed = self.seed)
            nx.draw(ws, ps, with_labels = with_labels)
            plt.show()
        return ws


    def new_ERNet(self, nodes, prob_connect, with_labels = True):
        """
        @pram node : 网络节点个数
        @pram prob_connect : 网络连接概率
        """
        er = nx.generators.erdos_renyi_graph(nodes, prob_connect, seed = self.seed)
        self.curr_network = Graph(er, seed = self.seed)
        if self.show == True:
            ps = nx.drawing.layout.spring_layout(er, seed = self.seed)
            nx.draw(er, ps, with_labels = with_labels)
            plt.show()
        return er


    def new_BANet(self, nodes, new_growing_edges, with_labels = True):
        """
        @pram node : 网络节点个数
        @pram new_growing_edges : 新增节点需要与已有节点们生成的连边数量
        """
        ba = nx.generators.barabasi_albert_graph(nodes, new_growing_edges, seed = self.seed)
        self.curr_network = Graph(ba, seed = self.seed)
        if self.show == True:
            ps = nx.drawing.layout.spring_layout(ba, seed = self.seed)
            nx.draw(ba, ps, with_labels = with_labels)
            plt.show()
        return ba

    # 获取当前图结构
    def get_curr_network(self):
        return self.curr_network
    
    # 获取当前图结构列表
    def get_curr_netlist(self):
        return self.curr_netlist[:]

    def netlist_push(self, network = None):
        if network != None:
            self.curr_netlist.append(network)
        elif self.curr_network not in self.curr_netlist:
            self.curr_netlist.append(self.curr_network)

    def netlist_pop(self, idx = -1):
        self.curr_netlist.pop(idx)


    """
    接下来需要设计函数获取当前图的各种静态属性, 然后绘制显示出来!
    不过这些图本身的属性其实应当划分至其本身,通过图本身提供的接口获取!
    """
    
    # 把所有可能的静态属性都给计算一遍
    def get_curr_network_static_prop(self, graph = None):
        graph.get_static_prop()



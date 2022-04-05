## 用于对网络发起攻击,测试网络受到攻击之后的性质
import numpy as np
import networkx as nx

def specific_attack(graph, centrality_metric = nx.degree_centrality):
    graph = graph.copy()
    steps = 0
    ranks = centrality_metric(graph)
    nodes = sorted(graph.nodes(), key = lambda n: ranks[n])
    while nx.is_connected(graph):
        graph.remove_node(nodes.pop())
        steps += 1
    return steps


def random_attack(graph):
    graph = graph.copy()
    steps = 0
    nodes = graph.nodes()
    while nx.is_connected(graph):
        node = np.random.choice(nodes)
        graph.remove_node(node)
        steps += 1
    return steps
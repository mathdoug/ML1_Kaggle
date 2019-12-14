import networkx as nx
from src.setup.toGraph import toGraph


def cnn(graph):
    return nx.cn_soundarajan_hopcroft(graph)


if __name__ == "__main__":
    graph = toGraph()

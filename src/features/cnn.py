import networkx as nx
from src.setup.creation_graph_dataframe import creation_graph_dataframe


def cnn(graph):
    return nx.cn_soundarajan_hopcroft(graph)


if __name__ == "__main__":
    graph = creation_graph_dataframe()

import networkx as nx
from src.toGraph.toGraph import toGraph


def jaccard_coefficient(graph):
    return nx.jaccard_coefficient(graph)


if __name__ == "__main__":
    graph = toGraph()
    print(jaccard_coefficient(graph))

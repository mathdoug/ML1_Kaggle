import networkx as nx
from src.setup.creation_graph_dataframe import creation_graph_dataframe


def jaccard_coefficient(graph):
    return nx.jaccard_coefficient(graph)


if __name__ == "__main__":
    graph = creation_graph_dataframe()
    print(jaccard_coefficient(graph))

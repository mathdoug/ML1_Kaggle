import networkx as nx
from src.setup.creation_graph_dataframe import creation_graph_dataframe


def jaccard_coefficient(graph):
    jaccard = []

    with open('../../data/training.txt', "r") as f:
        for line in f:
            line = line.split()
            for u,v,p in nx.jaccard_coefficient(graph, [(line[0], line[1])]):
                jaccard.append(p)
                print(jaccard[-1])
    return jaccard


if __name__ == "__main__":
    graph = creation_graph_dataframe()
    print(jaccard_coefficient(graph))
    #print(jaccard_coefficient(graph))

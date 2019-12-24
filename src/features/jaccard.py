import networkx as nx
from src.setup.creation_graph_dataframe import creation_graph_dataframe


def jaccard_coefficient(graph, df):
    jaccard = []

    with open('../../data/training.txt', "r") as f:
        for line in f:
            line = line.split()
            for u,v,p in nx.jaccard_coefficient(graph, [(line[0], line[1])]):
                jaccard.append(p)

    df["Jaccard"] = jaccard
    return


if __name__ == "__main__":
    graph, df_train, df_test = creation_graph_dataframe()
    jaccard_coefficient(graph, df_train)
    print("com Jaccard: \n", df_train.head())


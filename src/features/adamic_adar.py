import networkx as nx
import pandas as pd
from src.setup.creation_graph_dataframe import creation_graph_dataframe


def adamic_adar(graph, df):
    aa = []

    with open('../../data/training.txt', "r") as f:
        for line in f:
            line = line.split()
            for u, v, p in nx.adamic_adar_index(graph, [(line[0], line[1])]):
                aa.append(p)

    df["Adamic-Adar"] = aa
    return

if __name__ == "__main__":
    graph, df_train, df_test = creation_graph_dataframe()
    adamic_adar(graph, df_train)
    print("com Adamic-Adar: \n", df_train.head())
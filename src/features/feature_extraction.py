import networkx as nx
import numpy as np
from src.setup.creation_graph_dataframe import creation_graph_dataframe


def feature_extraction(graph, df):
    jaccard = []
    adamic_adar = []        #Adamic-Adar inde
    pa = []     #preferential attachment

    with open('../../data/training.txt', "r") as f:
        for line in f:
            line = line.split()
            for u,v,p in nx.jaccard_coefficient(graph, [(line[0], line[1])]):
                jaccard.append(p)
            for u,v,p in nx.adamic_adar_index(graph, [(line[0], line[1])]):
                adamic_adar.append(p)
            for u,v,p in nx.jaccard_coefficient(graph, [(line[0], line[1])]):
                jaccard.append(p)
            for u,v,p in nx.preferential_attachment(graph, [(line[0], line[1])]):
                pa.append(p)

    df["Jaccard"] = jaccard
    df["Adamic-Adar"] = adamic_adar
    df["Preferential Attachment"] = pa

    np.savetxt('../data/df_train.txt', df.values)
    return

if __name__ == "__main__":
    graph, df_train, df_test = creation_graph_dataframe()
    feature_extraction(graph, df_train)
    print(df_train.head())
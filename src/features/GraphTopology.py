import networkx as nx
import numpy as np
import pandas as pd
import os
from src.setup.setup import Setup


class GraphTopology:
    def fit(graph, df_train, df_test):
        """
        Detail:
            It adds the metric coefficients and the neighbor coefficients as columns in the dataset
        Arguments:
            graph -> nx.Graph()
            df_train -> pd.DataFrame()
            df_test -> pd.DataFrame()
        Return:
            df_train -> pd.DataFrame()
            df_test -> pd.DataFrame()

        """
        df_train, df_test = GraphTopology.metric_coefficients(graph, df_train, df_test)
        df_train, df_test = GraphTopology.neighborhood_coefficients(graph, df_train, df_test)
        return df_train, df_test

    def metric_coefficients(graph, df_train, df_test):
        """
        Detail:
            It computes the metric coefficients like jaccard, adamic,preferential attachment and resource allocation
        Arguments:
            graph -> nx.Graph()
            df_train -> pd.DataFrame()
            df_test -> pd.DataFrame()
        Return:
            df_train -> pd.DataFrame()
            df_test -> pd.DataFrame()

        """
        filename_testing = os.path.join(Setup.path_project(__file__), "data", "testing.txt")
        filename_training = os.path.join(Setup.path_project(__file__), "data", "training.txt")

        for filename, df in zip([filename_training, filename_testing], [df_train, df_test]):
            jaccard = []
            adamic_adar = []  # Adamic-Adar inde
            pa = []  # preferential attachment
            ra = []  # resource allocation

            with open(filename, "r") as f:
                for line in f:
                    line = line.split()
                    for u, v, p in nx.jaccard_coefficient(graph, [(line[0], line[1])]):
                        jaccard.append(p)
                    for u, v, p in nx.adamic_adar_index(graph, [(line[0], line[1])]):
                        adamic_adar.append(p)
                    for u, v, p in nx.preferential_attachment(graph, [(line[0], line[1])]):
                        pa.append(p)
                    for u, v, p in nx.resource_allocation_index(graph, [(line[0], line[1])]):
                        ra.append(p)

            df["Jaccard"] = jaccard
            df["Adamic-Adar"] = adamic_adar
            df["Preferential Attachment"] = pa
            df["Resource Allocation"] = ra

        return df_train, df_test

    def neighborhood_coefficients(graph, df_train, df_test):
        """
        Detail:
            It computes the neighborhood coefficients like common neighbors, salton index and sorensen index
        Arguments:
            graph -> nx.Graph()
            df_train -> pd.DataFrame()
            df_test -> pd.DataFrame()
        Return:
            df_train -> pd.DataFrame()
            df_test -> pd.DataFrame()

        """
        def intersection(lst1, lst2):
            return list(set(lst1) & set(lst2))

        filename_testing = os.path.join(Setup.path_project(__file__), "data", "testing.txt")
        filename_training = os.path.join(Setup.path_project(__file__), "data", "training.txt")

        for filename, df in zip([filename_training, filename_testing], [df_train, df_test]):
            cn = []  # common neighbors
            si = []  # salton index
            sorI = []  # sorensen index

            with open(filename, "r") as f:
                for line in f:
                    line = line.split()

                    n1 = graph.neighbors(line[0])
                    n2 = graph.neighbors(line[1])
                    inter = len(intersection(n1, n2))

                    cn.append(inter)
                    if graph.degree(line[0]) != 0 and graph.degree(line[1]) != 0:
                        si.append(inter / np.sqrt(graph.degree(line[0]) * graph.degree(line[1])))
                    else:
                        si.append(0)
                    sorI.append(2 * inter / (graph.degree(line[0]) + graph.degree(line[1])))

            df["Common Neighbors"] = cn
            df["Salton Index"] = si
            df["Sorensen Index"] = sorI

        return df_train, df_test


if __name__ == "__main__":
    graph, df_train, df_test = Setup.creation_graph_dataframe()

    print("### Data train:\n")
    print(df_train.head())
    print("\n### Data test:\n")
    print(df_test.head())

    df_train, df_test = GraphTopology.metric_coefficients(graph, df_train, df_test)
    print("\n####### After metric coefficients:\n")
    print("### Data train:\n")
    print(df_train.head())
    print("\n### Data test:\n")
    print(df_test.head())

    df_train, df_test = GraphTopology.neighborhood_coefficients(graph, df_train, df_test)
    print("\n####### After neighborhood coefficients:\n")
    print("### Data train:\n")
    print(df_train.head())
    print("\n### Data test:\n")
    print(df_test.head())

    df_train.to_csv(os.path.join(Setup.path_project(__file__), "data", "data_train_aux.txt"))
    df_test.to_csv(os.path.join(Setup.path_project(__file__), "data", "data_test_aux.txt"))

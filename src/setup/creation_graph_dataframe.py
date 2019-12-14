import networkx as nx
import os
import pandas as pd


def creation_graph_dataframe():
    """
    Detail:
        The function return the graph of the data training.txt and the dataframe of the train and the test
    Arguments:
        None
    return:
        graph -> nx.Graph()
        df_train -> pd.DataFrame()
        df_test -> pd.DataFrame()
    """

    # Find the location of data
    filename_training = __file__
    while os.path.basename(filename_training) != "ML1_Kaggle":
        filename_training = os.path.dirname(filename_training)
    filename_testing = os.path.join(filename_training, "data", "testing.txt")
    filename_training = os.path.join(filename_training, "data", "training.txt")

    # Creation of the graph_train
    graph = nx.Graph()
    with open(filename_training, "r") as f:
        for line in f:
            line = line.split()
            if line[2] == '1':
                graph.add_edge(line[0], line[1])
            else:
                graph.add_nodes_from([line[0], line[1]])

    # Creation of the dataframes
    df_train = pd.read_csv(filename_training, sep=" ", header=None)
    df_train.columns = ["node_1", "node_2", "output"]

    df_test = pd.read_csv(filename_testing, sep=" ", header=None)
    df_test.columns = ["node_1", "node_2"]

    return graph, df_train, df_test


if __name__ == "__main__":
    graph, df_train, df_test = creation_graph_dataframe()

    print("The graph of the data training was created.")
    print("Information of the training graph:")
    print("\tNumber of nodes: {}".format(graph.number_of_nodes()))
    print("\tNumber of edges: {}".format(graph.number_of_edges()))

    print("\nData Frame train:\n", df_train.head())
    print("\nShape:", df_train.shape)

    print("\nData Frame test:\n", df_test.head())
    print("\nShape:", df_test.shape)


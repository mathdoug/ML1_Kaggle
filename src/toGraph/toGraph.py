import networkx as nx


def toGraph():
    """
    Detail:
        The function return the graph of the data training.txt
    Arguments:
        file_training -> string
    return:
        graph -> nx.Graph()
    """
    filename_training = ""
    if __name__ == "__main__":
        filename_training += "../../data/training.txt"
    else:
        filename_training += "../data/training.txt"

    graph_train = nx.Graph()
    with open(filename_training, "r") as f:
        for line in f:
            line = line.split()
            if line[2] == '1':
                graph_train.add_edge(line[0], line[1])
            else:
                graph_train.add_nodes_from([line[0], line[1]])
    return graph_train


if __name__ == "__main__":
    graph = toGraph()
    print("The graph of the data training was created.")
    print("Information of the training graph:")
    print("\tNumber of nodes: {}".format(graph.number_of_nodes()))
    print("\tNumber of edges: {}".format(graph.number_of_edges()))


from src.toGraph.toGraph import toGraph

if __name__=="__main__":
    # Taking the graph of training and testing
    G = toGraph()
    print(G.number_of_nodes())
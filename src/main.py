from src.setup.creation_graph_dataframe import creation_graph_dataframe

"""
Our program occurs in this file
"""

if __name__=="__main__":
    # Taking the graph of training
    G = creation_graph_dataframe()
    print(G.number_of_nodes())
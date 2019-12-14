from src.setup.creation_graph_dataframe import creation_graph_dataframe

"""
Our program occurs in this file
"""

if __name__=="__main__":
    # Taking the graph and the teste of training
    graph, df = creation_graph_dataframe()
    print(graph.number_of_nodes())
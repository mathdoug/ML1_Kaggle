import networkx as nx
import pandas as pd
from src.setup.creation_graph_dataframe import creation_graph_dataframe


def adamic_adar(graph, df):
    aa = []

    for index, row in df.iterrows():
        for u,v,p in nx.adamic_adar_index(graph,[(row[])])

    for line in f:
            line = line.split()
            for u,v,p in nx.adamic_adar_index(graph, [(line[0], line[1])]):
                aa.append(p)
                print(aa[-1])
    df['Adamic Adar'] = aa
    return aa
from src.setup.setup import Setup
from src.features.GraphTopology import GraphTopology
from src.models.OurModel import OurModel
import os
import pandas as pd

"""
Our program occurs in this file
"""

if __name__=="__main__":
    # Taking the graph and the teste of training
    graph, df_train, df_test = Setup.creation_graph_dataframe()

    # Feature Engineering
    df_train, df_test = GraphTopology.fit(graph, df_train, df_test)

    # Modelling and Evaluation
    ourModel = OurModel()
    ourModel.performance(df_train)
    ourModel.fit(df_train)

    # Prediction
    pred = ourModel.predict(df_test)
    pred = pd.DataFrame(pred)
    pred.columns = ["predicted"]
    pred.index.name = "id"

    # CSV
    pred.to_csv(os.path.join(Setup.path_project(__file__), "data", "predictions.csv"))

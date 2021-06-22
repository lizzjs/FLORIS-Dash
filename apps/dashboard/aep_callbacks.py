
from dash.dependencies import Input, Output, State
from floris.simulation import floris
import pandas as pd
import plotly.express as px
import numpy as np

from app import app
import apps.floris_data


@app.callback(
    Output('compute-time-graph', 'figure'),
    Input("floris-outputs", "data")
)
def create_dashboard_plots(floris_output_data):
    columns = ["Model Name", "Compute Time"]
    model_name = apps.floris_data.default_input_dict["wake"]["properties"]["velocity_model"]
    values = [[model_name, floris_output_data[model_name]]]
    df = pd.DataFrame(values, columns=columns)
    fig1 = px.bar(
        df,
        x=columns[0],
        y=columns[1],
        template="seaborn",
        title="Power Curve"
    )
    return fig1

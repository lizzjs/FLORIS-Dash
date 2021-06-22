
from dash.dependencies import Input, Output, State
from floris.simulation import floris
import pandas as pd
import plotly.express as px
import numpy as np

from app import app
import apps.floris_data


@app.callback(
    Output('model-comparison-grpah', 'figure'),
    Output('compute-time-graph', 'figure'),
    Input("floris-outputs", "data")
)
def create_dashboard_plots(floris_output_data):

    # FLORIS AEP with and without wake steering
    columns = ["Real AEP"], #"Ideal AEP", "Optimal AEP"]
    model_name = apps.floris_data.default_input_dict["wake"]["properties"]["velocity_model"] #change this
    values = [[model_name, floris_output_data[model_name]]]
    df = pd.DataFrame(values, columns=columns)

    fig1 = px.scatter(
        df,
        x=columns[0],
        y=columns[1],
        template="seaborn",
        title="FLORIS AEP with and without Wake Steering"
    )

    # Compute time
    columns_ct = ["Model Name", "Compute Time"]
    model_name_ct = apps.floris_data.default_input_dict["wake"]["properties"]["velocity_model"]
    values = [[model_name_ct, floris_output_data[model_name_ct]]]
    df2 = pd.DataFrame(values, columns=columns_ct)
    fig2 = px.bar(
        df2,
        x=columns_ct[0],
        y=columns_ct[1],
        template="seaborn",
        title="Compute Time"
    )
    return fig1, fig2


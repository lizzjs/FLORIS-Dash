
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

from app import app
import apps.floris_data


@app.callback(
    Output('wind-rose-graph', 'figure'),
    Input('wind-rose-datatable', 'data')
)
def create_wind_rose_plot(data):
    df = pd.DataFrame(data)
    fig = px.bar_polar(
        df,
        r="frequency",
        theta="direction",
        color="strength",
        template="seaborn",
        color_discrete_sequence=px.colors.sequential.Plasma_r,
        title="Wind Rose"
    )
    return fig

@app.callback(
    Output('wind-rose-datatable', 'data'),
    Output('wind-rose-datatable', 'columns'),
    Input('wind-rose-datatable', 'data')
)
def get_wind_rose_table_data(data):
    if data is None:
        df = pd.DataFrame(apps.floris_data.wind_rose_data)
    else:
        df = pd.DataFrame(data)

    columns = [{"name": i, "id": i} for i in df.columns]
    return df.to_dict("rows"), columns


from dash.dependencies import Input, Output, State
import io
import pandas as pd
from app import app, colors
import base64
import dash_html_components as html
import plotly.express as px


@app.callback(
    [Output('wind-datatable-interactivity', 'data'),
    Output('wind-datatable-interactivity', 'columns')],
    [Input('wind-upload-data', 'contents'),
    Input('wind-upload-data', 'filename')]
)
def display_table_windrose(contents, filename):
    _module_df = pd.DataFrame({})

    if contents is not None:
        contents = contents[0]
        filename = filename[0]
        _module_df = parse_contents(contents, filename)

    columns = [{"name": i, "id": i} for i in _module_df.columns]
    return _module_df.to_dict("rows"), columns # table #, fig
    

@app.callback(
    Output('wind-rose-chart', 'figure'),
    Input('wind-datatable-interactivity', 'data')
)
def display_figure_windrose(data):
    return px.bar_polar(
        pd.DataFrame(data),
        r="frequency",
        theta="direction",
        color="strength",
        template="seaborn",
        color_discrete_sequence=px.colors.sequential.Plasma_r
    )

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    
    if 'xls' in filename:
        # Assume that the user uploaded an excel file
        df = pd.read_excel(io.BytesIO(decoded))

    else:
        pass

    return df


import dash
from dash.dependencies import Input, Output, State
# import plotly.graph_objs as go
import io
import pandas as pd

from app import app, colors

import dash_table
import base64
import dash_html_components as html
import plotly.express as px

@app.callback(
    Output('wind-table-data-output', 'children'),
    Output('wind-rose-chart', 'figure'),
    [Input('wind-upload-data', 'contents'),
    Input('wind-upload-data', 'filename')]
)
def display_table_windrose(contents, filename):
    table = html.Div()
    fig = px.bar_polar()

    if contents:
        contents = contents[0]
        filename = filename[0]
        df = parse_contents(contents, filename)

        table = html.Div(
            [
                html.H5(filename),
                dash_table.DataTable(
                    id = 'wind-datatable-interactivity',
                    data=df.to_dict("rows"),
                    columns=[{"name": i, "id": i} for i in df.columns],
                    editable=True,
                    cell_selectable=True,
                    column_selectable="multi",  # allow users to select 'multi' or 'single' columns
                    row_selectable="multi",     # allow users to select 'multi' or 'single' rows
                    row_deletable=True,         # choose if user can delete a row (True) or not (False)
                    selected_columns=[],        # ids of columns that user selects
                    selected_rows=[],           # indices of rows that user selects
                    page_action="none",         # all data is passed to the table up-front or not ('none')
                    style_table={'height': '300px', 'overflowY': 'auto'},
                ),
            ]
        )
        
        fig = px.bar_polar(df, r="frequency", theta="direction",
                   color="strength", template="seaborn",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)

    return table, fig

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    
    if 'xls' in filename:
        # Assume that the user uploaded an excel file
        df = pd.read_excel(io.BytesIO(decoded))

    else:
        pass

    return df
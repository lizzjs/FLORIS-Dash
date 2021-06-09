
import dash
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import io
import pandas as pd

import dash_table
import base64
import dash_html_components as html

from app import app

@app.callback(
    Output('editing-table-data-output', 'children'),
    [Input('home-upload-data', 'contents'),
    Input('home-upload-data', 'filename')]
)
def display_table(contents, filename):
    #TODO move 'layout' contents to home.py? Tried but failed
    #TODO check if edited cells are saved
    table = html.Div()

    if contents:
        contents = contents[0]
        filename = filename[0]
        df = parse_contents(contents, filename)

        table = html.Div(
            [
                html.H5(filename),
                dash_table.DataTable(
                    id = 'datatable-interactivity',
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
        print(df)
    return table

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    
    if 'xls' in filename:
        # Assume that the user uploaded an excel file
        df = pd.read_excel(io.BytesIO(decoded), sheet_name='cpctws')
        #TODO make separate dataframes for each sheet or do that in update_table method?
    else:
        pass

    return df
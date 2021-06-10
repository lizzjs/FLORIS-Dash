
import dash
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import io
import pandas as pd

import base64
import dash_html_components as html
import json

from app import app

@app.callback(
    [Output('homepage-datatable', 'data'),
    Output('homepage-datatable', 'columns')],
    [Input('home-upload-data', 'contents'),
    Input('home-upload-data', 'filename')],
    [Input('json-upload-data', 'contents'),
    Input('json-upload-data', 'filename')]
)
def display_table(contents, filename, jcontents, jfilename):
    _module_df = pd.DataFrame({})

    if contents is not None:
        contents = contents[0]
        filename = filename[0]
        _module_df = parse_contents(contents, filename)
    elif jcontents is not None:
        contents = jcontents[0]
        filename = jfilename[0]
        _module_df = parse_contents(contents, filename)
    # print(_module_df)
    columns = [{"name": i, "id": i} for i in _module_df.columns]
    return _module_df.to_dict("rows"), columns

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    # print(decoded)
    if 'xls' in filename:
        # Assume that the user uploaded an excel file
        df = pd.read_excel(io.BytesIO(decoded), sheet_name='cpctws')
    elif 'json' in filename:
        data = json.loads(decoded)

        df = pd.DataFrame(data["turbine"]["properties"]["power_thrust_table"])

    else:
        raise ValueError("The file imported was not in the expected file format.")

    return df
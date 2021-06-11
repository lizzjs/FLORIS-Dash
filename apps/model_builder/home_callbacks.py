
import base64
from dash.dependencies import Input, Output
import dash_html_components as html
import io
import json
import pandas as pd

from app import app
from apps.floris_inputs import user_defined_dict

from .utils import parse_contents

# @app.callback(
#     [Output('homepage-datatable', 'data'),
#     Output('homepage-datatable', 'columns')],
#     [Input('home-upload-list-data', 'contents'),
#     Input('home-upload-list-data', 'filename')],
# )
# def display_table(contents, filename):

#     _module_df = pd.DataFrame({})

#     if contents is not None:
#         contents = contents[0]
#         filename = filename[0]
#         _module_df = parse_contents(contents, filename)

#     columns = [{"name": i, "id": i} for i in _module_df.columns]
#     return _module_df.to_dict("rows"), columns


@app.callback(
    Output('homepage-datatable', 'children'),
    [Input('json-upload-input-file', 'contents'),
    Input('json-upload-input-file', 'filename')]
)
def load_json_input_file(contents, filename):
    if contents is not None:
        try:
            # decoded = base64.b64decode(contents[0]).decode('utf-8', "replace")
            # print("decoded", decoded)
            # iostring = io.StringIO(decoded)
            # print("iostring", iostring)
            # data = json.loads(io.StringIO(decoded))
            # print("data", data)
            data = json.load( open("test_data/" + filename[0], 'r') )
            user_defined_dict = data
            print(user_defined_dict)
            return data
        except Exception as e:
            print(e)
            return html.Div(['There was an error processing this file.'])

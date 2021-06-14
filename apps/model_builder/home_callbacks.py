
import base64
from dash.dependencies import Input, Output
import dash_html_components as html
import io
import json
import pandas as pd

from app import app
import apps.floris_data
import time


# @app.callback(
#     Output('homepage-datatable', 'children'),
#     [Input('json-upload-input-file', 'contents'),
#     Input('json-upload-input-file', 'filename')]
# )
# def load_json_input_file(contents, filename):
#     if contents is not None:
#         try:
#             # decoded = base64.b64decode(contents[0]).decode('utf-8', "replace")
#             # print("decoded", decoded)
#             # iostring = io.StringIO(decoded)
#             # print("iostring", iostring)
#             # data = json.loads(io.StringIO(decoded))
#             # print("data", data)
#             data = json.load( open("test_data/" + filename[0], 'r') )
#             apps.floris_inputs.user_defined_dict = data
#             return data
#         except Exception as e:
#             print(e)
#             return html.Div(['There was an error processing this file.'])
            
@app.callback(
    Output("jloading-output", "children"),
    [Input('json-upload-input-file', 'contents'),
    Input('json-upload-input-file', 'filename')], 
    Input("jupload-button", "n_clicks"),
)
def load_output(contents, filename, n):
    if n:
        time.sleep(1)
        return f"{filename} uploaded"
    elif n==None:
        return f"Upload file" 
    return "Upload unsuccessful"
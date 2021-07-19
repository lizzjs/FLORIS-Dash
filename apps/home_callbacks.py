
import base64
import dash
from dash.dependencies import Input, Output
import json

from app import app
import apps.floris_data
import time


@app.callback(
    Output('initial-input-store', 'data'),
    Output('label-input-file', 'children'),
    Output('button-start-model-builder', 'disabled'),
    Output('button-skip-to-review', 'disabled'),
    Input('button-load-defaults', 'n_clicks'),
    Input('upload-input-file', 'contents'),
    Input('upload-input-file', 'filename')
)
def store_input_data(_, contents, filename):

    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if trigger_id == "button-load-defaults":
        return apps.floris_data.default_input_dict, "No input file selected.", True, True

    elif trigger_id == "upload-input-file":
        if filename is None:
            return None, "No input file selected.", True, True

        content_type, content_string = contents.split(',')
        try:
            decoded = base64.b64decode(content_string).decode('utf-8')
            data = json.loads(decoded)
            return data, filename, False, False
        except Exception as e:
            print(e)
            return None, e, False, False

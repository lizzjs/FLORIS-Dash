
import base64
from dash.dependencies import Input, Output
import dash_html_components as html
import json

from app import app
import time


@app.callback(
    Output('floris-inputs', 'data'),
    Output('label-input-file', 'children'),
    Output('button-start-model-builder', 'disabled'),
    Output('button-skip-to-review', 'disabled'),
    Input('json-upload-input-file', 'contents'),
    Input('json-upload-input-file', 'filename')
)
def load_json_input_file(contents, filename):
    if filename is None:
        return {}, "No input file selected.", True, True

    content_type, content_string = contents.split(',')
    try:
        time.sleep(1)
        decoded = base64.b64decode(content_string).decode('utf-8')
        data = json.loads(decoded)
        return data, filename, False, False
    except Exception as e:
        print(e)
        return {}, e, False, False


import base64
from dash.dependencies import Input, Output
import dash_html_components as html
import json

from app import app
import time


@app.callback(
    Output('floris-inputs', 'data'),
    Output("jloading-output", "children"),
    Input('json-upload-input-file', 'contents'),
    Input('json-upload-input-file', 'filename')
)
def load_json_input_file(contents, filename):
    if contents is None:
        return {}, html.Div()

    content_type, content_string = contents.split(',')
    try:
        time.sleep(1)
        decoded = base64.b64decode(content_string).decode('utf-8')
        data = json.loads(decoded)
        return data, html.Div([f'Successfully uploaded {filename}'])
    except Exception as e:
        print(e)
        return {}, html.Div([f'There was an error processing {filename}: {e}.'])

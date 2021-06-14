
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html

from app import app
from apps.floris_inputs import default_input_dict
import time

@app.callback(
    Output("loading-output", "children"), [Input("loading-button", "n_clicks")]
)
def load_output(n):
    if n:
        time.sleep(1)
        return f"Output loaded {n} times"
    return "Output not reloaded yet"
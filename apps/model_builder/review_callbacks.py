
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html

from app import app
import time

from apps.floris_connection.run_floris import calculate_wake
import apps.floris_data

@app.callback(
    # Output("loading-output", "children"),
    Output("floris-outputs", "data"),
    Input("submit-button", "n_clicks"),
    State("floris-outputs", "data")
)
def load_output(n, floris_output_data):
    time.sleep(1)
    compute_time = calculate_wake(apps.floris_data.default_input_dict)
    model_name = apps.floris_data.default_input_dict["wake"]["properties"]["velocity_model"]
    floris_output_data = {
        model_name: compute_time
    }
    return floris_output_data

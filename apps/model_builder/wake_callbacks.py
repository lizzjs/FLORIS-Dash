
import dash
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import numpy as np

from app import app
import apps.floris_data
from floris.tools.floris_interface import FlorisInterface
from graph_generator import *

def _get_wake_definition(key, value, initial_input_store, wake_store):
    # On first load
    if value is None:
        if wake_store is not None:
            if key in wake_store:
                return wake_store[key]

        if initial_input_store is None:
            # TODO: Do we leave this? This handles the situation when the input store is not available for any reason.
            initial_input_store = apps.floris_data.default_input_dict
        return initial_input_store["wake"]["properties"][key]
    # On every other call, return the value in the field
    return value


@app.callback(
    Output('radio-deficit', 'value'),
    Output('radio-deflection', 'value'),
    Output('radio-turbulence', 'value'),
    Output('radio-combination', 'value'),
    Output("collapse-models", "is_open"),
    Input("collapse-model-button", "n_clicks"),
    Input('radio-deficit', 'value'),
    Input('radio-deflection', 'value'),
    Input('radio-turbulence', 'value'),
    Input('radio-combination', 'value'),
    State("collapse-models", "is_open"),
    State('initial-input-store', 'data'),
    State('wake-input-store', 'data')
)
def toggle_model(n, velocity_value, deflection_value, turbulence_value, combination_value, is_open, initial_input_store, wake_store):
    velocity_value = _get_wake_definition("velocity_model", velocity_value, initial_input_store, wake_store)
    deflection_value = _get_wake_definition("deflection_model", deflection_value, initial_input_store, wake_store)
    turbulence_value = _get_wake_definition("turbulence_model", turbulence_value, initial_input_store, wake_store)
    combination_value = _get_wake_definition("combination_model", combination_value, initial_input_store, wake_store)

    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if trigger_id == "collapse-model-button":
        is_open = not is_open

    return velocity_value, deflection_value, turbulence_value, combination_value, is_open


@app.callback(
    Output('velocity-parameter-datatable', 'data'),
    Output('velocity-parameter-datatable', 'columns'),
    Output('deflection-parameter-datatable', 'data'),
    Output('deflection-parameter-datatable', 'columns'),
    Output('turbulence-parameter-datatable', 'data'),
    Output('turbulence-parameter-datatable', 'columns'),
    Output("collapse-parameters", "is_open"),
    Output('velocity-param-label', 'children'),
    Output('deflection-param-label', 'children'),
    Output('turbulence-param-label', 'children'),
    Input("collapse-parameter-button", "n_clicks"),
    Input('radio-deficit', 'value'),
    Input('radio-deflection', 'value'),
    Input('radio-turbulence', 'value'),
    Input('radio-combination', 'value'),
    State("collapse-parameters", "is_open"),
)
def toggle_parameters(n, velocity_value, deflection_value, turbulence_value, combination_value, is_open):
    velocity_label = velocity_value.capitalize()
    deflection_label = deflection_value.capitalize()
    turbulence_label = turbulence_value.capitalize()

    fi = FlorisInterface(input_dict=apps.floris_data.default_input_dict)
    fi.floris.farm.wake.velocity_model = velocity_value
    fi.floris.farm.wake.deflection_model = deflection_value
    fi.floris.farm.wake.turbulence_model = turbulence_value
    fi.floris.farm.wake.combination_model = combination_value
    params = fi.get_model_parameters()

    vel_columns = [{"name": i, "id": i} for i in ["Parameter", "Value"]]
    vel_values = [ {"Parameter": k, "Value": v} for k, v in params["Wake Velocity Parameters"].items() ]

    def_columns = [{"name": i, "id": i} for i in ["Parameter", "Value"]]
    def_values = [ {"Parameter": k, "Value": v} for k, v in params["Wake Deflection Parameters"].items() ]

    turb_columns = [{"name": i, "id": i} for i in ["Parameter", "Value"]]
    turb_values = [ {"Parameter": k, "Value": v} for k, v in params["Wake Turbulence Parameters"].items() ]

    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if trigger_id == "collapse-parameter-button":
        is_open = not is_open

    return vel_values, vel_columns, def_values, def_columns, turb_values, turb_columns, is_open, velocity_label, deflection_label, turbulence_label


@app.callback(
    Output("wake-model-preview-graph", "figure"),
    Input('radio-deficit', 'value'),
    Input('radio-deflection', 'value'),
    Input('radio-turbulence', 'value'),
    Input('radio-combination', 'value'),
    Input('velocity-parameter-datatable', 'data'),
    Input('deflection-parameter-datatable', 'data'),
)
def preview_wake_model(velocity_value, deflection_value, turbulence_value, combination_value, velocity_table_data, deflection_table_data):
    model_parameters_dict = {
        "Wake Velocity Parameters": {},
        "Wake Deflection Parameters": {}
    }
    if velocity_table_data is not None:
        for row in velocity_table_data:
            model_parameters_dict["Wake Velocity Parameters"][row["Parameter"]] = row["Value"]
    if deflection_table_data is not None:
        for row in deflection_table_data:
            model_parameters_dict["Wake Deflection Parameters"][row["Parameter"]] = row["Value"]

    wake_contour_graph = create_preview_wake_model(velocity_value, deflection_value, turbulence_value, combination_value, model_parameters_dict)

    return wake_contour_graph


## Wake definition store

@app.callback(
    Output('wake-input-store', 'data'),
    Input('radio-deficit', 'value'),
    Input('radio-deflection', 'value'),
    Input('radio-turbulence', 'value'),
    Input('radio-combination', 'value'),
)
def store_turbine_definition(velocity_value, deflection_value, turbulence_value, combination_value):
    wake_data = {
        "velocity_model": velocity_value,
        "combination_model": combination_value,
        "deflection_model": deflection_value,
        "turbulence_model": turbulence_value,
    }
    return wake_data

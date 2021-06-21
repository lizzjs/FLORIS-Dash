
import dash
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import numpy as np

from app import app
import apps.floris_data
from floris.tools.floris_interface import FlorisInterface

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
)
def toggle_model(n, velocity_value, deflection_value, turbulence_value, combination_value, is_open):

    apps.floris_data.user_defined_dict["wake"]["properties"]["velocity_model"] = velocity_value
    apps.floris_data.user_defined_dict["wake"]["properties"]["deflection_model"] = deflection_value
    apps.floris_data.user_defined_dict["wake"]["properties"]["turbulence_model"] = turbulence_value
    apps.floris_data.user_defined_dict["wake"]["properties"]["combination_model"] = combination_value

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
    Input("collapse-parameter-button", "n_clicks"),
    Input('radio-deficit', 'value'),
    Input('radio-deflection', 'value'),
    Input('radio-turbulence', 'value'),
    Input('radio-combination', 'value'),
    State("collapse-parameters", "is_open"),
)
def toggle_parameters(n, velocity_value, deflection_value, turbulence_value, combination_value, is_open):

    fi = FlorisInterface(input_dict=apps.floris_data.default_input_dict)
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

    return vel_values, vel_columns, def_values, def_columns, turb_values, turb_columns, is_open

@app.callback(
    Output("wake-model-preview-graph", "figure"),
    Input('radio-deficit', 'value'),
    Input('radio-deflection', 'value'),
    Input('radio-turbulence', 'value'),
    Input('radio-combination', 'value'),
)
def preview_wake_model(velocity_value, deflection_value, turbulence_value, combination_value):

    # Using a FLORIS model with two turbines in tandem, show a preview of the wake model settings
    fi = FlorisInterface(input_dict=apps.floris_data.wake_model_preview_dict)
    fi.calculate_wake(yaw_angles=[10.0, 0.0])
    horizontal_slice = fi.get_hor_plane()

    minSpeed = horizontal_slice.df.u.min()
    maxSpeed = horizontal_slice.df.u.max()

    # Reshape to 2d for plotting
    # x1_mesh = horizontal_slice.df.x1.values.reshape(horizontal_slice.resolution[1], horizontal_slice.resolution[0])
    # x2_mesh = horizontal_slice.df.x2.values.reshape(horizontal_slice.resolution[1], horizontal_slice.resolution[0])
    u_mesh = horizontal_slice.df.u.values.reshape(horizontal_slice.resolution[1], horizontal_slice.resolution[0]).astype(np.float64)

    fig = go.Figure(
        data=go.Contour(
            z = u_mesh
        )
    )
    return fig

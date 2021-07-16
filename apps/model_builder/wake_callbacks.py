
import dash
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import numpy as np

from app import app
import apps.floris_data
from floris.tools.floris_interface import FlorisInterface
from graph_generator import *

@app.callback(
    Output("radio-deflection", "options"), 
    Input("radio-deficit", "value"),
)
def update_deflection_radio(radio):
    """
    If multizone in velocity deificit is selected the gauss option in deflection is disabled.
    """
    if "multizone" in radio:
        return [
            {"label": "Jimenez", "value": "jimenez"},
            {"label": "Gauss", "value": "gauss", "disabled": True},
        ]
    else:
        return [
            {"label": "Jimenez", "value": "jimenez"},
            {"label": "Gauss", "value": "gauss"},
        ]

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
    # Input('velocity-parameter-datatable', 'data'),
    # Input('radio-deficit', 'value'),

)
def preview_wake_model(velocity_value, deflection_value, turbulence_value, combination_value):#, velocity_table_data, velocity_model):
    #TODO connect the datatables to the preview figure

    # #convert list data from datatable to dictionary
    # velocity_parameters = {k:v for e in velocity_table_data for (k,v) in e.items()}
    # print(velocity_table_data['Value'])

    # #assign updated values to floris input data
    # apps.floris_data.user_defined_dict["wake"]["properties"]["velocity_model"] = velocity_model
    # apps.floris_data.user_defined_dict["wake"]["properties"]["parameters"]["wake_velocity_parameters"] = velocity_parameters

    # print(apps.floris_data.user_defined_dict["wake"]["properties"]["parameters"]["wake_velocity_parameters"])

    # #attempting to only update when change in the datatable is a trigger
    # # ctx = dash.callback_context
    # # trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    # # if trigger_id == "velocity-parameter-datatable": 
        
    # #     apps.floris_data.user_defined_dict["wake"]["properties"]["velocity_model"] = velocity_model
    # #     apps.floris_data.user_defined_dict["wake"]["properties"]["parameters"]["wake_velocity_parameters"] = velocity_parameters



    wake_contour_graph = create_preview_wake_model(velocity_value, deflection_value, turbulence_value, combination_value)
    
    return wake_contour_graph
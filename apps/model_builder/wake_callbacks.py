
from dash.dependencies import Input, Output

from app import app
import apps.floris_data


@app.callback(Output('radio-deficit', 'value'), Input('radio-deficit', 'value'))
def velocity_deficit(value):
    apps.floris_data.user_defined_dict["wake"]["properties"]["velocity_model"] = value
    return apps.floris_data.user_defined_dict["wake"]["properties"]["velocity_model"]

@app.callback(Output('radio-deflection', 'value'), Input('radio-deflection', 'value'))
def deflection(value):
    apps.floris_data.user_defined_dict["wake"]["properties"]["deflection_model"] = value
    return apps.floris_data.user_defined_dict["wake"]["properties"]["deflection_model"]

@app.callback(Output('radio-turbulence', 'value'), Input('radio-turbulence', 'value'))
def turbulence(value):
    apps.floris_data.user_defined_dict["wake"]["properties"]["turbulence_model"] = value
    return apps.floris_data.user_defined_dict["wake"]["properties"]["turbulence_model"]

@app.callback(Output('radio-combination', 'value'), Input('radio-combination', 'value'))
def combination(value):
    apps.floris_data.user_defined_dict["wake"]["properties"]["combination_model"] = value
    return apps.floris_data.user_defined_dict["wake"]["properties"]["combination_model"]

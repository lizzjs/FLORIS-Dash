
from dash.dependencies import Input, Output, State

from app import app
import apps.floris_data


# @app.callback(Output('radio-deficit', 'value'), Input('radio-deficit', 'value'))
# def velocity_deficit(value):
#     apps.floris_data.user_defined_dict["wake"]["properties"]["velocity_model"] = value
#     return apps.floris_data.user_defined_dict["wake"]["properties"]["velocity_model"]

# @app.callback(Output('radio-deflection', 'value'), Input('radio-deflection', 'value'))
# def deflection(value):
#     apps.floris_data.user_defined_dict["wake"]["properties"]["deflection_model"] = value
#     return apps.floris_data.user_defined_dict["wake"]["properties"]["deflection_model"]

# @app.callback(Output('radio-turbulence', 'value'), Input('radio-turbulence', 'value'))
# def turbulence(value):
#     apps.floris_data.user_defined_dict["wake"]["properties"]["turbulence_model"] = value
#     return apps.floris_data.user_defined_dict["wake"]["properties"]["turbulence_model"]

# @app.callback(Output('radio-combination', 'value'), Input('radio-combination', 'value'))
# def combination(value):
#     apps.floris_data.user_defined_dict["wake"]["properties"]["combination_model"] = value
#     return apps.floris_data.user_defined_dict["wake"]["properties"]["combination_model"]

@app.callback(
    Output('radio-deficit', 'value'), Output('radio-deflection', 'value'),
    Output('radio-turbulence', 'value'), Output('radio-combination', 'value'), Output("collapse-all", "is_open"),
    Input("collapse-button", "n_clicks"), Input('radio-deficit', 'value'), Input('radio-deflection', 'value'),
    Input('radio-turbulence', 'value'), Input('radio-combination', 'value'),
    State("collapse-all", "is_open"),
)
def toggle_collapse(n, velocity_value, deflection_value, turbulence_value, combination_value, is_open,):

    print(is_open)

    apps.floris_data.user_defined_dict["wake"]["properties"]["velocity_model"] = velocity_value

    apps.floris_data.user_defined_dict["wake"]["properties"]["deflection_model"] = deflection_value

    apps.floris_data.user_defined_dict["wake"]["properties"]["turbulence_model"] = turbulence_value

    apps.floris_data.user_defined_dict["wake"]["properties"]["combination_model"] = combination_value

    if n:
        # return not is_open, apps.floris_data.user_defined_dict["wake"]["properties"]["velocity_model"]
        return velocity_value, deflection_value, turbulence_value, combination_value, not is_open

    return velocity_value, deflection_value, turbulence_value, combination_value, is_open

from dash.dependencies import Input, Output, State
import pandas as pd

from app import app
from graph_generator import *


## Geometry

def _get_turbine_definition_value(key, value, initial_input_store):
    if initial_input_store is None:
        # TODO: This is a fatal error. How to handle?
        return None

    if value == None:
        return initial_input_store["turbine"]["properties"][key]

    return value


@app.callback(
    Output('input-rotor-diameter', 'value'),
    Input('input-rotor-diameter', 'value'),
    State('initial-input-store', 'data')
)
def rotor_diameter(value, initial_input_store):
    return _get_turbine_definition_value("rotor_diameter", value, initial_input_store)


@app.callback(
    Output('input-hub-height', 'value'),
    Input('input-hub-height', 'value'),
    State('initial-input-store', 'data')
)
def hub_height(value, initial_input_store):
        return _get_turbine_definition_value("hub_height", value, initial_input_store)


@app.callback(
    Output('input-yaw-angle', 'value'),
    Input('input-yaw-angle', 'value'),
    State('initial-input-store', 'data')
)
def yaw_angle(value, initial_input_store):
    return _get_turbine_definition_value("yaw_angle", value, initial_input_store)


@app.callback(
    Output('input-tilt-angle', 'value'),
    Input('input-tilt-angle', 'value'),
    State('initial-input-store', 'data')
)
def tilt_angle(value, initial_input_store):
    return _get_turbine_definition_value("tilt_angle", value, initial_input_store)


@app.callback(
    Output('input-tip-speed-ratio', 'value'),
    Input('input-tip-speed-ratio', 'value'),
    State('initial-input-store', 'data')
)
def tip_speed_ratio(value, initial_input_store):
    return _get_turbine_definition_value("TSR", value, initial_input_store)


@app.callback(
    Output('input-generator-efficiency', 'value'),
    Input('input-generator-efficiency', 'value'),
    State('initial-input-store', 'data')
)
def generator_efficiency(value, initial_input_store):
    return _get_turbine_definition_value("generator_efficiency", value, initial_input_store)


@app.callback(
    Output('input-pP', 'value'),
    Input('input-pP', 'value'),
    State('initial-input-store', 'data')
)
def pP(value, initial_input_store):
    return _get_turbine_definition_value("pP", value, initial_input_store)


@app.callback(
    Output('input-pT', 'value'),
    Input('input-pT', 'value'),
    State('initial-input-store', 'data')
)
def pT(value, initial_input_store):
    return _get_turbine_definition_value("pT", value, initial_input_store)


@app.callback(
    Output('slider-ngrid', 'value'),
    Input('slider-ngrid', 'value'),
    State('initial-input-store', 'data')
)
def ngrid(value, initial_input_store):
    return _get_turbine_definition_value("ngrid", value, initial_input_store)


@app.callback(
    Output('input-rloc', 'value'),
    Input('input-rloc', 'value'),
    State('initial-input-store', 'data')
)
def rloc(value, initial_input_store):
    return _get_turbine_definition_value("rloc", value, initial_input_store)


@app.callback(
    Output('switch-perimeter-points', 'value'),
    Input('switch-perimeter-points', 'value'),
    State('initial-input-store', 'data')
)
def perimeter_points(value, initial_input_store):
    state = _get_turbine_definition_value("use_points_on_perimeter", value, initial_input_store)
    return 1 if state == True else 0


## Performance

@app.callback(
    Output('CpU', 'figure'),
    Output('CtU', 'figure'),
    Input('turbine-performance-datatable', 'data')
)
def turbine_performance_plots(data):
    df_turbine_performance = pd.DataFrame(data)
    return create_turbine_performance_plots(df_turbine_performance)


@app.callback(
    Output('turbine-performance-datatable', 'data'),
    Output('turbine-performance-datatable', 'columns'),
    Input('turbine-performance-datatable', 'data'),
    State('initial-input-store', 'data')
)
def get_performance_table_data(data, initial_input_store):

    if initial_input_store is None:
        # TODO: This is a fatal error. How to handle?
        return None

    if data == None:
        df = pd.DataFrame(
            {
                'Wind Speed': initial_input_store["turbine"]["properties"]["power_thrust_table"]["wind_speed"],
                'Cp': initial_input_store["turbine"]["properties"]["power_thrust_table"]["power"],
                'Ct': initial_input_store["turbine"]["properties"]["power_thrust_table"]["thrust"]
            }
        )
    else:
        df = pd.DataFrame(data)

    columns = [{"name": i, "id": i} for i in df.columns]
    return df.to_dict("rows"), columns

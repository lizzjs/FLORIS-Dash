
from dash.dependencies import Input, Output, State
import pandas as pd

from app import app
import apps.floris_data
from graph_generator import *


## Geometry

def _get_turbine_definition_value(key, value, initial_input_store, turbine_store=None):
    
    # On first load
    if value is None:
        if turbine_store is not None:
            if key in turbine_store:
                return turbine_store[key]

        if initial_input_store is None:
            # TODO: Do we leave this? This handles the situation when the input store is not available for any reason.
            initial_input_store = apps.floris_data.default_input_dict
        return initial_input_store["turbine"]["properties"][key]

    # On every other call, return the value in the field
    return value


@app.callback(
    Output('input-rotor-diameter', 'value'),
    Input('input-rotor-diameter', 'value'),
    State('initial-input-store', 'data'),
    State('turbine-input-store', 'data')
)
def rotor_diameter(value, initial_input_store, turbine_store):
    key = "rotor_diameter"
    return _get_turbine_definition_value(key, value, initial_input_store, turbine_store)


@app.callback(
    Output('input-hub-height', 'value'),
    Input('input-hub-height', 'value'),
    State('initial-input-store', 'data'),
    State('turbine-input-store', 'data')
)
def hub_height(value, initial_input_store, turbine_store):
    key = "hub_height"
    return _get_turbine_definition_value(key, value, initial_input_store, turbine_store)


@app.callback(
    Output('input-yaw-angle', 'value'),
    Input('input-yaw-angle', 'value'),
    State('initial-input-store', 'data'),
    State('turbine-input-store', 'data')
)
def yaw_angle(value, initial_input_store, turbine_store):
    key = "yaw_angle"
    return _get_turbine_definition_value(key, value, initial_input_store, turbine_store)


@app.callback(
    Output('input-tilt-angle', 'value'),
    Input('input-tilt-angle', 'value'),
    State('initial-input-store', 'data'),
    State('turbine-input-store', 'data')
)
def tilt_angle(value, initial_input_store, turbine_store):
    key = "tilt_angle"
    return _get_turbine_definition_value(key, value, initial_input_store, turbine_store)


@app.callback(
    Output('input-tip-speed-ratio', 'value'),
    Input('input-tip-speed-ratio', 'value'),
    State('initial-input-store', 'data'),
    State('turbine-input-store', 'data')
)
def tip_speed_ratio(value, initial_input_store, turbine_store):
    key = "TSR"
    return _get_turbine_definition_value(key, value, initial_input_store, turbine_store)


@app.callback(
    Output('input-generator-efficiency', 'value'),
    Input('input-generator-efficiency', 'value'),
    State('initial-input-store', 'data'),
    State('turbine-input-store', 'data')
)
def generator_efficiency(value, initial_input_store, turbine_store):
    key = "generator_efficiency"
    return _get_turbine_definition_value(key, value, initial_input_store, turbine_store)


@app.callback(
    Output('input-pP', 'value'),
    Input('input-pP', 'value'),
    State('initial-input-store', 'data'),
    State('turbine-input-store', 'data')
)
def pP(value, initial_input_store, turbine_store):
    key = "pP"
    return _get_turbine_definition_value(key, value, initial_input_store, turbine_store)


@app.callback(
    Output('input-pT', 'value'),
    Input('input-pT', 'value'),
    State('initial-input-store', 'data'),
    State('turbine-input-store', 'data')
)
def pT(value, initial_input_store, turbine_store):
    key = "pT"
    return _get_turbine_definition_value(key, value, initial_input_store, turbine_store)


@app.callback(
    Output('slider-ngrid', 'value'),
    Input('slider-ngrid', 'value'),
    State('initial-input-store', 'data'),
    State('turbine-input-store', 'data')
)
def ngrid(value, initial_input_store, turbine_store):
    key = "ngrid"
    return _get_turbine_definition_value(key, value, initial_input_store, turbine_store)


@app.callback(
    Output('input-rloc', 'value'),
    Input('input-rloc', 'value'),
    State('initial-input-store', 'data'),
    State('turbine-input-store', 'data')
)
def rloc(value, initial_input_store, turbine_store):
    key = "rloc"
    return _get_turbine_definition_value(key, value, initial_input_store, turbine_store)


@app.callback(
    Output('switch-perimeter-points', 'on'),
    Input('switch-perimeter-points', 'on'),
    State('initial-input-store', 'data'),
    State('turbine-input-store', 'data')
)
def perimeter_points(value, initial_input_store, turbine_store):
    key = "use_points_on_perimeter"
    return _get_turbine_definition_value(key, value, initial_input_store, turbine_store)


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
    State('initial-input-store', 'data'),
    State('turbine-input-store', 'data')
)
def get_performance_table_data(data, initial_input_store, turbine_store):
    key = "power_thrust_table"
    table = _get_turbine_definition_value(key, data, initial_input_store, turbine_store)
    df = pd.DataFrame(table)
    columns = [{"name": i, "id": i} for i in df.columns]
    temp_column = columns.copy()

    # Rearrange columns in the final table
    columns[0] = temp_column[2] # Wind speed
    columns[1] = temp_column[0] # Power
    columns[2] = temp_column[1] # Thrust

    return df.to_dict("rows"), columns


## Turbine definition store

@app.callback(
    Output('turbine-input-store', 'data'),
    Input('input-rotor-diameter', 'value'),
    Input('input-hub-height', 'value'),
    Input('input-yaw-angle', 'value'),
    Input('input-tilt-angle', 'value'),
    Input('input-tip-speed-ratio', 'value'),
    Input('input-generator-efficiency', 'value'),
    Input('input-pP', 'value'),
    Input('input-pT', 'value'),
    Input('slider-ngrid', 'value'),
    Input('input-rloc', 'value'),
    Input('switch-perimeter-points', 'on'),
    Input('turbine-performance-datatable', 'data'),
)
def store_turbine_definition(rotor_diameter, hub_height, yaw_angle, tilt_angle, TSR, generator_efficiency, pP, pT, ngrid, rloc, use_points_on_perimeter, power_thrust_table):
    turbine_data = {
        "rotor_diameter": rotor_diameter,
        "hub_height": hub_height,
        "yaw_angle": yaw_angle,
        "tilt_angle": tilt_angle,
        "TSR": TSR,
        "generator_efficiency": generator_efficiency,
        "pP": pP,
        "pT": pT,
        "ngrid": ngrid,
        "rloc": rloc,
        "use_points_on_perimeter": use_points_on_perimeter,
        "power_thrust_table": power_thrust_table,
    }
    return turbine_data

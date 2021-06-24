
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

from app import app
import apps.model_builder.import_callbacks
import apps.floris_data


## Geometry inputs

@app.callback(Output('input-rotordiam', 'value'), Input('input-rotordiam', 'value'))
def rotor_diameter(value):
    apps.floris_data.user_defined_dict["turbine"]["properties"]["rotor_diameter"] = value
    return apps.floris_data.user_defined_dict["turbine"]["properties"]["rotor_diameter"]

@app.callback(Output('input-hubheight', 'value'), Input('input-hubheight', 'value'))
def hub_height(value):
    apps.floris_data.user_defined_dict["turbine"]["properties"]["hub_height"] = value
    return apps.floris_data.user_defined_dict["turbine"]["properties"]["hub_height"]

@app.callback(Output('slider-yawang', 'value'), Input('slider-yawang', 'value'))
def yaw_angle(value):
    apps.floris_data.user_defined_dict["turbine"]["properties"]["yaw_angle"] = value
    return apps.floris_data.user_defined_dict["turbine"]["properties"]["yaw_angle"]

@app.callback(Output('slider-tiltang', 'value'), Input('slider-tiltang', 'value'))
def tilt_angle(value):
    apps.floris_data.user_defined_dict["turbine"]["properties"]["tilt_angle"] = value
    return apps.floris_data.user_defined_dict["turbine"]["properties"]["tilt_angle"]

@app.callback(Output('input-TSR', 'value'), Input('input-TSR', 'value'))
def tsr(value):
    apps.floris_data.user_defined_dict["turbine"]["properties"]["TSR"] = value
    return apps.floris_data.user_defined_dict["turbine"]["properties"]["TSR"]

@app.callback(Output('input-genEff', 'value'), Input('input-genEff', 'value'))
def generator_efficiency(value):
    apps.floris_data.user_defined_dict["turbine"]["properties"]["generator_efficiency"] = value
    return apps.floris_data.user_defined_dict["turbine"]["properties"]["generator_efficiency"]

@app.callback(Output('input-pP', 'value'), Input('input-pP', 'value'))
def pP(value):
    apps.floris_data.user_defined_dict["turbine"]["properties"]["pP"] = value
    return apps.floris_data.user_defined_dict["turbine"]["properties"]["pP"]

@app.callback(Output('input-pT', 'value'), Input('input-pT', 'value'))
def pT(value):
    apps.floris_data.user_defined_dict["turbine"]["properties"]["pT"] = value
    return apps.floris_data.user_defined_dict["turbine"]["properties"]["pT"]

@app.callback(Output('slider-ngrid', 'value'), Input('slider-ngrid', 'value'))
def ngrid(value):
    apps.floris_data.user_defined_dict["turbine"]["properties"]["ngrid"] = value
    return apps.floris_data.user_defined_dict["turbine"]["properties"]["ngrid"]

@app.callback(Output('input-rloc', 'value'), Input('input-rloc', 'value'))
def rloc(value):
    apps.floris_data.user_defined_dict["turbine"]["properties"]["rloc"] = value
    return apps.floris_data.user_defined_dict["turbine"]["properties"]["rloc"]

@app.callback(Output('switch-perimeter-points', 'value'), Input('switch-perimeter-points', 'value'))
def perimeter_points(value):
    apps.floris_data.user_defined_dict["turbine"]["properties"]["use_points_on_perimeter"] = value
    return apps.floris_data.user_defined_dict["turbine"]["properties"]["use_points_on_perimeter"]


# Performance inputs

@app.callback(
    Output('CpU', 'figure'),
    Output('CtU', 'figure'),
    Input('turbine-performance-datatable', 'data')
)
def create_turbine_performance_plots(data):
    df = pd.DataFrame(data)

    fig1 = px.line(
        x=df["Wind Speed"],
        y=df["Cp"],
        template="seaborn",
        title="Power Curve"
    )

    fig2 = px.line(
        x=df["Wind Speed"],
        y=df["Ct"],
        template="seaborn",
        title="Thrust Curve"
    )

    return fig1, fig2

@app.callback(
    [Output('turbine-performance-datatable', 'data'),
    Output('turbine-performance-datatable', 'columns')],
    Input('turbine-performance-datatable', 'data')
)
def get_performance_table_data(data):
    if data is None:
        df = pd.DataFrame(
            {
                'Wind Speed': apps.floris_data.user_defined_dict["turbine"]["properties"]["power_thrust_table"]["wind_speed"],
                'Cp': apps.floris_data.user_defined_dict["turbine"]["properties"]["power_thrust_table"]["power"],
                'Ct': apps.floris_data.user_defined_dict["turbine"]["properties"]["power_thrust_table"]["thrust"]
            }
        )
    else:
        df = pd.DataFrame(data)

    columns = [{"name": i, "id": i} for i in df.columns]
    # print(df.to_dict("rows"))
    return df.to_dict("rows"), columns

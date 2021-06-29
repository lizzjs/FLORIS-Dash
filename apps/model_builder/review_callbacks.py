
from dash.dependencies import Input, Output, State
import apps.model_builder.review_callbacks
import numpy as np
import pandas as pd
import time

from app import app, colors
import apps.floris_data

import floris.tools as ft
from floris.tools.floris_interface import FlorisInterface
from floris.tools.optimization.scipy.yaw_wind_rose import YawOptimizationWindRose
import floris.tools.power_rose as pr
import floris.tools.wind_rose as rose

import plotly.graph_objs as go
import plotly.express as px
import matplotlib.pyplot as plt

# def get_floris_calc_cp_ct():
#     # Initialize the FLORIS interface fi
#     fi = ft.floris_interface.FlorisInterface(input_dict=apps.floris_data.default_input_dict)

#     saved_layout_y = apps.floris_data.default_input_dict["farm"]["properties"]["layout_x"]
#     saved_layout_x = apps.floris_data.default_input_dict["farm"]["properties"]["layout_y"]

#     fi.reinitialize_flow_field(layout_array=([0], [0]))
#     cp_return_array = []
#     ct_return_array = []

#     wind_speeds = apps.floris_data.default_input_dict["turbine"]["properties"]["power_thrust_table"]["wind_speed"] 

#     for ws in wind_speeds:
#         fi.reinitialize_flow_field(wind_speed=ws)
#         fi.calculate_wake()
#         ct_return_array.append(fi.get_turbine_ct()[0])

#         area = np.pi*fi.floris.rotor_radius #probably not correct
#         cp = fi.get_turbine_power()[0]* area**3 #conversion for cp, missing stuff
#         ct_return_array.append(cp)

#     fi.reinitialize_flow_field(layout_array=(saved_layout_x, saved_layout_y))

#     ct_return_array = np.array(ct_return_array)
#     cp_return_array = np.array(ct_return_array)
#     wind_speed = np.array(wind_speeds)

#     coeff_dict = {'Wind Speed':wind_speed, 'CpU':cp_return_array, 'CtU':ct_return_array}
#     df = pd.DataFrame(coeff_dict)

#     plt.plot(df['Wind Speed'], df["CpU"])
#     plt.show()
#     return df

@app.callback(
    # Output("loading-output", "children"),
    Output("floris-outputs", "data"),
    Input("submit-floris-button", "n_clicks"),
    State("floris-outputs", "data")
)
def run_floris(n, floris_output_data):

    if not n:
        return

    fi = FlorisInterface(input_dict=apps.floris_data.default_input_dict)

    wd = np.arange(0.0, 360.0, 15.0)
    np.random.seed(1)
    ws = 8.0 + np.random.randn(len(wd)) * 0.5
    freq = np.abs(np.sort(np.random.randn(len(wd))))
    freq = freq / freq.sum()

    wind_rose = rose.WindRose()
    df = wind_rose.make_wind_rose_from_user_dist(
        wd_raw=wd,
        ws_raw=ws,
        freq_val=freq
    )

    start = time.perf_counter()

    yaw_opt = YawOptimizationWindRose(
        fi,
        df.wd,
        df.ws,
        # minimum_yaw_angle=min_yaw,
        # maximum_yaw_angle=max_yaw,
        # minimum_ws=8.0,
        # maximum_ws=maximum_ws,
        # opt_options=opt_options,
    )

    # Determine baseline power with and without wakes
    df_base = yaw_opt.calc_baseline_power()

    # Perform optimization
    df_opt = yaw_opt.optimize()

    power_rose = pr.PowerRose()
    power_rose.make_power_rose_from_user_data(
        "",
        df,
        df_base["power_no_wake"],
        df_base["power_baseline"],
        df_opt["power_opt"],
    )

    end = time.perf_counter()

    model_name = apps.floris_data.default_input_dict["wake"]["properties"]["velocity_model"]
    compute_time = end - start

    floris_output_data = {
        model_name: {
            "compute_time": compute_time,
            "power_data": {
                "wind_directions": power_rose.df_power["wd"],
                "ideal_power": power_rose.power_no_wake,
                "baseline_power": power_rose.power_baseline,
                "optimized_power": power_rose.power_opt
            }
        }
    }
    return floris_output_data

@app.callback(
    Output('review-windrose-graph', 'figure'),
    Output('review-wind-farm-layout', 'figure'),
    # Output('aep-farm-graph', 'figure'),
    # Output('aep-windrose-graph', 'figure'),
    Input("floris-outputs", "data")
)
def return_review_page_graphs(floris_output_data):
    #Windrose
    wind_rose_figure = px.bar_polar(
        pd.DataFrame(apps.floris_data.wind_rose_data),
        r="frequency",
        theta="direction",
        color="strength",
        template="seaborn",
        color_discrete_sequence=px.colors.sequential.Plasma_r,
        title="Wind Rose"
    )

    #Wind farm 
    layout_data = pd.DataFrame(
        {
            'layout_x': apps.floris_data.user_defined_dict["farm"]["properties"]["layout_x"],
            'layout_y': apps.floris_data.user_defined_dict["farm"]["properties"]["layout_y"]
        }
    )
    boundary_data = pd.DataFrame(
        {
            'boundary_x': apps.floris_data.boundary_data["boundary_x"],
            'boundary_y': apps.floris_data.boundary_data["boundary_y"]
        }
    )

    layout_plot_data = [
        go.Scatter(
            x=layout_data['layout_x'],
            y=layout_data['layout_y'],
            mode='markers'
        )
    ]

    if boundary_data is not None:
        df_bf = boundary_data.append(boundary_data.iloc[0,:], ignore_index=True)
        layout_plot_data.append(
            go.Line(
                x=df_bf['boundary_x'],
                y=df_bf['boundary_y'],
            )
        )
    wind_farm_figure = go.Figure(
        data=layout_plot_data,
        layout=go.Layout(
            # plot_bgcolor=colors["graphBackground"],
            # paper_bgcolor=colors["graphBackground"]
        )
    )

    #Cp Ct 
    # df_floris_calc = get_floris_calc_cp_ct()

    return wind_rose_figure, wind_farm_figure
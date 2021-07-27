from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import copy

from floris.tools.floris_interface import FlorisInterface
import numpy as np
import apps.floris_data
import apps

def create_turbine_performance_plots(df):
    cp_plot_data = go.Line(
        x=df["wind_speed"],
        y=df["power"],
        name="Input",
        line = dict(color='rgb(204, 37, 8)')
    ),
    power_figure = go.Figure(
        data=cp_plot_data,
        layout=go.Layout(
            title= dict(
                text="Power Curve",
                x=0.5,
                y=0.88,
                font = dict(size=18)
            ),
            xaxis_title="Wind Speed",
            yaxis_title="Cp",
        )
    )

    ct_plot_data = go.Line(
        x=df["wind_speed"],
        y=df["thrust"],
        name="Input",
        line = dict(color='rgb(69, 3, 252)')
    ),
    thrust_figure = go.Figure(
        data=ct_plot_data,
        layout=go.Layout(
            title= dict(
                text="Thrust Curve",
                x=0.5,
                y=0.88,
                font = dict(size=18)
            ),
            xaxis_title='Wind Speed',
            yaxis_title="Ct",

        )
    )
    return power_figure, thrust_figure


def create_windrose_plot(df):
    wind_rose_figure = px.bar_polar(
        df,
        r="frequency",
        theta="direction",
        color="strength",
        template="seaborn",
        color_discrete_sequence=px.colors.sequential.Plasma_r,
        title="Wind Rose",

    )
    return wind_rose_figure

def create_farm_layout_plot(df, df2):
    figure_data = [
        go.Scatter(
            x=df['layout_x'],
            y=df['layout_y'],
            mode='markers',
            marker_symbol='y-down',
            marker_line_width=2, 
            marker_size=15,
            name='Wind turbines'
        )
    ]

    if df2 is not None: 
        figure_data.append(
            go.Line(
                x=df2['boundary_x'],
                y=df2['boundary_y'],
                name='Boundary'
            )
        )

    wind_farm_layout = go.Figure(
        data=figure_data,
        layout=go.Layout(
            title= dict(
                text="Wind Farm Layout",
                x=0.5,
                y=0.9,
            ),
            legend = dict(
                    font = dict(size=10, color="black"), 
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                )
        ),
        )
    return wind_farm_layout

def create_preview_wake_model(velocity_value, deflection_value, turbulence_value, combination_value, velocity_parameters):

    # Using a FLORIS model with two turbines in tandem, show a preview of the wake model settings
    wake_model_preview_dict = copy.deepcopy(apps.floris_data.default_input_dict)
    wake_model_preview_dict['farm']['properties']['layout_x'] = [0.0, 630.0, 0.0]
    wake_model_preview_dict['farm']['properties']['layout_y'] = [0.0, 0.0, 630]

    fi = FlorisInterface(input_dict=wake_model_preview_dict)

    fi.floris.farm.wake.velocity_model = velocity_value
    fi.set_model_parameters(velocity_parameters, verbose=True)
    fi.floris.farm.wake.deflection_model = deflection_value
    fi.floris.farm.wake.turbulence_model = turbulence_value
    fi.floris.farm.wake.combination_model = combination_value

    fi.calculate_wake(yaw_angles=[20.0, 0.0])
    horizontal_slice = fi.get_hor_plane()

    minSpeed = horizontal_slice.df.u.min()
    maxSpeed = horizontal_slice.df.u.max()

    # Reshape to 2d for plotting
    # x1_mesh = horizontal_slice.df.x1.values.reshape(horizontal_slice.resolution[1], horizontal_slice.resolution[0])
    # x2_mesh = horizontal_slice.df.x2.values.reshape(horizontal_slice.resolution[1], horizontal_slice.resolution[0])
    u_mesh = horizontal_slice.df.u.values.reshape(horizontal_slice.resolution[1], horizontal_slice.resolution[0]).astype(np.float64)

    wake_contour_graph = go.Figure(
        data=go.Contour(
            z = u_mesh
        )
    )
    return wake_contour_graph

def create_turbine_performance_comparison_plots(df_input, df_cp_ct):
    cp_plot_data = [
        go.Line(
            x=df_input["wind_speed"],
            y=df_input["power"],
            name="Input",
            line = dict(color='rgb(204, 37, 8)')
        ),
        go.Line(
            x=df_cp_ct["Wind Speed"],
            y=df_cp_ct["Cp"],
            name="FLORIS Calculated",
            line = dict(shape='linear', color='rgb(255, 182, 56)', dash='dot')
        )
    ]
    power_figure = go.Figure(
        data=cp_plot_data,
        layout=go.Layout(
            title= dict(
                text="Power Curve",
                x=0.5,
                y=0.9,
                font = dict(size=18)
            ),
            xaxis_title="Wind Speed",
            yaxis_title="Cp",
            legend = dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            height=400
        )
    )

    ct_plot_data = [
        go.Line(
            x=df_input["wind_speed"],
            y=df_input["thrust"],
            name="Input",
        ),
        go.Line(
            x=df_cp_ct["Wind Speed"],
            y=df_cp_ct["Ct"],
            name="FLORIS Calculated",
            line = dict(shape='linear', color='rgb(3, 219, 252)', dash='dot') #'linear', 'spline', 'hv', 'vh', 'hvh', 'vhv'
        )
    ]
    thrust_figure = go.Figure(
        data=ct_plot_data,
        layout=go.Layout(
            title= dict(
                text="Thrust Curve",
                x=0.5,
                y=0.9,
                font = dict(size=18)
            ),
            xaxis_title='Wind Speed',
            yaxis_title="Ct",
            legend = dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            height=400
        )
    )
    return power_figure, thrust_figure

def create_aep_dashboard_plots(floris_output_data):
    model_name = apps.floris_data.default_input_dict["wake"]["properties"]["velocity_model"]
    df = pd.DataFrame(floris_output_data[model_name]["power_data"])
    df = df.groupby("wind_directions").sum().reset_index()

    power_rose_data = [
        go.Line(
            x=df["wind_directions"],
            y=df["ideal_power"],
            name='Ideal Power',
            line=dict(shape='linear', dash='dash')
        ),
        go.Line(
            x=df["wind_directions"],
            y=df["baseline_power"],
            name='Baseline Power',
            line=dict(shape='linear', dash='dot')
        ),
        go.Line(
            x=df["wind_directions"],
            y=df["optimized_power"],
            name='Optimized Power',
            line=dict(shape='linear')
        )
    ]
    power_rose_figure = go.Figure(
        data=power_rose_data,
        layout=go.Layout(
            title= dict(
                text="Power Production",
                x=0.5,
                y=0.9,
                font=dict(size=18)
            ),
            legend = dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
        )
    )

    # Compute time
    columns_ct = ["Model Name", "Compute Time"]
    values = [
        [model_name, floris_output_data[model_name]["compute_time"]]
    ]
    compute_time_figure = px.bar(
        pd.DataFrame(values, columns=columns_ct),
        x=columns_ct[0],
        y=columns_ct[1],
        template="seaborn",
        title='Compute Time',
    )
    return power_rose_figure, compute_time_figure
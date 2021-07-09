
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

from app import app, colors
from apps.model_builder import review_layout
import apps.floris_data
import time

@app.callback(
    Output('model-comparison-graph', 'figure'),
    Output('compute-time-graph', 'figure'),
    Output('aep-farm-graph', 'figure'),
    Output('aep-windrose-graph', 'figure'),
    Input("floris-outputs", "data"),
)
def create_dashboard_plots(floris_output_data):

    model_name = apps.floris_data.default_input_dict["wake"]["properties"]["velocity_model"]

    df = pd.DataFrame()
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
            plot_bgcolor=colors["graphBackground"],
            title= dict(
                text="Power Production",
                x=0.5,
                y=0.9,
                font=dict(size=18)
            ),
            legend = dict(
                font = dict(size=10, color="black"), 
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

    # Wind farm layout
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
            mode='markers',
            name="Turbine Markers",
        )
    ]

    if boundary_data is not None:
        df_bf = boundary_data.append(boundary_data.iloc[0,:], ignore_index=True)
        layout_plot_data.append(
            go.Line(
                x=df_bf['boundary_x'],
                y=df_bf['boundary_y'],
                name="Boundary"
            )
        )
    layout_figure = go.Figure(
        data=layout_plot_data,
        layout=go.Layout(
            plot_bgcolor=colors["graphBackground"],
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
        )
    )

    # Windrose
    wind_rose_figure = px.bar_polar(
        pd.DataFrame(apps.floris_data.wind_rose_data),
        r="frequency",
        theta="direction",
        color="strength",
        template="seaborn",
        color_discrete_sequence=px.colors.sequential.Plasma_r,
        title="Wind Rose"
    )

    return power_rose_figure, compute_time_figure, layout_figure, wind_rose_figure


    # ax.plot(
    #     df.wd,
    #     df.energy_baseline / np.max(df.energy_opt),
    #     label="Baseline",
    #     color="k",
    # )
    # ax.axhline(
    #     np.mean(df.energy_baseline / np.max(df.energy_opt)), color="r", ls="--"
    # )
    # ax.plot(
    #     df.wd,
    #     df.energy_opt / np.max(df.energy_opt),
    #     label="Optimized",
    #     color="r",
    # )
    # ax.axhline(
    #     np.mean(df.energy_opt / np.max(df.energy_opt)), color="r", ls="--"
    # )
    # ax.set_ylabel("Normalized Energy")
    # ax.grid(True)
    # ax.legend()
    # ax.set_title(self.name)

    # ax = axarr[1]
    # ax.plot(
    #     df.wd,
    #     df.energy_baseline / df.energy_no_wake,
    #     label="Baseline",
    #     color="k",
    # )
    # ax.axhline(
    #     np.mean(df.energy_baseline) / np.mean(df.energy_no_wake),
    #     color="k",
    #     ls="--",
    # )
    # ax.plot(
    #     df.wd, df.energy_opt / df.energy_no_wake, label="Optimized", color="r"
    # )
    # ax.axhline(
    #     np.mean(df.energy_opt) / np.mean(df.energy_no_wake), color="r", ls="--"
    # )
    # ax.set_ylabel("Wind Farm Efficiency")
    # ax.grid(True)
    # ax.legend()

    # ax = axarr[2]
    # ax.plot(
    #     df.wd,
    #     100.0 * (df.energy_opt - df.energy_baseline) / df.energy_baseline,
    #     "r",
    # )
    # ax.axhline(
    #     100.0 * (df.energy_opt.mean() - df.energy_baseline.mean()),
    #     df.energy_baseline.mean(),
    #     color="r",
    #     ls="--",
    # )
    # ax.set_ylabel("Percent Gain")
    # ax.set_xlabel("Wind Direction (deg)")

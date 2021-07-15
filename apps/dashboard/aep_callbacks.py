
from dash.dependencies import Input, Output, State
import pandas as pd

from app import app
from apps.model_builder import review_layout
import apps.floris_data
from apps.graph_generator import *

@app.callback(
    Output('model-comparison-graph', 'figure'),
    Output('compute-time-graph', 'figure'),
    Output('aep-farm-graph', 'figure'),
    Output('aep-windrose-graph', 'figure'),
    Input("floris-outputs", "data"),
)
def create_dashboard_plots(floris_output_data):

    # Power Production & Compute Time 
    [power_rose_figure, compute_time_figure] = create_aep_dashboard_plots(floris_output_data)


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

    df_farm = pd.DataFrame(layout_data)

    if boundary_data is not None: 
        df_boundary = pd.DataFrame(boundary_data)
        df_boundary = df_boundary.append(df_boundary.iloc[0,:], ignore_index=True)
        
    wind_farm_figure = create_farm_layout_plot(df_farm, df_boundary)    

    # Windrose
    wind_data = apps.floris_data.wind_rose_data
    df_windrose = pd.DataFrame(wind_data)
    wind_rose_figure = create_windrose_plot(df_windrose)

    return power_rose_figure, compute_time_figure, wind_farm_figure, wind_rose_figure

    #TODO: Energy plot
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

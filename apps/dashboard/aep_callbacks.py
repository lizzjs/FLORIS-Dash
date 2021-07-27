
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import pandas as pd

from app import app
import apps.floris_data
from apps.graph_generator import *

app.clientside_callback(
    """
    function(n_clicks){
        if(n_clicks > 0){
            var opt = {
                margin: 1,
                filename: 'Results_Report.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 3},
                jsPDF: { unit: 'cm', format: 'a2', orientation: 'p' },
                pagebreak: { mode: ['avoid-all'] }
            };
            html2pdf().from(document.getElementById("print")).set(opt).save();
        }
    }
    """,
    Output('js','n_clicks'),
    Input('js','n_clicks')
)

@app.callback(
    Output('loading-spinner', 'children'),
    Output('model-comparison-graph-div', 'children'),
    Output('compute-time-graph-div', 'children'),
    Output('aep-farm-graph-div', 'children'),
    Output('aep-windrose-graph-div', 'children'),
    Input("floris-outputs", "data"),
    State("final-input-store", 'data')
)
def create_dashboard_plots(floris_output_data, final_input_store):

    # Power Production & Compute Time 
    [power_rose_figure, compute_time_figure] = create_aep_dashboard_plots(final_input_store, floris_output_data)


    # Wind farm layout
    layout_data = pd.DataFrame(
        {
            'layout_x': final_input_store["farm"]["properties"]["layout_x"],
            'layout_y': final_input_store["farm"]["properties"]["layout_y"]
        }
    )
    boundary_data = pd.DataFrame(
        {
            'boundary_x': final_input_store["farm"]["properties"]["boundary_x"],
            'boundary_y': final_input_store["farm"]["properties"]["boundary_y"]
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

    return None, dcc.Graph(figure=power_rose_figure), dcc.Graph(figure=compute_time_figure), dcc.Graph(figure=wind_farm_figure), dcc.Graph(figure=wind_rose_figure)

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


from dash.dependencies import Input, Output, State
import numpy as np
import time

from app import app
import apps.floris_data

from floris.tools.floris_interface import FlorisInterface
from floris.tools.optimization.scipy.yaw_wind_rose import YawOptimizationWindRose
import floris.tools.power_rose as pr
import floris.tools.wind_rose as rose


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

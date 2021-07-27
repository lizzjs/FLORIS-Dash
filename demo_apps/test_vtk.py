"""
An example that is (tries to be) a demo of all features.
"""

import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash_slicer import VolumeSlicer
from dash.dependencies import Input, Output, State, ALL

import dash_core_components as dcc
import dash_html_components as html

import numpy as np
import floris.tools as wfct
import apps.floris_data
from app import app

import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash_slicer import VolumeSlicer
from dash.dependencies import Input, Output, State, ALL
from skimage import measure

import plotly.express as px

app = dash.Dash(__name__, update_title=None)
server = app.server

# R, G, B = "#FF0000", "#00FF00", "#0000FF"
# R, G, B = (255, 0, 0), (0, 255, 0), (0, 0, 255)
# COLORMAP = [R, G, B]
# colorscales = px.colors.named_colorscales()
COLORMAP = px.colors.sequential.Turbo

# If the px color maps uses RBG values, then enable this to convert to tuples of ints
# for i, c in enumerate(COLORMAP):
#     COLORMAP[i] = c.strip("rgb(").strip(')').split(',')


fi = wfct.floris_interface.FlorisInterface(input_dict=apps.floris_data.default_input_dict)
fi.floris.farm.set_wake_model("jensen")
fi.reinitialize_flow_field()
fd = fi.get_flow_data()

# compute dimensions, origins and spacing based on flow data
axes = [fd.z, fd.y, fd.x]
origin = [ axis.mean().round().astype(int) for axis in axes ]
ranges = np.array( [ axis.ptp().round().astype(int) for axis in axes ] )
dimensions = (fd.dimensions.x3, fd.dimensions.x2, fd.dimensions.x1)
spacing = np.round(ranges / dimensions).astype(int)

volume = fd.u
volume = np.reshape(volume, dimensions)

# Create slicer objects
slicer0 = VolumeSlicer(
    app,
    volume,
    axis=0
)
slicer2 = VolumeSlicer(
    app,
    volume,
    axis=2,
    reverse_y=False
)

# Put everything together in a 2x2 grid
app.layout = html.Div(
    style={
        "display": "grid",
        "gridTemplateColumns": "33% 33% 33%",
    },
    children=[
        html.Div(
            [
                html.Center(html.H1("Axis 0")),
                slicer0.graph,
                html.Br(),
                slicer0.slider,
                *slicer0.stores,
            ]
        ),
        html.Div(
            [
                html.Center(html.H1("Axis 2")),
                slicer2.graph,
                html.Br(),
                slicer2.slider,
                *slicer2.stores,
            ]
        ),
        html.Div(
            [
                html.Center(html.H1("3D")),
                dcc.Graph(id="3Dgraph", figure=go.Figure()),
            ]
        ),
    ],
)


# Callback to display slicer view positions in the 3D view
app.clientside_callback(
    """
function update_3d_figure(states, ori_figure) {
    let traces = [];
    for (let state of states) {
        if (!state) continue;
        let xrange = state.xrange;
        let yrange = state.yrange;
        let xyz = [
            [xrange[0], xrange[1], xrange[1], xrange[0], xrange[0]],
            [yrange[0], yrange[0], yrange[1], yrange[1], yrange[0]],
            [state.zpos, state.zpos, state.zpos, state.zpos, state.zpos]
        ];
        xyz.splice(2 - state.axis, 0, xyz.pop());
        let s = {
            type: 'scatter3d',
            x: xyz[0], y: xyz[1], z: xyz[2],
            mode: 'lines', line: {color: state.color},
            hoverinfo: 'skip',
            showlegend: false,
        };
        traces.push(s);
    }
    let figure = {...ori_figure};
    figure.data = traces;
    return figure;
}
    """,
    Output("3Dgraph", "figure"),
    [Input({"scene": slicer0.scene_id, "context": ALL, "name": "state"}, "data")],
    [State("3Dgraph", "figure")],
)


@app.callback(
    Output(slicer0.overlay_data.id, "data"),
    Output(slicer2.overlay_data.id, "data"),
    Input({"scene": slicer0.scene_id, "context": ALL, "name": "state"}, "data"),
)
def update_overlay(_):
    mask = np.zeros(volume.shape, np.uint8)

    data_range = volume.max() - volume.min()

    # lower = vol.min() + data_range / 3.0
    # mid = vol.min() + 2 * data_range / 3.0
    # upper = vol.min() + data_range
    # mask += vol < lower
    # mask += vol < mid
    # mask += vol < upper

    thresholds = [ volume.min() + i * data_range / len(COLORMAP) for i in range(1,len(COLORMAP) + 1) ]

    for i in range(len(COLORMAP)):
        mask += volume < thresholds[i]

    slicer0_overlay = slicer0.create_overlay_data(mask, COLORMAP)
    sliver2_overlay = slicer2.create_overlay_data(mask, COLORMAP)
    return slicer0_overlay, sliver2_overlay

# # Callback to add contours in axes 2
# @app.callback(
#     Output(slicer0.extra_traces.id, "data"),
#     Input(slicer0.state.id, "data")
# )
# def update_contour(state):
#     if not state:
#         return dash.no_update
#     slice = volume[:, :, state["index"]]
#     contours = measure.find_contours(slice)
#     traces = []
#     for contour in contours:
#         traces.append(
#             {
#                 "type": "scatter",
#                 "mode": "lines",
#                 "line": {"color": "yellow", "width": 3},
#                 "x": contour[:, 1], # * spacing[1], # + origin[1],
#                 "y": contour[:, 0], # * spacing[0], # + origin[0],
#                 "hoverinfo": "skip",
#                 "showlegend": False,
#             }
#         )
#     return traces


if __name__ == "__main__":
    # Note: dev_tools_props_check negatively affects the performance of VolumeSlicer
    app.run_server(debug=True, dev_tools_props_check=False)

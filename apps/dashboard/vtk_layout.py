
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
import dash_html_components as html

import numpy as np
import apps.dashboard.vtk_callbacks
import floris.tools as wfct
from app import app

import dash_vtk
import plotly.graph_objects as go
from dash_slicer import VolumeSlicer
from dash.dependencies import Input, Output, State, ALL

fi = wfct.floris_interface.FlorisInterface(input_dict=apps.floris_data.default_input_dict)
fi.floris.farm.set_wake_model("gauss_legacy")
fi.reinitialize_flow_field()
fd = fi.get_flow_data()

# compute dimensions, origins and spacing based on flow data
origin = [axis.mean().round().astype(int) for axis in [fd.x, fd.y, fd.z]]
ranges = np.array([axis.ptp().round().astype(int) for axis in [fd.x, fd.y, fd.z]])

dimensions = np.array([np.unique(axis).shape[0] for axis in [fd.x, fd.y, fd.z]])

x, y, z = dimensions
spacing = np.round(ranges / dimensions).astype(int)

vtk_view = dash_vtk.View(id="vtk-view")

def CustomSlider(data: np.array, label: str, id: str):
    n_unique = np.unique(data).shape[0]

    return dbc.FormGroup(
        [
            dbc.Label(label),
            dcc.Slider(min=0, max=n_unique, value=n_unique / 2, step=1, id=id,),
        ]
    )

controls = [
    dbc.FormGroup(
        [
            dbc.Label("Dimension"),
            dbc.RadioItems(
                options=[{"label": x, "value": x} for x in ["u", "v", "w"]],
                value="u",
                id="radio-dimension",
                inline=True,
            ),
        ]
    ),
    dbc.FormGroup(
        [
            dbc.Label("Enabled"),
            dbc.Checklist(
                options=[
                    {"label": x, "value": x.replace("Slice ", "")}
                    for x in ["Volume", "Slice i"] #, "Slice j", "Slice k"]
                ],
                value=["Volume", "i"],
                id="child-enabled",
                inline=True,
            ),
        ]
    ),
    dbc.FormGroup(
        [
            dbc.Label("Color Window"),
            dcc.Slider(
                min=0.01, max=1, value=0.5, step=0.01, id="color-window", tooltip={},
            ),
        ]
    ),
    dbc.FormGroup(
        [
            dbc.Label("Color Level Volume"),
            dcc.Slider(
                min=0.01, max=1, value=0.5, step=0.01, id="color-level", tooltip={},
            ),
        ]
    ),
    CustomSlider(data=fd.x, id="slider-slice-i", label="Slice i"),
    # CustomSlider(data=fd.y, id="slider-slice-j", label="Slice j"),
    # CustomSlider(data=fd.z, id="slider-slice-k", label="Slice k"),
]

vtk_view_horizontal = dbc.Row(
    [
        dbc.Col(
            width=9,
                children=[
                    dbc.Card(
                        [
                            dbc.CardHeader("Flow Visualization"),
                            dbc.CardBody(vtk_view, style={"height": "100%"}),
                        ],
                        style={"height": "70vh"},
                    ),
            ]
        ),
        dbc.Col(
            width=3,
            children=dbc.Card(
                [
                    dbc.CardHeader("Flow Visualization Controls"), 
                    dbc.CardBody(controls)
                ],
                style={"height": "70vh"},
            ),
        ),
    ],
    no_gutters=True
)

# Read volume
vol = fd.u
# dims = (fd.dimensions.x1, fd.dimensions.x2, fd.dimensions.x3)
dims = (fd.dimensions.x3, fd.dimensions.x2, fd.dimensions.x1)
vol = np.reshape(vol, dims)
print(np.shape(vol))
ori = origin


slicer0 = VolumeSlicer(app, vol, spacing=spacing, origin=ori, axis=0, thumbnail=False, clim=None, reverse_y=False,)
slicer0_graph = slicer0.graph.figure
slicer0_graph.update_layout(margin={'pad': 0})

slicer2 = VolumeSlicer(app, vol, spacing=spacing, origin=ori, axis=2, reverse_y=False, color="#00ff99")
slicer2_graph = slicer0.graph.figure
slicer2_graph.update_layout(margin={'pad': 0})

slicers = html.Div(
    style={
        "display": "grid",
        "gridTemplateColumns": "40% 40% 20%",
    },
    children=[
        html.Div(
            [
                html.Center(html.H1("Elevation")),
                slicer0.graph,
                html.Br(),
                slicer0.slider,
                *slicer0.stores,
            ]
        ),
        html.Div(
            [
                html.Center(html.H1("Streamwise")),
                slicer2.graph,
                html.Br(),
                slicer2.slider,
                *slicer2.stores,
            ]
        ),
        html.Div(
            [
                html.Center(html.H1("3D")),
                dcc.Graph(id="3Dgraph", figure=go.Figure(layout=dict(margin={'b': 50, 'l': 0, 'pad': 0, 'r': 0, 't': 0}))),
            ],
        ),
    ]
),

slicer_layout_horizontal = dbc.Row(
    dbc.Col(
        children=dbc.Card(
            [
                dbc.CardHeader("Slicer View"), 
                dbc.CardBody(slicers)
            ]
        ),
        width=12
    )
)


layout = html.Div(
    children=[
        dbc.Row([dbc.Col(html.H1("Flow Visualization with FLORIS and VTK"), md=8)], align="center"),
        html.Hr(),
        slicer_layout_horizontal,
        vtk_view_horizontal,
    ]
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
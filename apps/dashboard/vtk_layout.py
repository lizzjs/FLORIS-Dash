
import dash_bootstrap_components as dbc
import dash_vtk
import dash_core_components as dcc
import dash_html_components as html

import numpy as np
import apps.dashboard.vtk_callbacks
import floris.tools as wfct

#Need this for the customsidebar
fi = wfct.floris_interface.FlorisInterface(input_dict=apps.floris_data.default_input_dict)
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
                    for x in ["Volume", "Slice i", "Slice j", "Slice k"]
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
            dbc.Label("Color Level"),
            dcc.Slider(
                min=0.01, max=1, value=0.5, step=0.01, id="color-level", tooltip={},
            ),
        ]
    ),
    CustomSlider(data=fd.x, id="slider-slice-i", label="Slice i"),
    CustomSlider(data=fd.y, id="slider-slice-j", label="Slice j"),
    CustomSlider(data=fd.z, id="slider-slice-k", label="Slice k"),
]

layout = dbc.Container(
    fluid=True,
    style={"height": "100vh"},
    children=[
        dbc.Row([dbc.Col(html.H1("Flow Visualization with FLORIS and VTK"), md=8)], align="center"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    width=4,
                    children=dbc.Card(
                        [dbc.CardHeader("Controls"), dbc.CardBody(controls),]
                    ),
                ),
                dbc.Col(
                    width=8,
                    children=dbc.Card(
                        [
                            dbc.CardHeader("Flow Visualization"),
                            dbc.CardBody(vtk_view, style={"height": "100%"}),
                        ],
                        style={"height": "80vh"},
                    ),
                ),
            ],
        ),
    ],
)

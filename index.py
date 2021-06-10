
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps.model_builder import turbine, farm, home, atmos_cond, wake

from apps.floris_input_defaults import default_input_dict
from floris.tools.floris_interface import FlorisInterface

SIDEBAR_STYLE = {
    # "position": "fixed",
    "top": 200,
    "left": 0,
    "bottom": 0,
    "width": "23.5rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

progress_card = html.Div(
    [
        html.H2("Model Builder", className="display-4"),
        html.Hr(),
        html.P(
            "FLORIS data input:", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Home", active="exact", href="/home")),
                dbc.NavItem(dbc.NavLink("Turbine", active="exact", href="/build/turbine")),
                dbc.NavItem(dbc.NavLink("Farm",  active="exact",href="/build/farm")),
                dbc.NavItem(dbc.NavLink("Atmospheric Conditions",  active="exact",href="/build/windrose")),
                dbc.NavItem(dbc.NavLink("Wake Model", active="exact", href="/build/wakemodel")),
                dbc.NavItem(dbc.NavLink("Calculate", active="exact", href="/calculate")),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

app.layout = dbc.Container(
    [
        dbc.Row( 
            dbc.Col( 
                dbc.Jumbotron( 
                    html.H1("FLORIS Dashboard", className="display-3") 
                ) 
            ) 
        ),
        dbc.Row(
            [
                # Progress tracker
                dbc.Col(
                    [
                        progress_card,
                        #TODO Consider moving next bar into the tubrine, farm, etc. layouts. Next button is fixed to 
                        #route path to farm 
                        # dbc.ListGroupItem( 
                            dbc.Button("Next", color="primary", href="/build/farm") 
                        # ),
                    ], width=2),

                # Input area
                dbc.Col(id="input-area", children=[])
            ]
        ),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ],
    fluid=True,
)

@app.callback(
    Output('input-area', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/' or pathname == '/home':
        return home.layout
    elif pathname == '/build/turbine':
        return turbine.layout
    elif pathname == '/build/farm':
        return farm.layout
    elif pathname == '/build/windrose':
        return atmos_cond.layout
    elif pathname == '/build/wakemodel':
        return wake.layout
    elif pathname == '/calculate':
        fi = FlorisInterface(input_dict=default_input_dict)
        fi.calculate_wake()
        turbines = fi.floris.farm.turbines

        cts = []
        powers = []
        ave_vels = []
        ais = []

        for i in range(len(turbines)):
            cts.append(turbines[i].Ct)
            powers.append(turbines[i].power)
            ave_vels.append(turbines[i].average_velocity)
            ais.append(turbines[i].aI)

        results = dbc.Card(
            dbc.CardBody([
                dbc.Row([ dbc.Col([ html.H3("FLORIS Results", className="card-text") ]) ]),
                dbc.Row([ dbc.Col([ html.Div(cts) ]) ]),
                dbc.Row([ dbc.Col([ html.Div(powers) ]) ]),
                dbc.Row([ dbc.Col([ html.Div(ave_vels) ]) ]),
                dbc.Row([ dbc.Col([ html.Div(ais) ]) ])
            ]),
            className="mt-3",
        )
        return html.Div([results])

    else:
        return dbc.Jumbotron([
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognized..."),
            ])


if __name__ == '__main__':
    app.run_server(debug=True)

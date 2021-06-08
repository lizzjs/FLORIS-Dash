
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps.model_builder import turbine, farm


progress_card = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Turbine", active="exact", href="/build/turbine")),
        dbc.NavItem(dbc.NavLink("Farm",  active="exact",href="/build/farm")),
        dbc.NavItem(dbc.NavLink("Atmospheric Conditions",  active="exact",href="/build/windrose")),
        dbc.NavItem(dbc.NavLink("Wake Model", active="exact", href="/build/wakemodel")),
        dbc.NavItem(dbc.NavLink("Calculate", active="exact", href="/calculate")),
    ],
    vertical=True,
    pills=True,
)

app.layout = dbc.Container(
    [
        dbc.Row( dbc.Col( dbc.Jumbotron( html.H1("FLORIS Dashboard", className="display-3") ) ) ),
        dbc.Row(
            [
                # Progress tracker
                dbc.Col(
                    [
                        progress_card,
                        dbc.ListGroupItem( dbc.Button("Next", color="primary", href="/build/farm") ),
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
    if pathname == '/' or pathname == '/build/turbine':
        return turbine.layout
    elif pathname == '/build/farm':
        return farm.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)


import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
import dash_html_components as html
from flask.globals import current_app

from app import app
from sidebar_nav import submenu_1, submenu_2, submenu_3, SIDEBAR_STYLE, CONTENT_STYLE
from apps.floris_connection.run_floris import calculate_wake
import apps.floris_data

next_button = dbc.Button("Next", id="next-button", color="primary", href="/", style={"top": '500',}) #style={'order':'last'}
sidebar_toggle = dbc.Button("Sidebar", outline=True, color="secondary", className="mr-1", id="btn_sidebar") #style={'order':'first'} #we can make this a hamburger menu icon later

navbar = dbc.NavbarSimple(
    [
        dbc.Row(
            [
                sidebar_toggle,
                next_button
            ]
        )   
    ],
    brand="Nav Bar",
    color="dark",
    dark=True,
    fluid=True,
)

sidebar = html.Div(
    [
        html.H2("Navigation Menu", className="display-6"),
        html.Hr(),
        dbc.Nav(submenu_1 + submenu_2 + submenu_3, vertical=True),
    ],
    style=SIDEBAR_STYLE,
    id="sidebar",
)
content = html.Div(
    id="page-content",
    style=CONTENT_STYLE)

app.layout = dbc.Container(
    [

        # dbc.Jumbotron( html.H1("FLORIS Dashboard", className="display-3")),
        navbar,
        html.Div(
        [
            
            sidebar,
            content,
            dcc.Store(id='side_click'),
            dcc.Location(id="url"),
        ],
        )
    ]

)

if __name__ == '__main__':
    app.run_server(debug=True)

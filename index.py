
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from app import app
from sidebar_nav import submenu_1, submenu_2, submenu_3, SIDEBAR_STYLE, CONTENT_STYLE

nav_button = dbc.ButtonGroup(
    [
        dbc.Button("Back", id="back-button", color="primary", href="/", style={"top": '500',}),
        dbc.Button("Next", id="next-button", color="primary", href="/", style={"top": '500'}), 
    ],
    size="md",
    className="mr-1",
)
sidebar_toggle = dbc.Button(children=[html.Img(src="/assets/bars.png", style={'width':'25px', "height": "20px"})], className="btn-dark btn-sm", outline='light', id="btn_sidebar", style={"margin-right": "7px", 'height': '32px'}) 

navbar = dbc.NavbarSimple(
    [
        dbc.Row(
            [
                dbc.Col([
                    sidebar_toggle,
                    nav_button
                ],)
            ]
        )   
    ],
    color="dark",
    dark=True,
    fluid=True,
)

sidebar = dbc.Card(
    [
        dbc.Nav(submenu_1 + submenu_2 + submenu_3, vertical=True),
    ],
    style=SIDEBAR_STYLE,
    id="sidebar",
)
content = dbc.Card(
    id="page-content",
    style=CONTENT_STYLE)

app.layout = dbc.Container(
    [
        

        dbc.Jumbotron( html.H1("FLORIS Dashboard", className="display-3")),
        navbar,
        sidebar,
        content,
        dcc.Location(id="url"),
        dcc.Store(id='side_click'),
        dcc.Store(id='floris-inputs'),
        dcc.Store(id='floris-outputs'),
    ],
    fluid=True
)

if __name__ == '__main__':
    app.run_server(debug=True)

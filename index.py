
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from app import app
from sidebar_nav import SIDEBAR_STYLE, CONTENT_STYLE

nav_button = dbc.ButtonGroup(children=[
        dbc.Button("Back", id="back-button", color="primary", href="/", style={"top": '500'}),
        dbc.Button("Next", id="next-button", color="primary", href="/", style={"top": '500'}), 
    ],
    size="md",
    className="mr-1",
)

navigation_menu = dbc.NavbarSimple(
    children=[
        dbc.Button(
            children=[
                html.Img(
                    src="/assets/home.png", 
                    style={'width':'30px', 'align':'center'}
                )
            ], 
            # className="btn-sm mr-1 btn-outline-light btn-dark", 
            className="btn-sm mr-1 btn-light", 
            href="/",
            id="home-button",
        ),
        nav_button
    ],
    brand="FLORIS Dashboard",
    brand_href="/",
    color="dark",
    dark=True,
    fluid=True,
)

sidebar = dbc.Card(
    dbc.Nav(
        children=[
            html.H2("Model Builder", style={'font-size':'14px'}),
            dbc.NavItem(dbc.NavLink("Atmospheric Conditions",  active="exact",href="/build/windrose")),
            dbc.NavItem(dbc.NavLink("Turbine", active="exact", href="/build/turbine")),
            dbc.NavItem(dbc.NavLink("Farm",  active="exact",href="/build/farm")),  
            dbc.NavItem(dbc.NavLink("Wake Model", active="exact", href="/build/wakemodel")),
            dbc.NavItem(dbc.NavLink("Review", active="exact", href="/build/review")),
            html.Hr(),
            html.H2("Results", style={'font-size':'14px'}),
            dbc.NavItem(dbc.NavLink("AEP", active="exact", href="/aep-results")),
        ],
        vertical=True,
        pills=True
    ),
    style=SIDEBAR_STYLE,
    id="sidebar",
)
content = dbc.Card(
    id="page-content",
    style=CONTENT_STYLE
)

app.layout = dbc.Container(children=[
        dbc.Row(
            dbc.Col(
                dbc.Jumbotron( 
                    [   
                       dbc.Row([
                            html.H1("FLORIS Dashboard", className="display-3 mr-3", style={'color':'white'}),
                       ]),
                    ],
                    style={'background-image':'url("/assets/banner.png")', 'background-repeat':'no-repeat', 'background-position':'top left'}       
                ),
            ),
        ),
        dbc.Row(
            dbc.Col(
                navigation_menu
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    sidebar,
                    width=2
                ),
                dbc.Col(
                    content,
                    width=10
                )
            ],
            no_gutters=True #we can remove this if anything
        ),
        dcc.Location(id="url"),
        dcc.Store(id='side_click'),
        dcc.Store(id='initial-input-store'),
        dcc.Store(id='turbine-input-store'),
        dcc.Store(id='wind-rose-input-store'),
        dcc.Store(id='final-input-store'),
        dcc.Store(id='floris-outputs'),
    ],
    fluid=True
)

if __name__ == '__main__':
    app.run_server(debug=True)

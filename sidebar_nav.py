
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask.globals import current_app

from app import app
from apps.model_builder import turbine_layout, farm_layout, atmos_cond_layout, wake_layout, review_layout, import_layout  
from apps.floris_connection.run_floris import calculate_wake
import apps.floris_data
import dash
from apps import home_layout #, dashboard

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 200,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

NAVIGATION_ITEMS = [
    "/",
    "/build/getting-started",
    "/build/windrose",
    "/build/turbine",
    "/build/farm",
    "/build/wakemodel",
    "/build/review",
    "/calculate",
    "/floris-dashboard"
]

home_page = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Home", active="exact", href="/")),
            ],
            pills=True
        ),
    ],
)

MB_progress_card = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Getting Started", active="exact", href="/build/getting-started")),
                dbc.NavItem(dbc.NavLink("Atmospheric Conditions",  active="exact",href="/build/windrose")),
                dbc.NavItem(dbc.NavLink("Turbine", active="exact", href="/build/turbine")),
                dbc.NavItem(dbc.NavLink("Farm",  active="exact",href="/build/farm")),  
                dbc.NavItem(dbc.NavLink("Wake Model", active="exact", href="/build/wakemodel")),
                dbc.NavItem(dbc.NavLink("Review", active="exact", href="/build/review")),
                dbc.NavItem(dbc.NavLink("Calculate", active="exact", href="/calculate")),
            ],
            vertical=True,
            pills=True,
        ),
    ],
)

FLORIS_dashboard = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Floris Dashboard", active="exact", href="/floris-dashboard")),
            ],
            pills=True,
        ),
    ],
)

submenu_1 = [
    html.Li(
        dbc.Row(
            [
                dbc.Col("Home"),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-1",
    ),
    dbc.Collapse([home_page],
        id="submenu-1-collapse",
        is_open=True
    ),
]

submenu_2 = [
    html.Li(
        dbc.Row(
            [
                dbc.Col("Model Builder"),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-2",
    ),
    dbc.Collapse([MB_progress_card,],
        id="submenu-2-collapse",
        is_open=True,
    ),
]

submenu_3 = [
    html.Li(
        dbc.Row(
            [
                dbc.Col("FLORIS Dashboard"),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-3",
    ),
    dbc.Collapse(
        [
            FLORIS_dashboard,
            dbc.NavLink("Page 2.1", href="/page-2/1"),
            dbc.NavLink("Page 2.2", href="/page-2/2"),
        ],
        id="submenu-3-collapse",
        is_open=True
    ),
]

next_button = [html.Li(
        dbc.Row(
            [
                dbc.Col(dbc.Button("Next", id="next-button", color="primary", href="/", style={"top": '500',}))
            ])
        )]


sidebar = html.Div(
    [
        html.H2("Navigation Menu", className="display-6"),
        html.Hr(),
        dbc.Nav(submenu_1 + submenu_2 + submenu_3 + next_button, vertical=True),
    ],
    style=SIDEBAR_STYLE,
    id="sidebar",
)

app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                dbc.Jumbotron( html.H1("FLORIS Dashboard", className="display-3") )
            )
        ),
        dbc.Row([
            # Progress tracker
            dbc.Col([
                sidebar,
                
            ], width=2),
            # Content area
            dbc.Col(id="page-content"),
        ]),
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='floris-inputs'),
    ],
    fluid=True,
)


# this function is used to toggle the is_open property of each Collapse
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [1,2,3]:
    app.callback(
        Output(f"submenu-{i}-collapse", "is_open"),
        [Input(f"submenu-{i}", "n_clicks")],
        [State(f"submenu-{i}-collapse", "is_open")],
    )(toggle_collapse)


@app.callback(
    Output('page-content', 'children'),
    Output('next-button', 'href'),
    Input('url', 'pathname'), 
)
def display_page(pathname):
    """
    Args:
        pathname (str): current url of the website

    Return:
        html.Div: layout of the current page
        str: url of the next page for navigation button
    """
    print(NAVIGATION_ITEMS)
    if pathname not in NAVIGATION_ITEMS:
        layout = dbc.Jumbotron([
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognized..."),
            ])
        next_nav = NAVIGATION_ITEMS[0]
        return layout, next_nav

    if pathname == '/':
        layout = home_layout.layout
        next_nav = NAVIGATION_ITEMS[ NAVIGATION_ITEMS.index(pathname) + 1 ]
        return layout, next_nav
    elif pathname == '/calculate':
        # TODO: ensure the input dict is valid
        
        cts, powers, ave_vels, ais = calculate_wake(apps.floris_data.default_input_dict)
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
        layout = html.Div([results])
        next_nav = NAVIGATION_ITEMS[ NAVIGATION_ITEMS.index(pathname) + 1 ]
        return layout, next_nav
    elif pathname == '/floris-dashboard':
        layout = html.Div(
            [
                # dbc.Row("Loading..."),
                "Loading",
                dbc.Spinner(color="primary", type="grow"),
                dbc.Spinner(color="secondary", type="grow"),
                dbc.Spinner(color="success", type="grow"),
                dbc.Spinner(color="warning", type="grow"),
                dbc.Spinner(color="danger", type="grow"),
                dbc.Spinner(color="info", type="grow"),
                dbc.Spinner(color="dark", type="grow"),
            ], id="Link-to-dashboard"
        )
        next_nav = NAVIGATION_ITEMS[0]
        return layout, next_nav

    # TODO: REMOVE THIS
    apps.floris_data.user_defined_dict = apps.floris_data.default_input_dict

    next_nav = NAVIGATION_ITEMS[ NAVIGATION_ITEMS.index(pathname) + 1 ]
    if pathname == '/build/getting-started':
        layout = import_layout.layout
    elif pathname == '/build/turbine':
        layout = turbine_layout.layout
    elif pathname == '/build/farm':
        layout = farm_layout.layout
    elif pathname == '/build/windrose':
        layout = atmos_cond_layout.layout
    elif pathname == '/build/wakemodel':
        layout = wake_layout.layout
    elif pathname == '/build/review':
        layout = review_layout.layout
    
    return layout, next_nav


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)
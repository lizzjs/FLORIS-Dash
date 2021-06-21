
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask.globals import current_app

from app import app
from apps.model_builder import turbine_layout, farm_layout, import_layout, atmos_cond_layout, wake_layout, review_layout
from apps.floris_connection.run_floris import calculate_wake
import apps.floris_data
import apps.dashboard

NAVIGATION_ITEMS = [
    "/",
    "/build/windrose",
    "/build/turbine",
    "/build/farm",
    "/build/wakemodel",
    "/build/review",
    "/calculate",
    "/floris-dashboard"
]

sidebar_style = {
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
        dbc.Nav(
            [
                # dbc.NavItem(dbc.NavLink("Home", active="exact", href="/")),
                dbc.NavItem(dbc.NavLink("Atmospheric Conditions",  active="exact",href="/build/windrose")),
                dbc.NavItem(dbc.NavLink("Turbine", active="exact", href="/build/turbine")),
                dbc.NavItem(dbc.NavLink("Farm",  active="exact",href="/build/farm")),  
                dbc.NavItem(dbc.NavLink("Wake Model", active="exact", href="/build/wakemodel")),
                dbc.NavItem(dbc.NavLink("Review", active="exact", href="/build/review")),
                dbc.NavItem(dbc.NavLink("Calculate", active="exact", href="/calculate")),
                dbc.NavItem(dbc.NavLink("Floris Dashboard", active="exact", href="/floris-dashboard")),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=sidebar_style,
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
                dbc.NavItem(dbc.NavLink("Home", active="exact", href="/")),
                progress_card,
                dbc.Button("Next", id="next-button", color="primary", href="/")
            ], width=2),

            # Content area
            dbc.Col(id="page-content")
        ]),
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='floris-inputs'),
    ],
    fluid=True,
)

@app.callback(
    Output('page-content', 'children'),
    Output('next-button', 'href'),
    Input('url', 'pathname')
)
def display_page(pathname):
    """
    Args:
        pathname (str): current url of the website

    Return:
        html.Div: layout of the current page
        str: url of the next page for navigation button
    """
    if pathname not in NAVIGATION_ITEMS:
        layout = dbc.Jumbotron([
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognized..."),
            ])
        next_nav = NAVIGATION_ITEMS[0]
        return layout, next_nav

    if pathname == '/calculate':
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
        # next_nav = NAVIGATION_ITEMS[0]

        next_nav = NAVIGATION_ITEMS[ NAVIGATION_ITEMS.index(pathname) + 1 ]
        print(next_nav)
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
    if pathname == '/':
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

if __name__ == '__main__':
    app.run_server(debug=True)

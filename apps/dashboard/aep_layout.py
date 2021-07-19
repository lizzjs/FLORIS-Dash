
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
import dash_html_components as html

# Imported but not used. This loads the callback functions into the web page.
import apps.dashboard.aep_callbacks

graph_layout = html.Div([
    dbc.Row([
            dbc.Col(dcc.Graph(id='model-comparison-graph')),
            dbc.Col(dcc.Graph(id='compute-time-graph'))
        ],
        justify="around"
    ),
    # dbc.Row(
    #     dbc.Col(dcc.Graph(id='energy-gain-graph')
    # ),
    # justify="center"
    # ),
    dbc.Row(
        [
            dbc.Col(dcc.Graph(id='aep-farm-graph')),
            dbc.Col(dcc.Graph(id='aep-windrose-graph'))
        ],
        justify="around"
    ),
    

])

layout = html.Div(
    children=[
        #This row will overlap the content below it in order to avoid having the 
        #download button included in the pdf export
        # dbc.Row([ 
        #     dbc.Col(width=11),
        #     dbc.Col(
        #         dbc.Button(
        #             children=[
        #                     html.Img(
        #                         src="/assets/file-download.png", 
        #                         style={'width':'30px', 'align':'center'}
        #                     )
        #                 ], 
        #                 className="btn-light", id='js', n_clicks=0
        #         ), 
        #         style={'margin':'25px 0px 0px 30px'}
        #     ),
        # ],style={'height':'0px'},),
        html.Div([
            dbc.Row(
                dbc.Col(html.H2("Annual Energy Production Dashboard")), 
                style={'height':'55px'},
            ),
            html.Br(),
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dbc.Spinner(
                                graph_layout,
                                id="results-spinner",
                                type="circle"
                            ),
                        ]
                    )
                ], className='cardDesign'
            )
        ], id='print'),
        dbc.Row([
                dbc.Button(
                    children=[
                            "Export to PDF ",
                            html.Img(
                                src="/assets/file-download.png", 
                                style={'width':'20px'}
                            )
                        ], 
                        className="btn-dark", id='js', n_clicks=0
                ), 
                # style={'margin':'25px 0px 0px 30px'} 
            ], justify='center'),
    ], id='main'
)
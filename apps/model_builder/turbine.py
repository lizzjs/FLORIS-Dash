
import dash_html_components as html
import dash_core_components as dcc
from app import app, colors

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.turbine_callbacks

layout = html.Div(
    
    id="main_layout",
    children=[

    html.Div(
        style={'margin': '50px 50px 50px 800px'},
        children=[

    dcc.Tabs(id='tabs-example', value='tab-1', children=[
    
        dcc.Tab(label='Geometry', children=[
    
            #TSR
            html.P('Tip Speed Ratio:'),
            dcc.Input(
                id="input-TSR", 
                type="number", 
                min=0, 
                max=20, 
                placeholder='TSR input'
            ),
            html.Div(id='TSR-numeric-input-output'),
    
            #Blade Count
            html.P('Blade Count:'),
            html.Div(
                dcc.Slider(
                    id="slider-bladecount",
                    min=1, 
                    max=9, 
                    marks={i: '{}'.format(i) for i in range(10)}, 
                    value=1, 
                ), style={'width': '40%', 'padding': '0px 20px 20px 20px'}),
            html.Div(id='updatemode-output-bladecount', style={'margin-left': 450}),

            #Blade Pitch
            html.P('Blade Pitch:'),
            dcc.Input(
                id="input-bladepitch", 
                type="number", 
                min=0, 
                max=20, 
                placeholder='Blade pitch input'
            ),
            html.Div(id='bladepitch-numeric-input-output'),

            #Generator Efficiency
            html.P('Generator Efficiency:'),
            dcc.Input(
                id="input-genEff", 
                type="number", 
                min=0, 
                max=20, 
                placeholder='Generator Efficiency input'
            ),
            html.Div(id='genEff-numeric-input-output'),
                
            #Hub Height
            html.P('Hub Height:'),
            dcc.Input(
                id="input-hubheight", 
                type="number", 
                min=0, 
                max=20, 
                value=3 
            ),
            html.Div(
                dcc.Slider(
                    id="slider-hubheight", min=0, max=20, 
                    marks={i: str(i) for i in range(21)}, 
                    value=3
                ),
                style={'width': '40%', 'padding': '0px 20px 20px 20px'}
            ),

            #ngrid
            html.P('ngrid:'),
            html.Div(
                dcc.Slider(
                    id="slider-ngrid",
                    min=1, 
                    max=9, 
                    marks={i: '{}'.format(i) for i in range(10)}, 
                    value=1, 
                ), style={'width': '40%', 'padding': '0px 20px 20px 20px'}),
            html.Div(id='updatemode-output-ngrid', style={'margin-left': 450}),

            #pP
            html.P('pP:'),
            dcc.Input(
                id="input-pP", 
                type="number", 
                min=0, 
                max=20, 
                step=0.01,
                placeholder='pP input'
            ),
            html.Div(id='pP-numeric-input-output'),

            #pT
            html.P('pT:'),
            dcc.Input(
                id="input-pT", 
                type="number", 
                min=0, 
                max=20, 
                step=0.01,
                placeholder='pT input'
            ),
            html.Div(id='pT-numeric-input-output'),

            #rloc
            html.P('rloc:'),
            dcc.Input(
                id="input-rloc", 
                type="number", 
                min=0, 
                max=20, 
                step=0.01,
                placeholder='rloc input'
            ),
            html.Div(id='rloc-numeric-input-output'),

            #Tilt Angle
            html.P('Tilt Angle:'),
            dcc.Input(
                id="input-tiltang", 
                type="number", 
                min=0, 
                max=20, 
                value=0.0
            ),
            html.Div(
                dcc.Slider(
                    id="slider-tiltang", 
                    min=0, 
                    max=20, 
                    marks={i: str(i) for i in range(21)}, 
                    value=0.0,
                    step=0.01,
                    updatemode='drag'
                ),
                style={'width': '40%', 'padding': '0px 20px 20px 20px'}
            ),

            #Use points on perimeter
            html.P('Use points on perimeter:'),
            dcc.RadioItems(
                id = 'radio-input',
                options=[
                    {'label': 'Yes', 'value': 1},
                    {'label': 'No', 'value': 0},
                ]
            ), 
            html.Div(id='radio-output'),

            #Yaw Angle
            html.P('Yaw Angle:'),
            dcc.Input(
                id="input-yawang", 
                type="number", 
                min=0, 
                max=20, 
                value=0.0
            ),
            html.Div(
                dcc.Slider(
                    id="slider-yawang", min=0, max=20, 
                    marks={i: str(i) for i in range(21)}, 
                    value=0.0,
                    step=0.01,
                    updatemode='drag'
                ),
                style={'width': '40%', 'padding': '0px 20px 20px 20px'}
            ),

            #Rotor Diameter
            html.P('Rotor Diameter:'),
            dcc.Input(
                id="input-rotordiam", 
                type="number", 
                min=0, 
                max=20, 
                value=3
            ),
            html.Div(
                dcc.Slider(
                    id="slider-rotordiam", min=0, max=20, 
                    marks={i: str(i) for i in range(21)}, 
                    value=3
                ),
                style={'width': '40%', 'padding': '0px 20px 20px 20px'}
            ),            
        ]),

        dcc.Tab(label='Cp/Ct Table', children=[
            dcc.Textarea(
                id='textarea-state-example',
                placeholder='Paste Cp/Ct table values here',
                style={'width': '30%', 'height': 300},
            ),
            html.Button('Submit', 
                id='textarea-state-example-button', 
                n_clicks=0,
                style={'margin': '10px'}
            ),
            html.Div(
                id='textarea-state-example-output', 
                style={'whiteSpace': 'pre-line'},
            ),
            html.Div(
                html.Hr(style={'width': '40%','margin': '10px'}),
            ),
            dcc.Upload(
                id='upload-data', 
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '20%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                # Allow multiple files to be uploaded
                multiple=True #change to true if you want multiple files 
            ),
            html.Div(id='output-div'),
            dcc.Graph(id="Mygraph1"),
            dcc.Graph(id="Mygraph2"),            
            # dcc.Graph(
            #     figure={
            #         'data': [
            #             {'x': [1, 2, 3], 'y': [1, 4, 1],
            #                 'type': 'bar', 'name': 'SF'},
            #             {'x': [1, 2, 3], 'y': [1, 2, 3],
            #              'type': 'bar', 'name': u'Montréal'},
            #         ]
            #     }
            # )
        ]),
    ]),
]),
       
dcc.Link('Next', href='/builder/farm'),

])

#Combining Tabs with callback and slider (input and slider not interacting)
from os import path
import dash
# import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='Geometry', children=[
                #TSR
                    html.P('Tip Speed Ratio:'),
                    dcc.Input(id="input-TSR", type="number", min=0, max=20, placeholder='TSR input'
                    ),
                    html.Div(id='TSR-numeric-input-output'),
                #Blade Count
                    html.P('Blade Count:'),
                    html.Div(dcc.Slider(id="slider-bladecount",min=1, max=9, marks={i: '{}'.format(i) for i in range(10)}, value=1, 
                    ), style={'width': '40%', 'padding': '0px 20px 20px 20px'}),
                    html.Div(id='updatemode-output-bladecount', style={'margin-left': 450}),
                #Blade Pitch
                    html.P('Blade Pitch:'),
                    dcc.Input(id="input-bladepitch", type="number", min=0, max=20, placeholder='Blade pitch input'
                    ),
                    html.Div(id='bladepitch-numeric-input-output'),
                #Generator Efficiency
                    html.P('Generator Efficiency:'),
                    dcc.Input(id="input-genEff", type="number", min=0, max=20, placeholder='Generator Efficiency input'
                    ),
                    html.Div(id='genEff-numeric-input-output'),
                    
                #Hub Height
                    html.P('Hub Height:'),
                    dcc.Input(id="input-hubheight", type="number", min=0, max=20, value=3 
                    ),
                    html.Div(dcc.Slider(
                        id="slider-hubheight", min=0, max=20, 
                        marks={i: str(i) for i in range(21)}, 
                        value=3
                    ), style={'width': '40%', 'padding': '0px 20px 20px 20px'}),

                #ngrid
                    html.P('ngrid:'),
                    html.Div(dcc.Slider(id="slider-ngrid",min=1, max=9, marks={i: '{}'.format(i) for i in range(10)}, value=1, 
                    ), style={'width': '40%', 'padding': '0px 20px 20px 20px'}),
                    html.Div(id='updatemode-output-ngrid', style={'margin-left': 450}),

                #pP
                    html.P('pP:'),
                    dcc.Input(id="input-pP", type="number", min=0, max=20, step=0.01,placeholder='pP input'
                    ),
                    html.Div(id='pP-numeric-input-output'),
                #pT
                    html.P('pT:'),
                    dcc.Input(id="input-pT", type="number", min=0, max=20, step=0.01,placeholder='pT input'
                    ),
                    html.Div(id='pT-numeric-input-output'),
                #rloc
                    html.P('rloc:'),
                    dcc.Input(id="input-rloc", type="number", min=0, max=20, step=0.01,placeholder='rloc input'
                    ),
                    html.Div(id='rloc-numeric-input-output'),
                #Tilt Angle
                    html.P('Tilt Angle:'),
                    dcc.Input(
                        id="input-tiltang", type="number", min=0, max=20, value=0.0
                    ),
                    html.Div(dcc.Slider(
                        id="slider-tiltang", min=0, max=20, 
                        marks={i: str(i) for i in range(21)}, 
                        value=0.0,
                        step=0.01,
                        updatemode='drag'
                    ), style={'width': '40%', 'padding': '0px 20px 20px 20px'}),

                #Use points on perimeter
                    html.P('Use points on perimeter:'),
                #Yaw Angle
                    html.P('Yaw Angle:'),
                    dcc.Input(
                        id="input-yawang", type="number", min=0, max=20, value=0.0
                    ),
                    html.Div(dcc.Slider(
                        id="slider-yawang", min=0, max=20, 
                        marks={i: str(i) for i in range(21)}, 
                        value=0.0,
                        step=0.01,
                        updatemode='drag'
                    ), style={'width': '40%', 'padding': '0px 20px 20px 20px'}),

                #Rotor Diameter
                    html.P('Rotor Diameter:'),
                    dcc.Input(
                        id="input-rotordiam", type="number", min=0, max=20, value=3
                    ),
                    html.Div(dcc.Slider(
                        id="slider-rotordiam", min=0, max=20, 
                        marks={i: str(i) for i in range(21)}, 
                        value=3
                    ), style={'width': '40%', 'padding': '0px 20px 20px 20px'}),
                
        ]),
        dcc.Tab(label='Cp/Ct Table', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [1, 4, 1],
                            'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [1, 2, 3],
                         'type': 'bar', 'name': u'Montréal'},
                    ]
                }
            )
        ]),
    ]),
])
#TAB1-TSR
@app.callback(Output('TSR-numeric-input-output', 'children'),
              Input('input-TSR', 'value'))
def GeomTab_TSR_output(input_value):
    print(input_value)
    # return input_value

#TAB1-Blade count
@app.callback(Output('updatemode-output-bladecount', 'children'),
              Input('slider-bladecount', 'value'))
def GeomTab_bladecount_display_value(value):
    return 'Blades: {}'.format(value)

#TAB1-Blade pitch
@app.callback(Output('bladepitch-numeric-input-output', 'children'),
              Input('input-bladepitch', 'value'))
def GeomTab_Bladepitch_output(input_value):
    print(input_value)
    # return input_value

#TAB1-Generator efficiency
@app.callback(Output('genEff-numeric-input-output', 'children'),
              Input('input-genEff', 'value'))
def GeomTab_genEff_output(input_value):
    print(input_value)
    # return input_value

#TAB1-Hub height
@app.callback(Output('input-hubheight', 'value'),
              Output('slider-hubheight', 'value'),
                Input('input-hubheight', 'value'),
                Input('slider-hubheight', 'value'))    
def GeomTab_hubheight_output(input_value, slider_value):
            ctx = dash.callback_context
            trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
            value = input_value if trigger_id == "input-hubheight" else slider_value
            print(input_value, slider_value, value)
            print(ctx.triggered)
            return value, value

#TAB1-ngrid
@app.callback(Output('updatemode-output-ngrid', 'children'),
              Input('slider-ngrid', 'value'))
def GeomTab_bladecount_display_value(value):
    return 'ngrid: {}'.format(value)

#TAB1-pP
@app.callback(Output('pP-numeric-input-output', 'children'),
              Input('input-pP', 'value'))
def GeomTab_pP_output(input_value):
    print(input_value)
    # return input_value

#TAB1-pT
@app.callback(Output('pT-numeric-input-output', 'children'),
              Input('input-pT', 'value'))
def GeomTab_pT_output(input_value):
    print(input_value)
    # return input_value

#TAB1-rloc
@app.callback(Output('rloc-numeric-input-output', 'children'),
              Input('input-rloc', 'value'))
def GeomTab_rloc_output(input_value):
    print(input_value)
    # return input_value

#TAB1-Tilt angle
@app.callback(Output('input-tiltang', 'value'),
              Output('slider-tiltang', 'value'),
                Input('input-tiltang', 'value'),
                Input('slider-tiltang', 'value'))
def GeomTab_tiltang_output(input_value, slider_value):
            ctx = dash.callback_context
            trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
            value = input_value if trigger_id == "input-tiltang" else slider_value
            print(input_value, slider_value, value)
            print(ctx.triggered)
            return value, value

#TAB1-Yaw angle
@app.callback(Output('input-yawang', 'value'),
              Output('slider-yawang', 'value'),
                Input('input-yawang', 'value'),
                Input('slider-yawang', 'value'))
def GeomTab_yawang_output(input_value, slider_value):
            ctx = dash.callback_context
            trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
            value = input_value if trigger_id == "input-yawang" else slider_value
            print(input_value, slider_value, value)
            print(ctx.triggered)
            return value, value

#TAB1-Rotor Diameter
@app.callback(Output('input-rotordiam', 'value'),
              Output('slider-rotordiam', 'value'),
                Input('input-rotordiam', 'value'),
                Input('slider-rotordiam', 'value'))
def GeomTab_rotordiam_output(input_value, slider_value):
            ctx = dash.callback_context
            trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
            value = input_value if trigger_id == "input-rotordiam" else slider_value
            print(input_value, slider_value, value)
            print(ctx.triggered)
            return value, value

if __name__ == '__main__':
    app.run_server(debug=True)
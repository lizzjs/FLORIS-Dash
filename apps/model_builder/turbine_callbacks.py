
import dash
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import io
import pandas as pd

from app import app, colors
import base64
import apps.model_builder.home_callbacks
import plotly.express as px

_mod_df = pd.DataFrame({'x': [1,2,3],'y' : [4,5,6]})

#TAB1-TSR
@app.callback(
    Output('TSR-numeric-input-output', 'children'),
    Input('input-TSR', 'value')
)
def GeomTab_TSR_output(input_value):
    # print(input_value)
    return input_value

#TAB1-Blade count
@app.callback(
    Output('updatemode-output-bladecount', 'children'),
    Input('slider-bladecount', 'value')
)
def GeomTab_bladecount_display_value(value):
    return 'Blades: {}'.format(value)

#TAB1-Blade pitch
@app.callback(
    Output('bladepitch-numeric-input-output', 'children'),
    Input('input-bladepitch', 'value')
)
def GeomTab_Bladepitch_output(input_value):
    # print(input_value)
    return input_value

#TAB1-Generator efficiency
@app.callback(
    Output('genEff-numeric-input-output', 'children'),
    Input('input-genEff', 'value')
)
def GeomTab_genEff_output(input_value):
    # print(input_value)
    return input_value

#TAB1-Hub height
@app.callback(
    Output('input-hubheight', 'value'),
    Input('input-hubheight', 'value'),
)
def GeomTab_hubheight_output(input_value):
    return input_value

#TAB1-ngrid
@app.callback(
    Output('updatemode-output-ngrid', 'children'),
    Input('slider-ngrid', 'value')
)
def GeomTab_bladecount_display_value(value):
    return 'ngrid: {}'.format(value)

#TAB1-pP
@app.callback(
    Output('pP-numeric-input-output', 'children'),
    Input('input-pP', 'value')
)
def GeomTab_pP_output(input_value):
    # print(input_value)
    return input_value

#TAB1-pT
@app.callback(
    Output('pT-numeric-input-output', 'children'),
    Input('input-pT', 'value')
)
def GeomTab_pT_output(input_value):
    # print(input_value)
    return input_value

#TAB1-rloc
@app.callback(
    Output('rloc-numeric-input-output', 'children'),
    Input('input-rloc', 'value')
)
def GeomTab_rloc_output(input_value):
    # print(input_value)
    return input_value

#TAB1-Tilt angle
@app.callback(
    Output('slider-tiltang', 'value'),
    Input('slider-tiltang', 'value')
)
def GeomTab_tiltang_output(slider_value):
    return slider_value

#TAB1-Points on Perimeter
@app.callback(
    Output('radio-output', 'children'),
    [Input('radio-input', 'value')]
)
def GeomTab_radiobutton_value(value):
    if value == 1:
        value = True
    else:
        value = False
    # print(value)

#TAB1-Yaw angle
@app.callback(
    Output('slider-yawang', 'value'),
    Input('slider-yawang', 'value')
)
def GeomTab_yawang_output(slider_value):
    return slider_value

#TAB1-Rotor Diameter
@app.callback(
    Output('input-rotordiam', 'value'),
    Input('input-rotordiam', 'value'),
)
def GeomTab_rotordiam_output(input_value):
    return input_value




#TAB2
@app.callback(
    Output('Mygraph1', 'figure'),
    Output('Mygraph2', 'figure'),
    Input('performance-datatable', 'data')
)
def display_graphs(data):
    fig1 = px.line(
        pd.DataFrame(data),
        template="seaborn",
    )

    fig2 = px.line(
        pd.DataFrame(data),
        template="seaborn",
    )
    return fig1, fig2

@app.callback(
    [Output('performance-datatable', 'data'),
    Output('performance-datatable', 'columns')],
    Input("performance-tab", "value")
)
def performance_display_table(data):
    _module_df = pd.DataFrame({'x': [1,2,3],'y' : [4,5,6]})
    columns = [{"name": i, "id": i} for i in _module_df.columns]
    return _module_df.to_dict("rows"), columns

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    if 'xls' in filename:
        # Assume that the user uploaded an excel file
        df = pd.read_excel(io.BytesIO(decoded), sheet_name='cpctws')
    elif 'json' in filename:
        df = pd.read_json(decoded)
    else:
        raise ValueError("The file imported was not in the expected file format.")

    return df
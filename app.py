#Combining Tabs with callback and slider (input and slider not interacting)
from os import path
import dash
# import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import dash_table as dt
import plotly.express as px
import base64
import io
import plotly.graph_objs as go


from layout import main_layout

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {"graphBackground": "#F5F5F5", "background": "#ffffff", "text": "#000000"}

app.layout = main_layout

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
    Output('slider-hubheight', 'value'),
    Input('input-hubheight', 'value'),
    Input('slider-hubheight', 'value')
)
def GeomTab_hubheight_output(input_value, slider_value):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "input-hubheight" else slider_value
    # print(input_value, slider_value, value)
    # print(ctx.triggered)
    return value, value

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
    Output('input-tiltang', 'value'),
    Output('slider-tiltang', 'value'),
    Input('input-tiltang', 'value'),
    Input('slider-tiltang', 'value')
)
def GeomTab_tiltang_output(input_value, slider_value):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "input-tiltang" else slider_value
    # print(input_value, slider_value, value)
    # print(ctx.triggered)
    return value, value

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
    Output('input-yawang', 'value'),
    Output('slider-yawang', 'value'),
    Input('input-yawang', 'value'),
    Input('slider-yawang', 'value')
)
def GeomTab_yawang_output(input_value, slider_value):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "input-yawang" else slider_value
    # print(input_value, slider_value, value)
    # print(ctx.triggered)
    return value, value

#TAB1-Rotor Diameter
@app.callback(
    Output('input-rotordiam', 'value'),
    Output('slider-rotordiam', 'value'),
    Input('input-rotordiam', 'value'),
    Input('slider-rotordiam', 'value')
)
def GeomTab_rotordiam_output(input_value, slider_value):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "input-rotordiam" else slider_value
    # print(input_value, slider_value, value)
    # print(ctx.triggered)
    return value, value

#TAB2
@app.callback(
    Output('Mygraph1', 'figure'),
    # Output('Mygraph2', 'figure') 
    [Input('upload-data', 'contents'),
    Input('upload-data', 'filename')])
def update_graph(contents, filename):
    print('inside update_graph')
    x = []
    y1 = []
    y2 = []
    if contents:
        contents = contents[0]
        filename = filename[0]
        df = parse_contents(contents, filename)
        # df = df.set_index(df.columns[0])
        x=df['Wind Speed']
        y1=df['Cp']
        y2=df['Ct']
    fig1 = go.Figure(
            data=[
                go.Scatter(
                    x=x, 
                    y=y1, 
                    mode='lines+markers')],
            # layout=go.Layout(
            #     plot_bgcolor=colors["graphBackground"],
            #     paper_bgcolor=colors["graphBackground"])
    )
    # fig2 = go.Figure(
    #         data=[
    #             go.Scatter(
    #                 x=x, 
    #                 y=y2, 
    #                 mode='lines+markers')],
    #         layout=go.Layout(
    #             plot_bgcolor=colors["graphBackground"],
    #             paper_bgcolor=colors["graphBackground"]
    # ))
    return fig1


def parse_contents(contents, filename):
    print('*')
    # print(contents)
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    print('****************')
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        # elif "txt" or "tsv" in filename:
        #     # Assume that the user upl, delimiter = r'\s+'oaded an excel file
        #     df = pd.read_csv(io.StringIO(decoded.decode("utf-8")), delimiter=r"\s+")
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    print('after exception')
    return df
    

    # for i in range 3:
    #     if df.column[i] == 'Cp':
    #         cp_data = df['Cp'],
    #     elif df.column[i] == 'Ct':
    #         ct_data = df['Ct']
    #     elif df.column[i] == 'Wind Speed':
    #         ws_data = df['Wind Speed']
    #     else:
    #         return html.Div([
    #             "File does not match expected 'Cp', 'Ct' and 'Wind Speed' column names."
    #         ])

    # print(df['Cp'])

    # line_graph1 = px.line(x=ws_data, y=cp_data)
    # line_graph2 = px.line(x=ws_data, y=ct_data)
    # # print(data)
    # return dcc.Graph(figure=line_graph1), dcc.Graph(figure=line_graph2) 
     

    # return html.Div([
    #     html.H5(filename),
#Can Delete
        # html.H6(datetime.datetime.fromtimestamp(date)),
        # html.P("Inset X axis data"),
        # dcc.Dropdown(id='xaxis-data',
        #              options=[{'label':x, 'value':x} for x in df.columns]),
        # html.P("Inset Y axis data"),
        # dcc.Dropdown(id='yaxis-data',
        #              options=[{'label':x, 'value':x} for x in df.columns]),
        # html.Button(id="submit-button", children="Create Graph"),
        # html.Hr(),

        # dt.DataTable(
        #     data=df.to_dict('records'),
        #     columns=[{'name': i, 'id': i} for i in df.columns],
        #     page_size=15
        # ),

        # dcc.Store(id='stored-data', data=df.to_dict('records')),
#Can Delete
        # # For debugging, display the raw contents provided by the web browser
        # html.Div('Raw Content'),
        # html.Pre(contents[0:200] + '...', style={
        #     'whiteSpace': 'pre-wrap',
        #     'wordBreak': 'break-all'
        # })
    # ])
#Can Delete
# @app.callback(Output('output-datatable', 'children'),
#               Input('upload-data', 'contents'),
#               State('upload-data', 'filename'),
#               State('upload-data', 'last_modified'))
# def update_output(list_of_contents, list_of_names, list_of_dates):
#     if list_of_contents is not None:
#         children = [
#             parse_contents(c, n, d) for c, n, d in
#             zip(list_of_contents, list_of_names, list_of_dates)]
#         return children


# @app.callback(Output('output-div', 'children'),
#               Input('submit-button','n_clicks'),
#               State('stored-data','data'),
#               State('xaxis-data','value'),
#               State('yaxis-data', 'value'))
# def make_graphs(n, data, cp_data, ct_data, ws_data):
#     if n is None:
#         return dash.no_update
#     else:
        


if __name__ == '__main__':
    app.run_server(debug=True)
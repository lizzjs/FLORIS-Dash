import pandas as pd 
import datetime as dt

import plotly.offline as pyo 
import plotly.graph_objs as go 
import plotly.express as px

import dash
import dash_core_components as dcc 
import dash_html_components as html 
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

card1 = dbc.Card([
    dbc.CardBody([
        html.P(['2 His Majesties Letter to the Lord Thresurer & other of the Lords to deliver the Charge of the Tower & Prisones thereunto S.r Wm Wade Knight which was done by the Earle of Dorsett and the Earle of Devonshire on Thursday in the Afternoon, at the Clock being the 15 of Aug. 1605'],
                className = "narrative"
            )
    ])
],className='cardDesign')

card2 = dbc.Card([
    dbc.CardBody([
               dcc.Graph(figure=dict(
                   data=[go.Pie(labels=labels,values=values)],
                   layout=dict(autosize=True)
               ),
               responsive=True,
               )
    ])        
],className='cardDesign')


card2_1 = dbc.Card([
    dbc.CardBody([
               dcc.Graph(figure=dict(
                   data=[go.Pie(labels=labels,values=values)]
               ))
    ])
 ],className='cardDesign')

card2_2 = dbc.Card([
    dbc.CardBody([
               dcc.Graph(figure=dict(
                   data=[go.Pie(labels=labels,values=values)]
               ))
    ])
 ],className='cardDesign')

card3 = dbc.Card([
    dbc.CardBody([
               dcc.Graph(figure=dict(
                   data=[go.Bar(x=labels,y=values)]
               ))
    ])        
],className='cardDesign')

app.layout = html.Div([
    html.Div([
        dbc.Row([
            dbc.Col([
                html.H3(['Report PDF Generator'])
            ]),
        ]),

        dbc.Row([
            dbc.Col([
                card1
            ],id="col1"),
        ]),

        dbc.Row([
            dbc.Col([
                card2
            ],id="col2"),
        ]),

        dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([card2_1],xs=12, sm=12, md=12, lg=6, xl=6,id="col3"),
                dbc.Col([card2_2],xs=12, sm=12, md=12, lg=6, xl=6,id="col4"),
            ])
        ]),
    ]),

        dbc.Row([
            dbc.Col([
                card3
            ],id="col5"),
        ]),
    ],id='print'),
    dbc.Button(children=['Download'],className="mr-1",id='js',n_clicks=0),
],id='main',)

app.clientside_callback(
    """
    function(n_clicks){
        if(n_clicks > 0){
            var opt = {
                margin: 1,
                filename: 'Results_Report.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 3},
                jsPDF: { unit: 'cm', format: 'a2', orientation: 'p' },
                pagebreak: { mode: ['avoid-all'] }
            };
            html2pdf().from(document.getElementById("print")).set(opt).save();
        }
    }
    """,
    Output('js','n_clicks'),
    Input('js','n_clicks')
)

if __name__ == '__main__':
    app.run_server(port='8050',debug=True)

# #js code
# function addScript(url) {
#     var script = document.createElement('script');
#     script.type = 'application/javascript';
#     script.src = url;
#     document.head.appendChild(script);
# }
# addScript('https://raw.githack.com/eKoopmans/html2pdf/master/dist/html2pdf.bundle.js');

# #css code
# @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');

# #main{
#     font-family: 'Montserrat', sans-serif;
#   }

# .cardDesign{
#     box-shadow:0 4px 8px 0 rgba(0, 0, 0, 0.2);
#     margin-top: 5px;
#     margin-bottom: 5px;
# }

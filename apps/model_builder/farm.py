
import dash_html_components as html
import dash_core_components as dcc

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.farm_callbacks

layout = html.Div(
    
    id="farm_layout",
    children=[
    
      dcc.Textarea(
          id='textarea-farm-layout',
          placeholder='Paste farm layout points here',
          style={'width': '30%', 'height': 300},
      ),
      html.Button('Submit', 
          id='textarea-farm-layout-button', 
          n_clicks=0,
          style={'margin': '10px'}
      ),
      # html.Div(
      #         id='textarea-farm-output', 
      #         style={'whiteSpace': 'pre-line'},
      #     ),
      dcc.Graph(id="farm-graph",),
    ]

)
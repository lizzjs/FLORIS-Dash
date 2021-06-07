
import dash_html_components as html

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.farm_callbacks

farm_layout = html.Div(
    
    id="farm_layout",
    children=[

        html.Div(
          "farm"
        ),

    ]

)
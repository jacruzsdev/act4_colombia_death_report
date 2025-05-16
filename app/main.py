import os

import dash
from dash import html, dcc  # Corrected import for html and dcc
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc  # Import Dash Bootstrap Components

from bq_data import get_data
from reports import views


def create_dash_app() -> dash.Dash:
    """
    Creates the Dash application with multiple pages, now using Bootstrap.

    Args:
        data (pd.DataFrame): The data to be displayed.

    Returns:
        dash.Dash: The Dash application instance.
    """
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])  # Use Bootstrap stylesheet
    app.config.suppress_callback_exceptions = True #suppress callback exceptions

    logo_uni = '/assets/logo.png'  # Correct relative path for Dash
    # Define the app layout with multiple pages
    app.layout = html.Div([
        # Add a logo to the upper right corner
        html.Header(
            html.Img(src=logo_uni, style={'height': '50px', 'transform': 'scale(0.5)'}), # Use the local path and scale
            style={'position': 'absolute', 'top': '0px', 'right': '5px', 'zIndex': 500}
        ),
        dcc.Location(id='url', refresh=False),
        dbc.Container(  # Use Bootstrap Container for layout
            html.Div(id='page-content'),
            fluid=True
        )
    ])

    # Create callbacks to switch between pages
    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def display_page(pathname):
        if pathname == '/mapa':
            return views.create_map(get_data.get_report_1())
        elif pathname == '/lineas':
            return views.create_line_chart(get_data.get_report_2())
        elif pathname == '/barras':
            return views.create_bar_chart(get_data.get_report_3())
        elif pathname == '/circular':
            return views.create_pie_chart(get_data.get_report_4())
        elif pathname == '/tabla':
            return views.create_table(get_data.get_report_5())
        elif pathname == '/histograma':
            return views.create_histogram(get_data.get_report_6())
        elif pathname == '/barras_apiladas':
            return views.create_stacked_bar_chart(get_data.get_report_7())
        else:
            return views.main_page()
    return app


def main():
    """
    Main function to run the Dash application.
    """
    app = create_dash_app()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))


if __name__ == '__main__':
    main()

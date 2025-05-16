from dash import html, dcc  # Corrected import for html and dcc
import dash_leaflet as dl
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def main_page() -> html.Div:
    return html.Div([
                html.H1("Maestría en IA", style={'textAlign': 'center'}),
                html.H2("UNIDAD 2. Aplicación web con dashborad interactivo en Python", style={'textAlign': 'center'}),
                html.H3("Actividad 4: Aplicación web interactiva para el análisis de mortalidad en Colombia", style={'textAlign': 'center'}),
                html.P("Este informe presenta un análisis de la mortalidad en Colombia durante el año 2019.", style={'textAlign': 'center'}),
                html.P("Maestrantes:", style={'textAlign': 'center'}),
                html.P("Jesus Andres Cruz Sanabria - jcruz47@unisalle.edu.co", style={'textAlign': 'center'}),
                html.P("Joaquín Ivan Barrera Lozada - jbarrera17@unisalle.edu.co", style={'textAlign': 'center'}),
                html.Div([
                    dbc.Button('Ver Mapa de distribución total de muertes por departamento en Colombia', href='/mapa', className='w-100 my-2'),
                    dbc.Button('Ver Total de muertes por mes en Colombia', href='/lineas', className='w-100 my-2'),
                    dbc.Button('Ver 5 ciudades más violentas de Colombia, considerando homicidios (códigos X95)', href='/barras', className='w-100 my-2'),
                    dbc.Button('Ver 10 ciudades con menor índice de mortalidad.', href='/circular', className='w-100 my-2'),
                    dbc.Button('Ver 10 principales causas de muerte en Colombia', href='/tabla', className='w-100 my-2'),
                    dbc.Button('Ver Distribución de muertes según rangos de edad quinquenales (0-4, 5-9, …, 85+ años)', href='/histograma', className='w-100 my-2'),
                    dbc.Button('Ver Total de muertes por sexo en cada departamento', href='/barras_apiladas', className='w-100 my-2'),
                ], className='d-flex flex-column align-items-center')
            ], style={'textAlign': 'center'})

def create_map(df: pd.DataFrame) -> html.Div:
    """
    Creates a map displaying the distribution of deaths per department.

    Args:
        df (pd.DataFrame): DataFrame containing the death data.

    Returns:
        dl.Map: The Dash Leaflet map.
    """
    markers = [
        dl.Marker(
            position=[row['Lat'], row['Long']],
            children=[
                dl.Tooltip(f"{row['DEPARTAMENTO']}: {row['n_muertes']} muertes")
            ]
        )
        for _, row in df.iterrows()
    ]
    colombia_map = dl.Map(
        center=[4, -72],
        zoom=6,
        children=[
            dl.TileLayer(),
            dl.FeatureGroup(children=markers)
        ],
        style={'width': '100%', 'height': '500px'}
    )
    return html.Div([
        html.H1("Distribución de Muertes por Departamento en Colombia", style={'textAlign': 'center'}),
        colombia_map,
        html.Div([
            dbc.Button('Ir a Inicio', href='/', className='w-100 my-2'),
            dbc.Button('Ver Total de muertes por mes en Colombia', href='/lineas', className='w-100 my-2'),
            dbc.Button('Ver 5 ciudades más violentas de Colombia, considerando homicidios (códigos X95)', href='/barras', className='w-100 my-2'),
            dbc.Button('Ver 10 ciudades con menor índice de mortalidad.', href='/circular', className='w-100 my-2'),
            dbc.Button('Ver 10 principales causas de muerte en Colombia', href='/tabla', className='w-100 my-2'),
            dbc.Button('Ver Distribución de muertes según rangos de edad quinquenales (0-4, 5-9, …, 85+ años)', href='/histograma', className='w-100 my-2'),
            dbc.Button('Ver Total de muertes por sexo en cada departamento', href='/barras_apiladas', className='w-100 my-2'),
        ], className='d-flex flex-column align-items-center')
    ])


def create_line_chart(df: pd.DataFrame) -> html.Div:
    """
    Creates a line chart showing total deaths per month.

    Args:
        df (pd.DataFrame): DataFrame containing the death data.

    Returns:
        dcc.Graph: The Plotly line chart.
    """
    fig = px.line(df, x='MES', y='n_muertes', title='Total de Muertes por Mes en Colombia')
    line_chart = dcc.Graph(figure=fig)
    return html.Div([
        line_chart,
        html.Div([
            dbc.Button('Ir a Inicio', href='/', className='w-100 my-2'),
            dbc.Button('Ver Mapa de distribución total de muertes por departamento en Colombia', href='/mapa', className='w-100 my-2'),
            dbc.Button('Ver 5 ciudades más violentas de Colombia, considerando homicidios (códigos X95)', href='/barras', className='w-100 my-2'),
            dbc.Button('Ver 10 ciudades con menor índice de mortalidad.', href='/circular', className='w-100 my-2'),
            dbc.Button('Ver 10 principales causas de muerte en Colombia', href='/tabla', className='w-100 my-2'),
            dbc.Button('Ver Distribución de muertes según rangos de edad quinquenales (0-4, 5-9, …, 85+ años)', href='/histograma', className='w-100 my-2'),
            dbc.Button('Ver Total de muertes por sexo en cada departamento', href='/barras_apiladas', className='w-100 my-2'),
        ], className='d-flex flex-column align-items-center')
    ])


def create_bar_chart(df: pd.DataFrame) -> html.Div:
    """
    Creates a bar chart showing the 5 most violent cities.

    Args:
        df (pd.DataFrame): DataFrame containing the death data.

    Returns:
        dcc.Graph: The Plotly bar chart.
    """
    fig = px.bar(df, x='Ciudad', y='n_muertes', title='Las 5 Ciudades Más Violentas de Colombia (Homicidios X95)')
    bar_chart = dcc.Graph(figure=fig)
    return html.Div([
                bar_chart,
                html.Div([
                    dbc.Button('Ir a Inicio', href='/', className='w-100 my-2'),
                    dbc.Button('Ver Mapa de distribución total de muertes por departamento en Colombia', href='/mapa', className='w-100 my-2'),
                    dbc.Button('Ver Total de muertes por mes en Colombia', href='/lineas', className='w-100 my-2'),
                    dbc.Button('Ver 10 ciudades con menor índice de mortalidad.', href='/circular', className='w-100 my-2'),
                    dbc.Button('Ver 10 principales causas de muerte en Colombia', href='/tabla', className='w-100 my-2'),
                    dbc.Button('Ver Distribución de muertes según rangos de edad quinquenales (0-4, 5-9, …, 85+ años)', href='/histograma', className='w-100 my-2'),
                    dbc.Button('Ver Total de muertes por sexo en cada departamento', href='/barras_apiladas', className='w-100 my-2'),
                ], className='d-flex flex-column align-items-center')
            ])


def create_pie_chart(df: pd.DataFrame) -> html.Div:
    """
    Creates a pie chart showing the 10 cities with the lowest mortality rate.

    Args:
        df (pd.DataFrame): DataFrame containing the death data.

    Returns:
        dcc.Graph: The Plotly pie chart.
    """
    fig = px.pie(df, names='Ciudad', values='n_muertes', title='10 Ciudades con Menor Índice de Mortalidad')

    pie_chart = dcc.Graph(figure=fig)
    return html.Div([
        pie_chart,
        html.Div([
            dbc.Button('Ir a Inicio', href='/', className='w-100 my-2'),
            dbc.Button('Ver Mapa de distribución total de muertes por departamento en Colombia', href='/mapa', className='w-100 my-2'),
            dbc.Button('Ver Total de muertes por mes en Colombia', href='/lineas', className='w-100 my-2'),
            dbc.Button('Ver 5 ciudades más violentas de Colombia, considerando homicidios (códigos X95)', href='/barras', className='w-100 my-2'),
            dbc.Button('Ver 10 principales causas de muerte en Colombia', href='/tabla', className='w-100 my-2'),
            dbc.Button('Ver Distribución de muertes según rangos de edad quinquenales (0-4, 5-9, …, 85+ años)', href='/histograma', className='w-100 my-2'),
            dbc.Button('Ver Total de muertes por sexo en cada departamento', href='/barras_apiladas', className='w-100 my-2'),
        ], className='d-flex flex-column align-items-center')
    ])


def create_table(df: pd.DataFrame) -> html.Div:
    """
    Creates a Plotly table showing the top 10 leading causes of death.

    Args:
        df (pd.DataFrame): DataFrame containing the death data with columns
                           like 'Código', 'Nombre_Causa', and 'Total_Casos'.

    Returns:
        dcc.Graph: A Dash dcc.Graph component containing the Plotly table.
    """
    fig = go.Figure(data=[go.Table(
        header=dict(values=['Código', 'Nombre de la Causa', "Descripción", 'Total de Casos'],
                    fill_color='lightgrey',
                    align='left'),
        cells=dict(values=[df['COD_MUERTE'], df['MANERA_MUERTE'], df['Descripcion_4_caracteres'], df['n_muertes']],
                   fill_color='white',
                   align='left'))
    ])
    table = dcc.Graph(figure=fig)
    return html.Div([
        table,
        html.Div([
            dbc.Button('Ir a Inicio', href='/', className='w-100 my-2'),
            dbc.Button('Ver Mapa de distribución total de muertes por departamento en Colombia', href='/mapa', className='w-100 my-2'),
            dbc.Button('Ver Total de muertes por mes en Colombia', href='/lineas', className='w-100 my-2'),
            dbc.Button('Ver 5 ciudades más violentas de Colombia, considerando homicidios (códigos X95)', href='/barras', className='w-100 my-2'),
            dbc.Button('Ver 10 ciudades con menor índice de mortalidad.', href='/circular', className='w-100 my-2'),
            dbc.Button('Ver Distribución de muertes según rangos de edad quinquenales (0-4, 5-9, …, 85+ años)', href='/histograma', className='w-100 my-2'),
            dbc.Button('Ver Total de muertes por sexo en cada departamento', href='/barras_apiladas', className='w-100 my-2'),
        ], className='d-flex flex-column align-items-center')
    ])


def create_histogram(df: pd.DataFrame) -> html.Div:
    """
    Creates a histogram showing the distribution of deaths by age ranges.

    Args:
        df (pd.DataFrame): DataFrame containing the death data.

    Returns:
        dcc.Graph: The Plotly histogram.
    """
    fig = px.bar(df, x='Grupo_Edad', y='n_muertes', title='Distribución de Muertes por Rangos de Edad')
    histogram = dcc.Graph(figure=fig)
    return html.Div([
        histogram,
        html.Div([
            dbc.Button('Ir a Inicio', href='/', className='w-100 my-2'),
            dbc.Button('Ver Mapa de distribución total de muertes por departamento en Colombia', href='/mapa', className='w-100 my-2'),
            dbc.Button('Ver Total de muertes por mes en Colombia', href='/lineas', className='w-100 my-2'),
            dbc.Button('Ver 5 ciudades más violentas de Colombia, considerando homicidios (códigos X95)', href='/barras', className='w-100 my-2'),
            dbc.Button('Ver 10 principales causas de muerte en Colombia', href='/tabla', className='w-100 my-2'),
            dbc.Button('Ver Distribución de muertes según rangos de edad quinquenales (0-4, 5-9, …, 85+ años)', href='/histograma', className='w-100 my-2'),
            dbc.Button('Ver Total de muertes por sexo en cada departamento', href='/barras_apiladas', className='w-100 my-2'),
        ], className='d-flex flex-column align-items-center')
    ])


def create_stacked_bar_chart(df: pd.DataFrame) -> html.Div:
    """
    Creates a stacked bar chart comparing deaths by sex and department with a horizontal slicer.

    Args:
        df (pd.DataFrame): DataFrame containing the death data with 'DEPARTAMENTO', 'n_muertes', and 'SEXO' columns.

    Returns:
        html.Div: A div containing the Plotly stacked bar chart and a range slider.
    """
    departments = df['DEPARTAMENTO'].unique()
    fig = px.bar(df, x='DEPARTAMENTO', y='n_muertes', color='SEXO',
                 title='Comparación de Muertes por Sexo y Departamento')
    stacked_bar_chart = dcc.Graph(id='stacked-bar-chart', figure=fig)

    range_slider = dcc.RangeSlider(
        id='department-range-slider',
        min=0,
        max=len(departments) - 1,
        step=1,
        value=[0, min(10, len(departments) - 1)],  # Initial range to display
        marks={i: dept for i, dept in enumerate(departments[::max(1, len(departments) // 10)])}, # Add some marks for better understanding
    )

    return html.Div([
                stacked_bar_chart,
                range_slider,
                html.Div([
                    dbc.Button('Ir a Inicio', href='/', className='w-100 my-2'),
                    dbc.Button('Ver Mapa de distribución total de muertes por departamento en Colombia', href='/mapa', className='w-100 my-2'),
                    dbc.Button('Ver Total de muertes por mes en Colombia', href='/lineas', className='w-100 my-2'),
                    dbc.Button('Ver 5 ciudades más violentas de Colombia, considerando homicidios (códigos X95)', href='/barras', className='w-100 my-2'),
                    dbc.Button('Ver 10 principales causas de muerte en Colombia', href='/tabla', className='w-100 my-2'),
                    dbc.Button('Ver Distribución de muertes según rangos de edad quinquenales (0-4, 5-9, …, 85+ años)', href='/histograma', className='w-100 my-2'),
                    dbc.Button('Ver Total de muertes por sexo en cada departamento', href='/barras_apiladas', className='w-100 my-2'),
                ], className='d-flex flex-column align-items-center')
            ])

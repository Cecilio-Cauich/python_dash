import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd 
from dash.dependencies import Input,Output

df = pd.read_csv('suicide-rate.csv', encoding = 'utf-8')
df_suicide_mx = df.pivot_table(index='Year', columns='Entity', values='Suicide mortality rate')
df_suicide_mx = df_suicide_mx['Mexico']

df_completo = pd.read_csv('suicide-rates-by-age-detailed.csv', encoding = 'utf-8')
df_suicide_ages_5_14 = df_completo.pivot_table(index='Year', columns='Entity', values='Deaths - Self-harm - Sex: Both - Age: 5-14 years (Rate)')
df_suicide_ages_5_14 = df_suicide_ages_5_14['Mexico']

df_completo = pd.read_csv('suicide-rates-by-age-detailed.csv', encoding = 'utf-8')
df_suicide_ages_15_49 = df_completo.pivot_table(index='Year', columns='Entity', values='Deaths - Self-harm - Sex: Both - Age: 15-49 years (Rate)')
df_suicide_ages_15_49 = df_suicide_ages_15_49['Mexico']


df_completo = pd.read_csv('suicide-rates-by-age-detailed.csv', encoding = 'utf-8')
df_suicide_ages_50_69 = df_completo.pivot_table(index='Year', columns='Entity', values='Deaths - Self-harm - Sex: Both - Age: 50-69 years (Rate)')
df_suicide_ages_50_69 = df_suicide_ages_50_69['Mexico']

app = dash.Dash(__name__)

fig = px.line(
    data_frame= df_suicide_mx)

fig_514 = px.line(
    data_frame= df_suicide_ages_5_14)

fig_1549 = px.line(
    data_frame= df_suicide_ages_15_49)

fig_5069 = px.line(
    data_frame= df_suicide_ages_50_69)

app.layout = html.Div(children=[
    html.H1(children='Muertes por suicidio en México 1990-2019.',style={'textAlign':'center','color':'#006400'}),

    html.Div(children='''
        Texto indefinido.
    ''',style ={'textAlign':'center','color':'#006400'}),
    
     dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    
    html.Div(children='''
        Muertes dentro del rango de edades de 5 a 14 años!.
    ''',style ={'textAlign':'center','color':'#006400'}),
    
     dcc.Graph(
        id='example-graph_a',
        figure=fig_514
    ),
    
    html.Div(children='''
        Muertes dentro del rango de edades de 15 a 49 años!.
    ''',style ={'textAlign':'center','color':'#006400'}),
    
     dcc.Graph(
        id='example-graph_b',
        figure=fig_1549
    ),
    
    html.Div(children='''
        Muertes dentro del rango de edades de 50 a 69 años!.
    ''',style ={'textAlign':'center','color':'#006400'}),
    
     dcc.Graph(
        id='example-graph_c',
        figure=fig_5069
    ),
])


if __name__ == '__main__':
    app.run_server(debug=False)

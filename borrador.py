# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:46:30 2023

@author: karen
"""
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from pgmpy.inference import VariableElimination
from pgmpy.readwrite import BIFReader
import dash_bootstrap_components as dbc

import plotly.colors as colors
# Obtener la paleta de verdes
greens_palette = colors.sequential.Greens
# Obtener la paleta de azules
blues_palette = colors.sequential.Blues

# Obtener la base de datos
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:proyecto2@proy2database.czhxhldkmqh7.us-east-1.rds.amazonaws.com/icfes')
datos_originales=pd.read_sql('SELECT * FROM icfes_data', engine)
datos_originales.head()

# Read model from BIF file 
#reader = BIFReader("ModeloK2.bif")##poner aqui modelo bif
#modelo = reader.get_model()

# Print model 
#print(modelo)

from pgmpy.estimators import BayesianEstimator
#emv = BayesianEstimator(model=modelo, data=datos)
#modelo.fit(data=datos, estimator = BayesianEstimator)   
#modelo.check_model()

#infer = VariableElimination(modelo)


# Crear la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


#Grafico1

valores1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in datos_originales.index:
    if datos_originales.loc[i, 'fami_estratovivienda'] == "Estrato 1":
        if datos_originales.loc[i, 'desemp_ingles']=='-A':
            valores1[0] = valores1[0]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A1':
            valores1[1] = valores1[1]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A2':
            valores1[2] = valores1[2]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='B1':
            valores1[3] = valores1[3]+1
        else:
            valores1[4] = valores1[4]+1
    elif datos_originales.loc[i, 'fami_estratovivienda'] == "Estrato 2":
        if datos_originales.loc[i, 'desemp_ingles']=='-A':
            valores1[5] = valores1[5]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A1':
            valores1[6] = valores1[6]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A2':
            valores1[7] = valores1[7]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='B1':
            valores1[8] = valores1[8]+1
        else:
            valores1[9] = valores1[9]+1
    elif datos_originales.loc[i, 'fami_estratovivienda'] == "Estrato 3":
        if datos_originales.loc[i, 'desemp_ingles']=='-A':
            valores1[10] = valores1[10]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A1':
            valores1[11] = valores1[11]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A2':
            valores1[12] = valores1[12]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='B1':
            valores1[13] = valores1[13]+1
        else:
            valores1[14] = valores1[14]+1
    elif datos_originales.loc[i, 'fami_estratovivienda'] == "Estrato 4":
        if datos_originales.loc[i, 'desemp_ingles']=='-A':
            valores1[15] = valores1[15]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A1':
            valores1[16] = valores1[16]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A2':
            valores1[17] = valores1[17]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='B1':
            valores1[18] = valores1[18]+1
        else:
            valores1[19] = valores1[19]+1
    elif datos_originales.loc[i, 'fami_estratovivienda'] == "Estrato 5":
        if datos_originales.loc[i, 'desemp_ingles']=='-A':
            valores1[20] = valores1[20]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A1':
            valores1[21] = valores1[21]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A2':
            valores1[22] = valores1[22]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='B1':
            valores1[23] = valores1[23]+1
        else:
            valores1[24] = valores1[24]+1
    elif datos_originales.loc[i, 'fami_estratovivienda'] == "Estrato 6":
        if datos_originales.loc[i, 'desemp_ingles']=='-A':
            valores1[25] = valores1[25]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A1':
            valores1[26] = valores1[26]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A2':
            valores1[27] = valores1[27]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='B1':
            valores1[28] = valores1[28]+1
        else:
            valores1[29] = valores1[29]+1
    else:
        if datos_originales.loc[i, 'desemp_ingles']=='-A':
            valores1[30] = valores1[30]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A1':
            valores1[31] = valores1[31]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='A2':
            valores1[32] = valores1[32]+1
        elif datos_originales.loc[i, 'desemp_ingles']=='B1':
            valores1[33] = valores1[33]+1
        else:
            valores1[34] = valores1[34]+1
porcentajes1 = [round(valores1[0]/(valores1[0]+valores1[1]+valores1[2]+valores1[3]+valores1[4]),3),round(valores1[1]/(valores1[0]+valores1[1]+valores1[2]+valores1[3]+valores1[4]),3), round(valores1[2]/(valores1[0]+valores1[1]+valores1[2]+valores1[3]+valores1[4]),3), round(valores1[3]/(valores1[0]+valores1[1]+valores1[2]+valores1[3]+valores1[4]),3) , round(valores1[4]/(valores1[0]+valores1[1]+valores1[2]+valores1[3]+valores1[4]),3), 
                round(valores1[5]/(valores1[5]+valores1[6]+valores1[7]+valores1[8]+valores1[9]),3),round(valores1[6]/(valores1[5]+valores1[6]+valores1[7]+valores1[8]+valores1[9]),3), round(valores1[7]/(valores1[5]+valores1[6]+valores1[7]+valores1[8]+valores1[9]),3), round(valores1[8]/(valores1[5]+valores1[6]+valores1[7]+valores1[8]+valores1[9]),3) , round(valores1[9]/(valores1[5]+valores1[6]+valores1[7]+valores1[8]+valores1[9]),3), 
                round(valores1[10]/(valores1[10]+valores1[11]+valores1[12]+valores1[13]+valores1[14]),3),round(valores1[11]/(valores1[10]+valores1[11]+valores1[12]+valores1[13]+valores1[14]),3), round(valores1[12]/(valores1[10]+valores1[11]+valores1[12]+valores1[13]+valores1[14]),3), round(valores1[13]/(valores1[10]+valores1[11]+valores1[12]+valores1[13]+valores1[14]),3) , round(valores1[14]/(valores1[10]+valores1[11]+valores1[12]+valores1[13]+valores1[14]),3), 
                round(valores1[15]/(valores1[15]+valores1[16]+valores1[17]+valores1[18]+valores1[19]),3),round(valores1[16]/(valores1[15]+valores1[16]+valores1[17]+valores1[18]+valores1[19]),3), round(valores1[17]/(valores1[15]+valores1[16]+valores1[17]+valores1[18]+valores1[19]),3), round(valores1[18]/(valores1[15]+valores1[16]+valores1[17]+valores1[18]+valores1[19]),3) , round(valores1[19]/(valores1[15]+valores1[16]+valores1[17]+valores1[18]+valores1[19]),3),
                round(valores1[20]/(valores1[20]+valores1[21]+valores1[22]+valores1[23]+valores1[24]),3),round(valores1[21]/(valores1[20]+valores1[21]+valores1[22]+valores1[23]+valores1[24]),3), round(valores1[22]/(valores1[20]+valores1[21]+valores1[22]+valores1[23]+valores1[24]),3), round(valores1[23]/(valores1[20]+valores1[21]+valores1[22]+valores1[23]+valores1[24]),3) , round(valores1[24]/(valores1[20]+valores1[21]+valores1[22]+valores1[23]+valores1[24]),3), 
                round(valores1[25]/(valores1[25]+valores1[26]+valores1[27]+valores1[28]+valores1[29]),3),round(valores1[26]/(valores1[25]+valores1[26]+valores1[27]+valores1[28]+valores1[29]),3), round(valores1[27]/(valores1[25]+valores1[26]+valores1[27]+valores1[28]+valores1[29]),3), round(valores1[28]/(valores1[25]+valores1[26]+valores1[27]+valores1[28]+valores1[29]),3) , round(valores1[29]/(valores1[25]+valores1[26]+valores1[27]+valores1[28]+valores1[29]),3),
                round(valores1[30]/(valores1[30]+valores1[31]+valores1[32]+valores1[33]+valores1[34]),3),round(valores1[31]/(valores1[30]+valores1[31]+valores1[32]+valores1[33]+valores1[34]),3), round(valores1[32]/(valores1[30]+valores1[31]+valores1[32]+valores1[33]+valores1[34]),3), round(valores1[33]/(valores1[30]+valores1[31]+valores1[32]+valores1[33]+valores1[34]),3) , round(valores1[34]/(valores1[30]+valores1[31]+valores1[32]+valores1[33]+valores1[34]),3) 
                ]
porcentajes1

df1 = pd.DataFrame({
    "Desempeño en Ingles": ["-A", "A1", "A2","B1", "B+", "-A", "A1", "A2","B1", "B+","-A", "A1", "A2","B1", "B+","-A", "A1", "A2","B1", "B+","-A", "A1", "A2","B1", "B+","-A", "A1", "A2","B1", "B+","-A", "A1", "A2","B1", "B+"],
    "Porcentaje": porcentajes1,
    "Estrato de Vivienda": ["Estrato 1", "Estrato 1", "Estrato 1", "Estrato 1","Estrato 1","Estrato 2", "Estrato 2", "Estrato 2", "Estrato 2", "Estrato 2","Estrato 3", "Estrato 3", "Estrato 3", "Estrato 3", "Estrato 3","Estrato 4", "Estrato 4", "Estrato 4", "Estrato 4", "Estrato 4","Estrato 5", "Estrato 5", "Estrato 5", "Estrato 5", "Estrato 5","Estrato 6", "Estrato 6", "Estrato 6", "Estrato 6", "Estrato 6","Sin Estrato", "Sin Estrato", "Sin Estrato", "Sin Estrato", "Sin Estrato"]
})

fig1=px.bar(df1, x="Estrato de Vivienda", y="Porcentaje", color="Desempeño en Ingles", color_discrete_sequence=blues_palette[2:7])
fig1.update_layout(legend=dict(yanchor="bottom", y=1, xanchor="left", x=0.01))
fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)")  



## Grafico 2

valores2 = [0,0,0,0,0,0,0,0,0,0]

for i in datos_originales.index:
    if datos_originales.loc[i, 'cole_naturaleza'] == "NO OFICIAL":
        if datos_originales.loc[i, 'punt_global']<200:
            valores2[0] = valores2[0]+1
        elif datos_originales.loc[i, 'punt_global']>=200 and datos_originales.loc[i, 'punt_global']<250:
            valores2[1] = valores2[1]+1
        elif datos_originales.loc[i, 'punt_global']>=250 and datos_originales.loc[i, 'punt_global']<300:
            valores2[2] = valores2[2]+1
        elif datos_originales.loc[i, 'punt_global']>=300 and datos_originales.loc[i, 'punt_global']<350:
            valores2[3] = valores2[3]+1
        else:
            valores2[4] = valores2[4]+1
    else:
        if datos_originales.loc[i, 'punt_global']<200:
            valores2[5] = valores2[5]+1
        elif datos_originales.loc[i, 'punt_global']>=200 and datos_originales.loc[i, 'punt_global']<250:
            valores2[6] = valores2[6]+1
        elif datos_originales.loc[i, 'punt_global']>=250 and datos_originales.loc[i, 'punt_global']<300:
            valores2[7] = valores2[7]+1
        elif datos_originales.loc[i, 'punt_global']>=300 and datos_originales.loc[i, 'punt_global']<350:
            valores2[8] = valores2[8]+1
        else:
            valores2[9] = valores2[9]+1

porcentajes2 = [round(valores2[0]/(valores2[0]+valores2[5]),3), round(valores2[1]/(valores2[1]+valores2[6]),3), round(valores2[2]/(valores2[2]+valores2[7]),3), round(valores2[3]/(valores2[3]+valores2[8]),3), round(valores2[4]/(valores2[4]+valores2[9]),3),round(valores2[5]/(valores2[0]+valores2[5]),3), round(valores2[6]/(valores2[1]+valores2[6]),3), round(valores2[7]/(valores2[2]+valores2[7]),3), round(valores2[8]/(valores2[3]+valores2[8]),3),round(valores2[9]/(valores2[4]+valores2[9]),3)]   
porcentajes2

df2 = pd.DataFrame({
    "Puntaje global": ["Menos de 200", "Entre 200 y 250", "Entre 251 y 300","Entre 301 y 350", "Más de 351", "Menos de 200", "Entre 200 y 250", "Entre 251 y 300","Entre 301 y 350", "Más de 351"],
    "Proporción de personas": porcentajes2,
    "Naturaleza del Colegio": ["NO OFICIAL", "NO OFICIAL", "NO OFICIAL", "NO OFICIAL","NO OFICIAL","OFICIAL", "OFICIAL", "OFICIAL", "OFICIAL","OFICIAL"]
})

fig2=px.bar(df2, x='Puntaje global', y='Proporción de personas', color='Naturaleza del Colegio', barmode='stack',  color_discrete_sequence=[greens_palette[4], blues_palette[4]])
fig2.update_layout(legend=dict(yanchor="bottom", y=1, xanchor="left", x=0.01))
fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)")  



# Gráfico 3
valores3 = [0,0,0,0,0,0,0,0,0,0]
for i in datos_originales.index:
    if datos_originales.loc[i, 'estu_genero'] == "F":
        if datos_originales.loc[i, 'punt_global']<200:
            valores3[0] = valores3[0]+1
        elif datos_originales.loc[i, 'punt_global']>=200 and datos_originales.loc[i, 'punt_global']<250:
            valores3[1] = valores3[1]+1
        elif datos_originales.loc[i, 'punt_global']>=250 and datos_originales.loc[i, 'punt_global']<300:
            valores3[2] = valores3[2]+1
        elif datos_originales.loc[i, 'punt_global']>=300 and datos_originales.loc[i, 'punt_global']<350:
            valores3[3] = valores3[3]+1
        else:
            valores3[4] = valores3[4]+1
    else:
        if datos_originales.loc[i, 'punt_global']<200:
            valores3[5] = valores3[5]+1
        elif datos_originales.loc[i, 'punt_global']>=200 and datos_originales.loc[i, 'punt_global']<250:
            valores3[6] = valores3[6]+1
        elif datos_originales.loc[i, 'punt_global']>=250 and datos_originales.loc[i, 'punt_global']<300:
            valores3[7] = valores3[7]+1
        elif datos_originales.loc[i, 'punt_global']>=300 and datos_originales.loc[i, 'punt_global']<350:
            valores3[8] = valores3[8]+1
        else:
            valores3[9] = valores3[9]+1

porcentajes3 = [round(valores3[0]/(valores3[0]+valores3[5]),3), round(valores3[1]/(valores3[1]+valores3[6]),3), round(valores3[2]/(valores3[2]+valores3[7]),3), round(valores3[3]/(valores3[3]+valores3[8]),3), round(valores3[4]/(valores3[4]+valores3[9]),3),round(valores3[5]/(valores3[0]+valores3[5]),3), round(valores3[6]/(valores3[1]+valores3[6]),3), round(valores3[7]/(valores3[2]+valores3[7]),3), round(valores3[8]/(valores3[3]+valores3[8]),3),round(valores3[9]/(valores3[4]+valores3[9]),3)]   
porcentajes3

df3 = pd.DataFrame({
    "Puntaje global": ["Menos de 200", "Entre 200 y 250", "Entre 251 y 300","Entre 301 y 350", "Más de 351", "Menos de 200", "Entre 200 y 250", "Entre 251 y 300","Entre 301 y 350", "Más de 351"],
    "Proporción de personas": porcentajes3,
    "Género": ["Femenino", "Femenino", "Femenino", "Femenino","Femenino","Masculino", "Masculino", "Masculino", "Masculino","Masculino"]
})

fig3=px.bar(df3, x='Puntaje global', y='Proporción de personas', color='Género', barmode='stack',  color_discrete_sequence=[ blues_palette[4],greens_palette[4]])
fig3.update_layout(legend=dict(yanchor="bottom", y=1, xanchor="left", x=0.01))
fig3.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)") 

#Crear gráficos
tab1_content = dbc.Card(
    dbc.CardBody([
    html.H2('¿Qué dicen los datos?'),
    html.P(children='Queremos proporcionarte información relevante sobre los resultados de la prueba Saber 11 - Icfes, basada en estadísticas del conjunto de datos disponible en el repositorio de Datos Abiertos. Esperamos que esta información sea útil para ti.' ),
    html.Div([
  
    html.Div([
        dcc.Graph(id='grafico1', figure = fig3)],
        style={'width': '33%', 'display': 'inline-block'}),
        
    html.Div([
        dcc.Graph(id='grafico2', figure = fig1)],
        style={'width': '33%', 'display': 'inline-block'}),
        
    html.Div([
        dcc.Graph(id='grafico3', figure = fig2)],
        style={'width': '33%', 'display': 'inline-block'})
    ], style={'display': 'flex'})
    
],  style={'margin': '30px'}))

tab2_content=dbc.Card(
    dbc.CardBody([
    html.P(children='Aquí te brindamos una herramienta que puedes utilizar para predecir el puntaje global de la prueba saber 11 y con ello, apoyarte en la toma de decisiones' ),
    html.Br(),
    
    html.H6("Ingresa el valor de la información que tengas disponible:"),
    
    html.Div([
        html.Div(['Edad:',
                dcc.Dropdown(
                    id='input_age',
                    options=[
                        {'label': 'Entre 25 y 40 años', 'value': 1},
                        {'label': 'Entre 41 y 50 años', 'value': 2},
                        {'label': 'Entre 51 y 60 años', 'value': 3},
                        {'label': 'Mayor a 60 años', 'value': 4}
            ],
            value='-1'
        )],  style={'width': '50%', 'marginRight': '50px'}),   
        html.Div(['Sexo:',
        dcc.Dropdown(
            id='input_sex',
            options=[
                {'label': 'Mujer', 'value': 0},
                {'label': 'Hombre', 'value': 1}
            ],
            value='-1'
        )], style={'width': '50%'})],  style={'display': 'flex', "width": "100%"}),
    
    html.Div([
            html.Div(['Nivel de colesterol:',
            dcc.Dropdown(
                id='input_chol',
                options=[
                    {'label': 'Menor o igual a 200', 'value': 1},
                    {'label': 'Entre 201 y 240', 'value': 2},
                    {'label': 'Mayor o igual a 240', 'value': 3},
                ],
                value='-1'
            )],  style={'width': '50%','marginRight': '50px'}),
            
            html.Div(['Nivel de presión arterial en reposo:',
            dcc.Dropdown(
                id='input_trestbps',
                options=[
                    {'label': 'Menor o igual a 120', 'value': 1},
                    {'label': 'Entre 121 y 139', 'value': 2},
                    {'label': 'Entre 140 y 159', 'value': 3},
                    {'label': 'Entre 160 y 179', 'value': 4},
                    {'label': 'Mayor o igual a 159', 'value': 5},
                ],
                value='-1'
            )], style={'width': '50%'})],  style={'display': 'flex', "width": "100%"}),
    
    html.Div([
            html.Div(['En caso de presentar talasemia, indica el tipo:',
            dcc.Dropdown(
                id='input_thal',
                options=[
                    {'label': 'Normal', 'value': 3},
                    {'label': 'Defecto fijo', 'value': 6},
                    {'label': 'Defecto reversible', 'value': 7},
                ],
                value='-1'
            )],  style={'width': '50%', 'marginRight': '50px'}),
            
            html.Div(['El nivel de azucar en la sangre en ayunas es mayor a 120 mg/dl:',
            dcc.Dropdown(
                id='input_fbs',
                options=[
                    {'label': 'Sí', 'value': 1},
                    {'label': 'No', 'value': 0},
                   
                ],
                value='-1'
            )], style={'width': '50%'})],  style={'display': 'flex', "width": "100%"}),
    html.Br(),
    html.H6("A continuación te presentamos la probabilidad de tener o no una enfermedad cardiaca:"),
    html.Br(),
    html.Div([
        html.Div(
        dcc.Graph(id='grafico'),
         style={'width': '60%'}),
        html.Div([
            html.Br(),
            html.Div(id='recomendación')],
            style={'textAlign': 'left','marginTop':'150px','width': '30%'})], style={'display': 'flex','width': '100%'}, className='row'),
    ],  style={'margin': '30px'}
))
# Definir las pestañas
tabs = dbc.Tabs([
    dbc.Tab(label='Datos de interés', tab_id='tab-1', children=[tab1_content]),
    dbc.Tab(label='Obten aquí tu probabilidad', tab_id='tab-2', children=[tab2_content]),
], id='tabs', active_tab='tab-1', className="nav nav-tabs")


# Definir el diseño de la aplicación
app.layout = dbc.CardBody([
       html.Div([
       html.Img(src='https://upload.wikimedia.org/wikipedia/commons/a/a2/Icfes_logo_2022.png',
                 style={'height': '70%', 'width': 'auto','max-width': '100%'}),
        html.H1(children='Resultados Examen Saber 11°-ICFES',
                style={'textAlign': 'center', 'marginTop': '25px', "width": "80%", 'fontSize': '3vw'}),
        html.Img(src='https://educacion.uniandes.edu.co/sites/default/files/Uniandes.png',
                 style={'height': '60%', 'width': 'auto', 'max-width': '100%', 'marginTop': '20px'})
    ], style={'display': 'flex', 'height': '120px', "width": "100%"}),
    html.Br(),
    tabs
    
 ], style={'margin': '30px'})


@app.callback(
    [Output(component_id='grafico', component_property='figure'),
     Output(component_id='recomendación', component_property='children')]
     ,
    [
     Input(component_id='input_age', component_property='value'),
     Input(component_id='input_sex', component_property='value'),
     Input(component_id='input_chol', component_property='value'),
     Input(component_id='input_trestbps', component_property='value'),
     Input(component_id='input_thal', component_property='value'),
     Input(component_id='input_fbs', component_property='value')
     ])
def update_pie_chart(input_age, input_sex, input_chol, input_trestbps, input_thal, input_fbs):
    
    valores = ['age','sex','chol','trestbps','thal','fbs']
    respuesta = [input_age, input_sex, input_chol, input_trestbps, input_thal, input_fbs]
      
    aux={}
    for i in range(0, 6):
        if respuesta[i] != '-1': 
            aux[valores[i]]= respuesta[i]
        
    if len(aux)==0:
        posterior_p = infer.query(["num"], evidence={'age':2,'sex':1,'chol':2,'trestbps':1,'thal':3,'fbs':1})

    else:
        posterior_p = infer.query(["num"], evidence=aux)
    
    num_states = modelo.get_cpds("num").state_names["num"]
    
    # valores para el gráfico de torta
    labels = ['Ausencia de enfermedad cardiaca', 'Presencia de enfermedad cardiaca']
    values = [posterior_p.values[num_states.index(0)], posterior_p.values[num_states.index(1)]]
    
    
    # Crear el objeto Pie de Plotly
    #if isinstance(values[0], (int, float))
        
    import plotly.graph_objs as go
    figura = go.Figure(go.Pie(labels=labels, 
                          values=values,
                          textfont={'size': 20},
                          #hole=0.5,
                          hoverinfo='label+percent',
                          marker=dict(colors=["greenyellow", "red"],
                                      line=dict(color='#000000', width=1)),
                          #textposition='outside',
                          pull = [0, 0.2]
                         ), layout=(go.Layout( margin=dict(l=100, r=10, t=10, b=10))                     
                        )
)
    figura.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)")  
    if values[0] > 0.8 :
            recomendación = 'Como la probabilidad de que no tengas una enfermedad cardiaca es alta ('+'{:.0%}'.format(values[0]) +'), te sugerimos continuar con tus chequeos de control, teniendo en cuenta que no es urgente que consultes un médico especialista.'
    elif values[0] > 0.5:
            recomendación = 'A pesar de que la probabilidad de que tengas una enfermedad cardiaca no es tan alta ('+ '{:.0%}'.format(values[1]) +'), te sugerimos consultar a un médico especialista y así decartar que tengas una enfermedad cardiaca.'
    elif values[0] > 0.25:
            recomendación = 'De acuerdo con tus características, es probable que tengas una enfermedad cardiaca ('+'{:.0%}'.format(values[1]) +'), te sugerimos consultar a un médico especialista en el menor tiempo posible.'
    elif values[0]<=0.25: 
            recomendación = 'De acuerdo con tus características, la probabilidad de tener una enfermedad cardiaca es muy alta (' +'{:.0%}'.format(values[1]) + '), deberias consultar a un médico especialista de inmediato para confirmar esto y si es así, iniciar un tratamiento.'
    else: 
        recomendación = "Lamentamos informarle que no tenemos evidencia para el caso presentado, por lo que no podemos estimarlo."
       
    return figura, recomendación

if __name__ == '__main__':
    app.run_server(debug=True)
    
    

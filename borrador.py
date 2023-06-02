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

##Obtener base discretizada
datos=pd.read_sql('SELECT * FROM datos_discretizados',engine)
datos.head()

# Read model from BIF file 
reader = BIFReader("ModeloICFES.bif")
modelo = reader.get_model()


from pgmpy.estimators import BayesianEstimator
emv = BayesianEstimator(model=modelo, data=datos)
modelo.fit(data=datos, estimator = BayesianEstimator)   
modelo.check_model()

infer = VariableElimination(modelo)


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
    html.P(children='A continuación proporcionamos información relevante sobre los resultados de la prueba Saber 11° en la ciudad de Bogotá dentro de los años 2019 a 2022, basada en estadísticas del conjunto de datos disponible en el repositorio de Datos Abiertos.' ),
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
    html.P(children='Esta es una herramienta que se puede utilizar para predecir el puntaje global de la prueba saber 11° de un estudiante de Bogotá dada las características de su entorno' ),
    html.Br(),
    
    html.H6("Ingrese el valor de la información que tenga disponible:"),
    
    html.Div([
        html.Div(['Género de estudiante:',
                dcc.Dropdown(
                    id='input_genero',
                    options=[
                        {'label': 'Mujer', 'value': 1},
                        {'label': 'Hombre', 'value': 0}
            ],
            value='-1'
        )],  style={'width': '33%', 'marginRight': '50px'}),   
        html.Div(['Naturaleza del Colegio:',
        dcc.Dropdown(
            id='input_natu_colegio',
            options=[
                {'label': 'Oficial', 'value': 1},
                {'label': 'No Oficial', 'value': 0}
            ],
            value='-1'
        )], style={'width': '33%','marginRight': '50px'}), 
        html.Div(['Jornada:',
        dcc.Dropdown(
            id='input_jornada',
            options=[
                {'label': 'Mañana', 'value': 1},
                {'label': 'Tarde', 'value': 2},
                {'label': 'Completa', 'value': 3},
                {'label': 'Noche', 'value': 4},
                {'label': 'Única', 'value': 5},
                {'label': 'Sabatina', 'value': 0}
            ],
            value='-1'
        )], style={'width': '33%'})],
        
        style={'display': 'flex', "width": "100%","margin-bottom": "30px"}),
    
    html.Div([
            html.Div(['Desempeño en inglés:',
            dcc.Dropdown(
                id='input_ingles',
                options=[
                    {'label': 'A-', 'value': 1},
                    {'label': 'A1', 'value': 2},
                    {'label': 'A2', 'value': 3},
                    {'label': 'B1', 'value': 4},
                    {'label': 'B+', 'value': 5}
                ],
                value='-1'
            )],  style={'width': '33%','marginRight': '50px'}),
            
            html.Div(['Estrato de la vivienda :',
            dcc.Dropdown(
                id='input_estrato',
                options=[
                    {'label': '1', 'value': 1},
                    {'label': '2', 'value': 2},
                    {'label': '3', 'value': 3},
                    {'label': '4', 'value': 4},
                    {'label': '5', 'value': 5},
                    {'label': '6', 'value': 6},
                    {'label': 'Sin estrato', 'value': 0}
                ],
                value='-1'
            )], style={'width': '33%','marginRight': '50px'}), 
            html.Div(['¿En la familia tienen internet?',
            dcc.Dropdown(
                id='input_internet',
                options=[
                    {'label': 'Sí', 'value': 1},
                    {'label': 'No', 'value': 0}
                ],
                value='-1'
            )], style={'width': '33%'})],
            
            style={'display': 'flex', "width": "100%","margin-bottom": "30px"}),
        
    html.Div([
            html.Div(['¿En la familia tienen computador?',
            dcc.Dropdown(
                id='input_compu',
                options=[
                    {'label': 'Sí', 'value': 1},
                    {'label': 'No', 'value': 0}
                ],
                value='-1'
            )],  style={'width': '33%','marginRight': '50px'}),
            
            html.Div(['¿En la familia tienen lavadora?',
            dcc.Dropdown(
                id='input_lavadora',
                options=[
                    {'label': 'Sí', 'value': 1},
                    {'label': 'No', 'value': 0}
                ],
                value='-1'
            )], style={'width': '33%','marginRight': '50px'}), 
            html.Div(['¿En la familia tienen automóvil?',
            dcc.Dropdown(
                id='input_auto',
                options=[
                    {'label': 'Sí', 'value': 1},
                    {'label': 'No', 'value': 0}
                ],
                value='-1'
            )], style={'width': '33%'})],
            
            style={'display': 'flex', "width": "100%","margin-bottom": "30px"}),
    html.Div([
            html.Div(['¿Cuántas personas hay en su hogar?',
            dcc.Dropdown(
                id='input_personas_hogar',
                options=[
                    {'label': '1 a 2', 'value': 1},
                    {'label': '3 a 4', 'value': 2},
                    {'label': '5 a 6', 'value': 3},
                    {'label': '7 a 8', 'value': 4},
                    {'label': '9 o más', 'value': 5}
                ],
                value='-1'
            )],  style={'width': '33%','marginRight': '50px'}),
            
            html.Div(['Nivel de educación de la madre:',
            dcc.Dropdown(
                id='input_madre',
                options=[
                    {'label': 'Primaria (Completa o incompleta)', 'value': 1},
                    {'label': 'Secundaria/Bachillerato (Completa o incompleta)', 'value': 2},
                    {'label': 'Técnica o tecnologica (Completa o incompleta)', 'value': 3},
                    {'label': 'Profesional (Completa o incompleta)', 'value': 4},
                    {'label': 'Posgrado', 'value': 5},
                    {'label': 'No aplica o no sabe', 'value': 0}
                ],
                value='-1'
            )], style={'width': '33%','marginRight': '50px'}), 
            html.Div(['Nivel de educación del padre:',
            dcc.Dropdown(
                id='input_padre',
                options=[
                    {'label': 'Primaria (Completa o incompleta)', 'value': 1},
                    {'label': 'Secundaria/Bachillerato (Completa o incompleta)', 'value': 2},
                    {'label': 'Técnica o tecnologica (Completa o incompleta)', 'value': 3},
                    {'label': 'Profesional (Completa o incompleta)', 'value': 4},
                    {'label': 'Posgrado', 'value': 5},
                    {'label': 'No aplica o no sabe', 'value': 0}
                ],
                value='-1'
            )], style={'width': '33%'})],
            
            style={'display': 'flex', "width": "100%","margin-bottom": "30px"}),
    html.Div([
            html.Div(['Número de cuartos en su hogar:',
            dcc.Dropdown(
                id='input_cuartos_hogar',
                options=[
                    {'label': '1', 'value': 1},
                    {'label': '2', 'value': 2},
                    {'label': '3', 'value': 3},
                    {'label': '4', 'value': 4},
                    {'label': '5', 'value': 5},
                    {'label': '6 o mas', 'value': 6}
                ],
                value='-1'
            )],  style={'width': '33%','marginRight': '50px'})],
            style={'display': 'flex', "width": "100%"}),   
    html.Br(),
    html.H6("A continuación presentamos la probabilidad de obtener los siguientes puntajes en el Examen Saber 11°:"),
    html.Br(),
    html.Div([
        html.Div(
        dcc.Graph(id='figura'),
         style={'width': '60%'}),
        html.Div([
            html.Br(),
            html.Div(id='recomendación')],
            style={'textAlign': 'left','marginTop':'150px','width': '30%', 'fontSize': '20px'})], style={'display': 'flex','width': '100%'}, className='row'),
    ],  style={'margin': '30px'}
))
# Definir las pestañas
tabs = dbc.Tabs([
    dbc.Tab(label='Datos de interés', tab_id='tab-1', children=[tab1_content]),
    dbc.Tab(label='Pronóstico', tab_id='tab-2', children=[tab2_content]),
], id='tabs', active_tab='tab-1', className="nav nav-tabs")


# Definir el diseño de la aplicación
app.layout = dbc.CardBody([
       html.Div([
       html.Img(src='https://upload.wikimedia.org/wikipedia/commons/a/a2/Icfes_logo_2022.png',
                 style={'height': '70%', 'width': 'auto','max-width': '100%'}),
        html.H1(children='Análisis de resultados Examen Saber 11°',
                style={'textAlign': 'center', 'marginTop': '25px', "width": "80%", 'fontSize': '3vw'}),
        html.Img(src='https://educacion.uniandes.edu.co/sites/default/files/Uniandes.png',
                 style={'height': '60%', 'width': 'auto', 'max-width': '100%', 'marginTop': '20px'})
    ], style={'display': 'flex', 'height': '120px', "width": "100%"}),
    html.Br(),
    tabs
    
 ], style={'margin': '30px'})


@app.callback(
    [Output(component_id='figura', component_property='figure'),
     Output(component_id='recomendación', component_property='children')]
     ,
    [
     Input(component_id='input_genero', component_property='value'),
     Input(component_id='input_jornada', component_property='value'),
     Input(component_id='input_natu_colegio', component_property='value'),
     Input(component_id='input_ingles', component_property='value'),
     Input(component_id='input_estrato', component_property='value'),
     Input(component_id='input_internet', component_property='value'),
     Input(component_id='input_compu', component_property='value'),
     Input(component_id='input_lavadora', component_property='value'),
     Input(component_id='input_auto', component_property='value'),
     Input(component_id='input_personas_hogar', component_property='value'),
     Input(component_id='input_madre', component_property='value'),
     Input(component_id='input_padre', component_property='value'),
     Input(component_id='input_cuartos_hogar', component_property='value')
     ])

def update_pie_chart(input_genero, input_jornada, input_natu_colegio, input_ingles, input_estrato, input_internet,input_compu,input_lavadora,input_auto,input_personas_hogar,input_madre,input_padre,input_cuartos_hogar):
    
    valores = ['estu_genero','cole_jornada','cole_naturaleza','desemp_ingles','fami_estratovivienda','fami_tieneinternet', 'fami_tienecomputador','fami_tienelavadora','fami_tieneautomovil', 'fami_personashogar','fami_educacionmadre','fami_educacionpadre','fami_cuartoshogar']
    respuesta = [input_genero, input_jornada, input_natu_colegio, input_ingles, input_estrato, input_internet,input_compu,input_lavadora,input_auto,input_personas_hogar,input_madre,input_padre,input_cuartos_hogar]
      
    aux={}
    for i in range(0, 6):
        if respuesta[i] != '-1': 
            aux[valores[i]]= respuesta[i]
        
    if len(aux)==0:
        posterior_p = infer.query(["punt_global"], evidence={'estu_genero':1,'cole_jornada':2,'cole_naturaleza':1,'desemp_ingles':3,'fami_estratovivienda':4,'fami_tieneinternet':1, 'fami_tienecomputador':0,'fami_tienelavadora':0,'fami_tieneautomovil':0, 'fami_personashogar':2,'fami_educacionmadre':2,'fami_educacionpadre':2,'fami_cuartoshogar':3})

    else:
        posterior_p = infer.query(["punt_global"], evidence=aux)
    
    punt_states = modelo.get_cpds("punt_global").state_names["punt_global"]
    
    # valores para el gráfico de torta
    labels = ['menor a 200', 'entre 201 y 250', 'entre 251 y 300', 'entre 301 y 350', 'mayor a 351']
    values = [posterior_p.values[punt_states.index(1)], posterior_p.values[punt_states.index(2)], posterior_p.values[punt_states.index(3)], posterior_p.values[punt_states.index(4)], posterior_p.values[punt_states.index(5)]]
    
    max_value = values[0]  # Asignamos el primer valor de la lista como el máximo inicialmente
    max_label = labels[0]  # Asignamos el primer label como el correspondiente al valor máximo inicialmente

    for i in range(len(values)):
        if values[i] > max_value:
            max_value = values[i]
            max_label = labels[i]
    
    # Crear el objeto Pie de Plotly
    #if isinstance(values[0], (int, float))
    import plotly.graph_objs as go
    
    highlight_color = greens_palette[4] # Color para resaltar la porción del valor máximo
    colors_list = [highlight_color if label == max_label else blues_palette[i] for i, label in enumerate(labels)]

    figura = go.Figure(go.Pie(labels=labels, 
                          values=values,
                          textfont={'size': 20},
                          marker=dict(
                                colors=colors_list # Utilizamos la paleta de colores Greens
                        ),pull=[0.1 if label == max_label else 0 for label in labels]# Resaltamos la porción del valor máximo
                          ), layout=(go.Layout( margin=dict(l=100, r=10, t=10, b=10))                     
                        )   
    )
    figura.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)")  
    
    
    
    recomendación = 'De acuerdo a las características del evaluado, se estima que el puntaje global del Examen Saber 11° sea '+max_label
           
    return figura, recomendación

if __name__ == '__main__':
    app.run_server(debug=True)
    
    

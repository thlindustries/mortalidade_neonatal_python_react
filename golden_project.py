import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from dash.dependencies import Input, Output

import pandas as pd

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

#listas globais
lista_dias_vividos=[]
lista_total=[]

#df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')


df_ac = pd.read_csv('Dados-AC.csv')
##------------------ACRE---------------------
df_morteNeonatal_AC=df_ac[:]
df_morteNeonatal_AC['year_death'] = df_morteNeonatal_AC['year_death'].astype('Int64')
df_morteNeonatal_AC=df_morteNeonatal_AC[df_morteNeonatal_AC["morte_menor_28d"] == 1]

df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_sg_sexo == 'M','n_sg_sexo'] = 1
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_sg_sexo == 'F','n_sg_sexo'] = 2
df_morteNeonatal_AC['n_sg_sexo']=df_morteNeonatal_AC['n_sg_sexo'].astype(int)

df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_raca_cor_mae == 1,'n_tp_raca_cor_mae'] = 'maes_brancas'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_raca_cor_mae == 2,'n_tp_raca_cor_mae'] = 'maes_negras'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_raca_cor_mae == 3,'n_tp_raca_cor_mae'] = 'maes_asiaticas'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_raca_cor_mae == 4,'n_tp_raca_cor_mae'] = 'maes_pardas'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_raca_cor_mae == 5,'n_tp_raca_cor_mae'] = 'maes_indigenas'

df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_sg_sexo == 1,'n_sg_sexo'] = 'Homem'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_sg_sexo == 2,'n_sg_sexo'] = 'Mulher'

df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_ocorrencia == 1,'n_tp_ocorrencia'] = 'hospital'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_ocorrencia == 2,'n_tp_ocorrencia'] = 'other_health_establishment'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_ocorrencia == 3,'n_tp_ocorrencia'] = 'residence'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_ocorrencia == 4,'n_tp_ocorrencia'] = 'other'
##------------------ACRE---------------------
##----------------- Indicadores -------------
#available_indicators = df['Indicator Name'].unique()

available_indicators_peso = df_morteNeonatal_AC['n_nu_peso'].unique()
available_indicators_cor_mae = df_morteNeonatal_AC['n_tp_raca_cor_mae'].unique()
available_indicators_tipo_de_parto = df_morteNeonatal_AC['n_tp_ocorrencia'].unique()
##----------------- Indicadores -------------
app.layout = html.Div([
    html.Div([
        dcc.Tabs(id="tabs", value='tab-1', children=[
            dcc.Tab(label='1º Visualização:', value='tab-1', children=[
                html.H1(["Mortalidade neonatal por peso, cor da mãe, ano e local de nascimento"],style={'text-align':'center'}),
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id='xaxis-column2',
                            options=[{'label': i, 'value': i} for i in available_indicators_cor_mae],
                            value='maes_pardas',
                            style={'background-color':'#e6e6e6'}
                        ),
                        dcc.RadioItems(
                            id='xaxis-type2',
                            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                            value='Linear',
                            labelStyle={'display': 'inline-block'}
                        )
                    ],style={'width': '48%', 'display': 'inline-block'}),
                    html.Div([
                        dcc.Dropdown(
                            id='yaxis-column2',
                            options=[{'label': i, 'value': i} for i in available_indicators_tipo_de_parto],
                            value='hospital',
                            style={'background-color':'#e6e6e6'}
                        ),
                        dcc.RadioItems(
                            id='yaxis-type2',
                            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                            value='Linear',
                            labelStyle={'display': 'inline-block'}
                        )
                    ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
                ],style={'height':'100%','background-color':'#d6d4d4'}),
                dcc.Graph(id='indicator-graphic2'),
                html.Br(), html.Br(),
                dcc.Slider(
                    id='year--slider2',
                    min=df_morteNeonatal_AC['year_death'].min(),
                    max=df_morteNeonatal_AC['year_death'].max(),
                    value=df_morteNeonatal_AC['year_death'].max(),
                    marks={str(year): str(year) for year in df_morteNeonatal_AC['year_death'].unique()},
                    step=None
                )
            ],style={'background-color':'#8f8f8f'}),
            dcc.Tab(label='2º Visualização:', value='tab-2', children=[
                html.Div([
                    html.H1(["Mortalidade neonatal e média de dias vividos por faixa de peso"],style={'text-align':'center'}),
                    html.Div([
                        html.Br(),
                        dcc.Graph(id='indicator-graphic3'),
                    ],style={'width': '30%', 'float': 'right', 'display': 'inline-block'}),
                    html.Div([
                        html.Br(), html.Br(),
                        dcc.Graph(id='indicator-graphic4'),
                    ],style={"width": "70%" }),
                    dcc.Slider(
                        id='year--slider3',
                        min=df_morteNeonatal_AC['year_death'].min(),
                        max=df_morteNeonatal_AC['year_death'].max(),
                        value=df_morteNeonatal_AC['year_death'].max(),
                        marks={str(year): str(year) for year in df_morteNeonatal_AC['year_death'].unique()},
                        step=None
                    ),
                ],style={'height':'100%','background-color':'#d6d4d4'}),               
            ],style={'background-color':'#8f8f8f'}),
            dcc.Tab(label='3º Visualização:', value='tab-3', children=[
                html.H1(["Mortalidade neonatal relacionada com tipo do parto e idade da mãe"],style={'text-align':'center'}),
                dcc.Graph(id='indicator-graphic5'),
                html.Br(), html.Br(),
                dcc.Slider(
                    id='year--slider5',
                    min=df_morteNeonatal_AC['year_death'].min(),
                    max=df_morteNeonatal_AC['year_death'].max(),
                    value=df_morteNeonatal_AC['year_death'].max(),
                    marks={str(year): str(year) for year in df_morteNeonatal_AC['year_death'].unique()},
                    step=None
                ),
            ],style={'background-color':'#8f8f8f'}),
        ]),
        html.Div(id='tabs-content'), 
    ],style={'background-color':'#d6d4d4'})
])
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
        ])
    elif tab == 'tab-2':
        return html.Div([
        ])
    elif tab == 'tab-3':
        return html.Div([
        ])

@app.callback(
    Output('indicator-graphic2', 'figure'),
    [Input('xaxis-column2', 'value'),
     Input('yaxis-column2', 'value'),
     Input('xaxis-type2', 'value'),
     Input('yaxis-type2', 'value'),
     Input('year--slider2', 'value')])
def update_graph2(xaxis_column_name, yaxis_column_name,
                 xaxis_type2, yaxis_type2,
                 year_value2):
    aux=df_morteNeonatal_AC[:]

    menor_ano=aux['year_death'].min()

    dataframe_original=aux[aux['year_death']==2006]
    if year_value2>menor_ano:
        for i in range(menor_ano+1,year_value2+1):
            #print(i)
            dataframe_auxiliar=aux[aux['year_death']==i]
            dataframe_original=dataframe_original.append(dataframe_auxiliar)
    #aux=aux[aux['year_death']==year_value2]
    dataframe_original=dataframe_original[dataframe_original['n_tp_raca_cor_mae']==xaxis_column_name]
    dataframe_original=dataframe_original[dataframe_original['n_tp_ocorrencia']==yaxis_column_name]

    aux_homem_final = dataframe_original[dataframe_original['n_sg_sexo']=='Homem']
    aux_mulher_final = dataframe_original[dataframe_original['n_sg_sexo']=='Mulher']

    lista_pesos=list(available_indicators_peso)
    #lista_idade_mae=list(available_indicators_idade_mae)

    return {
        'data': [
            dict(
                x=lista_pesos,
                y=aux_homem_final.groupby('n_nu_peso')['n_nu_peso'].count().values,
                name='Mortes de meninos',
                text=aux_homem_final['n_sg_sexo'],
                #z=lista_idade_mae,
                type='histogram',
                marker={
                   'size': 20,
                   'color':'rgb(0, 179, 255)'
                }
                #type='pie'
                #type='scatter3d'
            ),
            dict(
                x=lista_pesos,
                y=aux_mulher_final.groupby('n_nu_peso')['n_nu_peso'].count().values,
                name='Mortes de meninas',
                #z=lista_idade_mae,
                text=aux_mulher_final['n_sg_sexo'],
                type='histogram',
                marker={
                    'size': 20,
                    'color':'rgb(255, 153, 229)',
                },
                
                # type='scatter3d'
            )
        ],
        'layout': dict(
            plot_bgcolor="#d6d4d4",
            paper_bgcolor="#d6d4d4",
            xaxis={
                'title': 'Peso da criança',
                'type': 'linear' if xaxis_type2 == 'Linear' else 'log'
            },
            yaxis={
                'title': 'Número de óbitos',
                'type': 'linear' if yaxis_type2 == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }
@app.callback(
    Output('indicator-graphic5', 'figure'),
    [Input('year--slider5', 'value')])

def update_graph98(year_value5):
    aux=df_morteNeonatal_AC[:]
    menor_ano=aux['year_death'].min()

    dataframe_original=aux[aux['year_death']==2006]
    if year_value5>menor_ano:
        for i in range(menor_ano+1,year_value5+1):
            #print(i)
            dataframe_auxiliar=aux[aux['year_death']==i]
            dataframe_original=dataframe_original.append(dataframe_auxiliar)
    #aux=aux[aux['year_death']==year_value2]


    parto_normal_aux=dataframe_original[dataframe_original['n_tp_parto']==1]    
    parto_cesarea_aux=dataframe_original[dataframe_original['n_tp_parto']==2]
    #
    #1    8-14
    #2    15-19
    #3    20-24
    #4    25-29
    #5    30-34
    #6    35-39
    #7    40-44
    #8    45-49
    #9    50+

    # parto_normal_aux.loc[parto_normal_aux.n_ct_idade == 1,'n_ct_idade'] = '8-14'
    # parto_normal_aux.loc[parto_normal_aux.n_ct_idade == 2,'n_ct_idade'] = '15-19'
    # parto_normal_aux.loc[parto_normal_aux.n_ct_idade == 3,'n_ct_idade'] = '20-24'
    # parto_normal_aux.loc[parto_normal_aux.n_ct_idade == 4,'n_ct_idade'] = '25-29'
    # parto_normal_aux.loc[parto_normal_aux.n_ct_idade == 5,'n_ct_idade'] = '30-34'
    # parto_normal_aux.loc[parto_normal_aux.n_ct_idade == 6,'n_ct_idade'] = '35-39'
    # parto_normal_aux.loc[parto_normal_aux.n_ct_idade == 7,'n_ct_idade'] = '40-44'
    # parto_normal_aux.loc[parto_normal_aux.n_ct_idade == 8,'n_ct_idade'] = '45-49'
    # parto_normal_aux.loc[parto_normal_aux.n_ct_idade == 9,'n_ct_idade'] = '50+' 

    lista_idades_mae=['8-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50+'] 




    available_indicators_idade_mae_normal = parto_normal_aux['n_ct_idade'].unique()
    available_indicators_idade_mae_cesarea = parto_cesarea_aux['n_ct_idade'].unique()
    # aux_homem_final = dataframe_original[dataframe_original['n_sg_sexo']=='Homem']
    # aux_mulher_final = dataframe_original[dataframe_original['n_sg_sexo']=='Mulher']

    #lista_pesos=list(available_indicators_peso)
    lista_idade_mae_1=list(available_indicators_idade_mae_normal)
    lista_idade_mae_2=list(available_indicators_idade_mae_cesarea)
    
    lista_obitos_normal=list(parto_normal_aux.groupby('n_ct_idade')['n_ct_idade'].count().values)
    lista_obitos_cesaria=list(parto_normal_aux.groupby('n_ct_idade')['n_ct_idade'].count().values)
    
    #print(lista_obitos_normal)
    #print(lista_obitos_cesaria)

    return {
        'data': [
            dict(
                x=lista_idade_mae_1,
                y=lista_obitos_normal,
                name='Parto Normal',
                text=parto_normal_aux['n_tp_parto'],
                #z=lista_idade_mae,
                type='bar',
                marker={
                   'size': 20,
                   'color':'rgb(255, 255, 138)'
                }
                #type='pie'
                #type='scatter3d'
            ),
            dict(
                x=lista_idade_mae_2,
                y=lista_obitos_cesaria,
                name='Parto Cesaria',
                #z=lista_idade_mae,
                text=parto_cesarea_aux['n_tp_parto'],
                type='bar',
                marker={
                    'size': 20,
                    'color':'rgb(48, 105, 13)'
                }
                # type='scatter3d'
            )
        ],
        'layout': dict(
            plot_bgcolor="#d6d4d4",
            paper_bgcolor="#d6d4d4",
            xaxis={
                'title': 'Idade da mãe',
                'type': 'linear' 
            },
            yaxis={
                'title': 'Número de óbitos',
                'type': 'linear'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }
@app.callback(
    Output('indicator-graphic3', 'figure'),
    [Input('year--slider3', 'value')])
def update_graph3(year_value3):
    aux=df_morteNeonatal_AC[:]

    menor_ano=aux['year_death'].min()
    dataframe_original=aux[aux['year_death']==2006]
    if year_value3>menor_ano:
       for i in range(menor_ano+1,year_value3+1):
           dataframe_auxiliar=aux[aux['year_death']==i]
           dataframe_original=dataframe_original.append(dataframe_auxiliar)

    aux_homem_final = dataframe_original[dataframe_original['n_sg_sexo']=='Homem']
    aux_mulher_final = dataframe_original[dataframe_original['n_sg_sexo']=='Mulher']

    return {
        'data': [
            dict(
                values=[aux_homem_final.groupby('n_sg_sexo')['n_sg_sexo'].count().values[0],aux_mulher_final.groupby('n_sg_sexo')['n_sg_sexo'].count().values[0]],
                labels=['Mortes de meninos','Mortes de meninas'],
                type='pie',
                hole=.4,
                marker={
                    'colors':['rgb(0, 179, 255)','rgb(255, 153, 229)']
                },
            )
        ],
        'layout': dict(
            paper_bgcolor="#d6d4d4",
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest',
            annotations=[
                dict(
                    text='Mortes',x=0.5,y=0.5,font_sizer=20,showarrow=False
                )
            ]
        )
    }

@app.callback(
    Output('indicator-graphic4', 'figure'),
    [Input('year--slider3', 'value')])
def update_graph4(year_value3):
    # if (len(lista_total)>4):
    #     lista_total=[]
    ##Criando dataframes auxiliares
    df_teste = df_ac[:]
    df_morteNeonatal=df_teste[:]
    
    #Listas auxiliares
    lista_db=[]
    lista_dd=[]
    lista_mb=[]
    lista_md=[]
    lista_yb=[]
    lista_yd=[]
    
    
    #Filtrando o csv e convertendo informações
    df_morteNeonatal['year_death'] = df_morteNeonatal['year_death'].astype('Int64')
    df_morteNeonatal=df_morteNeonatal[df_morteNeonatal["morte_menor_28d"] == 1]

    df_morteNeonatal.loc[df_morteNeonatal.n_sg_sexo == 'M','n_sg_sexo'] = 1
    df_morteNeonatal.loc[df_morteNeonatal.n_sg_sexo == 'F','n_sg_sexo'] = 2
    df_morteNeonatal['n_sg_sexo']=df_morteNeonatal['n_sg_sexo'].astype(int)
    menor_ano=df_morteNeonatal['year_death'].min()

    ##Data frame ordenado
    teste_order=df_morteNeonatal.sort_values(by=['n_nu_peso'])
    aux=teste_order[:]

    

    #Criando listas para realização de calculos
    lista_dia_nascimento_ordenada=[]
    lista_dia_morte_ordenada=[]
    lista_mes_nascimento_ordenada=[]
    lista_mes_morte_ordenada=[]
    lista_ano_nascimento_ordenada=[]
    lista_ano_morte_ordenada=[]

    lista_auxx=[]
    #Ocorrencia momentanea que é inserida na lista de ocorrencias    
    ocorrencias=0
    lista_ocorrencias=[]
    
    #Agrupando csv's por ano
    menor_ano=aux['year_death'].min()
    dataframe_original=aux[aux['year_death']==2006]
    if year_value3>menor_ano:
       for i in range(menor_ano+1,year_value3+1):
           dataframe_auxiliar=aux[aux['year_death']==i]
           dataframe_original=dataframe_original.append(dataframe_auxiliar)

    #print(str(year_value3))
    testando=list(dataframe_original['day_birth'].values)
    #print(str(len(testando)))
    #print("+++Dias nascidos para 2006 ^++")

    ##--------------------------------------------------------------------------------------------------------------

    teste_order=dataframe_original.sort_values(by=['n_nu_peso'])
    elemetos_linha_matriz=0
    #Pegando os pesos do dataframe
    lista_ordenada=list(teste_order['n_nu_peso'].values)

    if year_value3==2016:
        #Inserindo pesos lixos pra completar 280 e ter 10 partes inteiras de 28 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        elemetos_linha_matriz=28
    if year_value3==2015:
        #Inserindo pesos lixos pra completar 250 e ter 10 partes inteiras de 25 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)
        elemetos_linha_matriz=25
    if year_value3==2014:
        #Inserindo pesos lixos pra completar 210 e ter 10 partes inteiras de 21 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)
        elemetos_linha_matriz=21
    if year_value3==2013:
        #Inserindo pesos lixos pra completar 160 e ter 10 partes inteiras de 16 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)        
        lista_ordenada.insert(0,6)        
        lista_ordenada.insert(0,7)        
        lista_ordenada.insert(0,8)        
        lista_ordenada.insert(0,9)        
        lista_ordenada.insert(0,10) 
        elemetos_linha_matriz=16       
    if year_value3==2012:
        #Inserindo pesos lixos pra completar 110 e ter 10 partes inteiras de 11 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)        
        lista_ordenada.insert(0,6)        
        lista_ordenada.insert(0,7)        
        lista_ordenada.insert(0,8)          
        lista_ordenada.insert(0,9)          
        lista_ordenada.insert(0,10)          
        lista_ordenada.insert(0,11)         
        lista_ordenada.insert(0,12) 
        elemetos_linha_matriz=11    
    if year_value3==2011:
        #Inserindo pesos lixos pra completar 90 e ter 10 partes inteiras de 9 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5) 
        lista_ordenada.insert(0,6) 
        lista_ordenada.insert(0,7) 
        lista_ordenada.insert(0,8) 
        elemetos_linha_matriz=9       
    if year_value3==2010:
        #Inserindo pesos lixos pra completar 80 e ter 10 partes inteiras de 8 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4) 
        elemetos_linha_matriz=8    
    if year_value3==2009:
        #Inserindo pesos lixos pra completar 70 e ter 10 partes inteiras de 7 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)
        elemetos_linha_matriz=7
    if year_value3==2008:
        #Inserindo pesos lixos pra completar 60 e ter 10 partes inteiras de 6 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)
        lista_ordenada.insert(0,6)
        lista_ordenada.insert(0,7)
        lista_ordenada.insert(0,8)   
        elemetos_linha_matriz=6             
    if year_value3==2007:
        #Inserindo pesos lixos pra completar 40 e ter 10 partes inteiras de 4 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)        
        lista_ordenada.insert(0,6)        
        lista_ordenada.insert(0,7)        
        lista_ordenada.insert(0,8)        
        lista_ordenada.insert(0,9)        
        lista_ordenada.insert(0,10)        
        lista_ordenada.insert(0,11)        
        lista_ordenada.insert(0,12)
        elemetos_linha_matriz=4 
    if year_value3==2006:
        #Inserindo pesos lixos pra completar 30 e ter 10 partes inteiras de 3 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)        
        lista_ordenada.insert(0,6)        
        lista_ordenada.insert(0,7)        
        lista_ordenada.insert(0,8)        
        lista_ordenada.insert(0,9)        
        lista_ordenada.insert(0,10)        
        lista_ordenada.insert(0,11)         
        lista_ordenada.insert(0,12)
        elemetos_linha_matriz=3
        #print(str(len(lista_ordenada)))
        #print("+++Tamanho lista ordenada 2006 ^++")
        
    #Removendo elementos repetidos da lista
    i = 0
    while i < len(lista_ordenada):
        count = lista_ordenada.count(lista_ordenada[i]) 
        for j in range(0, count-1):
            lista_ordenada.remove(lista_ordenada[i])

        i = i+1
    #print(str(len(lista_ordenada)))
    #print("+++Tamanho lista ordenada sem repetidos 2006 ^++")
    #print(len(lista_ordenada))   
    #Criando matriz para agrupamento dos pesos //Nem queira entender...
    matriz_pesos=np.zeros((10,elemetos_linha_matriz))
    aux=0
    cont = 0
    aux2=elemetos_linha_matriz
    aux3=1

    for y in range(0,10):
        l_teste=[]
        for j in range(aux,aux2):
            #print("Elemento adicionado = "+str(lista_ordenada[j]))
            #print("posicao da lista = "+str(j))
            #print("cont "+str(cont))
            #print("Aux = "+str(aux))
            aux=j
            l_teste.append(lista_ordenada[j])
            
        for tamanho in range(0,len(l_teste)):
            matriz_pesos[cont][tamanho]=int(l_teste[tamanho])
        l_teste=[]

        j=aux+1
        aux=aux+1
        cont=cont+1
        aux3=aux3+1
        aux2=aux3*elemetos_linha_matriz

    #print(str(matriz_pesos[:][:]))
    #print("elm--->"+str(elemetos_linha_matriz))
        
    #Criando listas auxiliares para tirar a média de dias vividos por agrupamento de pesos
    for i in range(0,len(matriz_pesos)):
        #teste_order=dataframe_original.sort_values(by=['n_nu_peso'])
        for j in range(0,elemetos_linha_matriz):
            aux=teste_order[teste_order['n_nu_peso']==matriz_pesos[i][j]]

            valores_a_inserir_day_birth=aux['day_birth'].values
            #print("db "+str(j)+""+str(i)+"----> "+str(valores_a_inserir_day_birth))

            valores_a_inserir_day_death=aux['day_death'].values
            #print("dd "+str(j)+""+str(i)+"----> "+str(valores_a_inserir_day_death))

            valores_a_inserir_month_birth=aux['month_birth'].values
            #print("mb "+str(j)+""+str(i)+"----> "+str(valores_a_inserir_month_birth))

            valores_a_inserir_month_death=aux['month_death'].values
            #print("md "+str(j)+""+str(i)+"----> "+str(valores_a_inserir_month_death))

            valores_a_inserir_year_birth=aux['year_birth'].values
            #print("yb "+str(j)+""+str(i)+"----> "+str(valores_a_inserir_year_birth))

            valores_a_inserir_year_death=aux['year_death'].values
            #print("yd "+str(j)+""+str(i)+"----> "+str(valores_a_inserir_year_death))


            #print(str(len(valores_a_inserir_day_birth)))
            for x in range(0,len(valores_a_inserir_day_birth)):
                lista_dia_nascimento_ordenada.append(valores_a_inserir_day_birth[x])
                #print("elemento X---> "+str(valores_a_inserir_day_birth[x]))
                #print("ldb---> "+str(lista_dia_nascimento_ordenada))

                lista_dia_morte_ordenada.append(valores_a_inserir_day_death[x])
                #print("ldd---> "+str(lista_dia_morte_ordenada))
                
                lista_mes_nascimento_ordenada.append(valores_a_inserir_month_birth[x])
                #print("lmb---> "+str(lista_mes_nascimento_ordenada))

                lista_mes_morte_ordenada.append(valores_a_inserir_month_death[x])
                #print("lmd---> "+str(lista_mes_morte_ordenada))
                
                lista_ano_nascimento_ordenada.append(valores_a_inserir_year_birth[x])
                #print("lyb---> "+str(lista_ano_nascimento_ordenada))

                lista_ano_morte_ordenada.append(valores_a_inserir_year_death[x])
                #print("lyd---> "+str(lista_ano_morte_ordenada))
                
            ocorrencias = ocorrencias + teste_order[teste_order['n_nu_peso']==matriz_pesos[i][j]].count().values[0]
        if (len(valores_a_inserir_day_birth)!=0):
            lista_ocorrencias.append(ocorrencias)
            lista_dia_nascimento_ordenada.append("___")
            lista_dia_morte_ordenada.append("___")
            lista_mes_nascimento_ordenada.append("___")
            lista_mes_morte_ordenada.append("___")
            lista_ano_nascimento_ordenada.append("___")
            lista_ano_morte_ordenada.append("___")
        else:
            lista_auxx.append(0)
            lista_auxx.append(0)
            lista_auxx.append(0)
            lista_auxx.append("___")
        ocorrencias= 0

    for cc in range(0,len(lista_auxx)):
        lista_dia_nascimento_ordenada.append(lista_auxx[cc])
        lista_dia_morte_ordenada.append(lista_auxx[cc])
        lista_mes_nascimento_ordenada.append(lista_auxx[cc])
        lista_mes_morte_ordenada.append(lista_auxx[cc])
        lista_ano_nascimento_ordenada.append(lista_auxx[cc])
        lista_ano_morte_ordenada.append(lista_auxx[cc])


    #Preenchendo listas auxiliares para calcular a média de dias vividos por faixa de peso
    for i in range(0,len(lista_dia_nascimento_ordenada)):
        if(lista_dia_nascimento_ordenada[i]!='___'):
            
            lista_db.append(lista_dia_nascimento_ordenada[i])
            lista_dd.append(lista_dia_morte_ordenada[i])
            lista_mb.append(lista_mes_nascimento_ordenada[i])
            lista_md.append(lista_mes_morte_ordenada[i])
            lista_yb.append(lista_ano_nascimento_ordenada[i])
            lista_yd.append(lista_ano_morte_ordenada[i])
            #print(str(lista_dia_nascimento_ordenada[i])+"---> "+str(i+1))
        else:
            i=i+1            
        #____________Tudo certo até aqui__________________________            
            aux=teste_order[:]
            #print("-=-=-=-=-=-=-=>>"+str(len(lista_db)))
            dias_vividos_v2(lista_db,lista_mb,lista_yb,lista_dd,lista_md,lista_yd)
            lista_db=[]
            lista_dd=[]
            lista_mb=[]
            lista_md=[]
            lista_yb=[]
            lista_yd=[]
    lista_pesos_grafico=[]
    for i in range(0,len(matriz_pesos)):
        lista_pesos_grafico.append(str(int(matriz_pesos[i].min()))+"-"+str(int(matriz_pesos[i].max())))
    
    # print("___________________________________________________________________________________________________________-")

    #print(lista_ocorrencias) #Ocorrencias por faixa de peso
    #print(lista_pesos_grafico) #Faixas de peso
    #print(lista_total) #Média de dias vividos por faixa de peso
    


##---------------------------------------------------------------------------------------------------------------------------

    lista_pesos=list(available_indicators_peso)
    
    #final_data = pd.DataFrame(data=[lista_ocorrencias, lista_pesos_grafico, lista_total], columns=['Óbitos', 'Peso', 'Média de Dias Vividos'])

    return {
        'data': [
            dict(
                x = lista_ocorrencias,#Ocorrencias por faixa de peso
                y = lista_pesos_grafico,#Faixas de peso
                z=lista_total, #Média de dias vividos por faixa de peso
                # x=final_data['Óbitos'],
                # y=final_data['Peso'],
                # z=final_data['Média de Dias Vividos'],
                type='scatter3d',
                surfacecolor='rgb(0, 255, 30)',
                mode='markers', 
                marker={'size': 8, 'color': lista_total, 'colorscale': 'Rainbow', "showscale": True,
                        "colorbar": {"thickness": 15, "len": 0.5, "x": 0.8, "y": 0.6, },'symbol':201 },
                
                # camera= dict(
                # up=dict(x=0,y=0,z=1),
                # center=dict(x=0,y=0,z=0),
                # eye=dict(x=0,y=0,z=0),
                #),
            )
        ],
        'layout': dict(
            paper_bgcolor="#d6d4d4",
            height=600,
            scene={
                "xaxis":{'title':'Número de óbitos'},
                "yaxis":{'title':'Peso'},
                "zaxis":{'title':'Média de dias vividos'},
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        ),
        
    }
def dias_vividos_v2(lista_db,lista_mb,lista_yb,lista_dd,lista_md,lista_yd):
    #Todas as listas estão chegando perfeitamente certas, !TESTADO

    aux=0
    aux2=0
    lista_dias_vividos.append("___________")
    
    #print("Tamanho lista--->"+str(len(lista_db)))    
    for i in range(0,len(lista_db)):
        aux=(lista_yd[i]-lista_yb[i])
        aux=(aux*12)+lista_md[i]-lista_mb[i]
        aux=aux*31
        aux=aux+lista_dd[i]
        aux=aux-lista_db[i]
        aux2=aux2+aux
    aux2=aux2/int(len(lista_db))
    #print("Aux2--->"+str(aux2))
    if round(aux2) not in lista_total:
        lista_total.append(int(round(aux2)))
    
if __name__ == '__main__':
    app.run_server(host='localhost',port='8050',debug=True)
# # #     app.run_server(debug=True)
# if __name__ == "__main__":
#     app.run_server(debug=True)
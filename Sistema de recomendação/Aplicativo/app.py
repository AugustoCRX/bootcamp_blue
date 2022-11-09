import pandas as pd
import plotly.graph_objects as go
from threading import Timer
import webbrowser
import keyboard

import re
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

from dash import Dash, dcc, html, Input, Output

import pickle

from contextlib import contextmanager
import sys, os

def processamento(tokens):
        stop_words = stopwords.words('english')
        lemmatizer = WordNetLemmatizer()
        stemmer = PorterStemmer()
        
        token_processado = []
        for token in tokens:
                token = token.lower()
                token = lemmatizer.lemmatize(token)
                
                if token not in stop_words:
                        token = stemmer.stem(token)
                        token_processado.append(token)
        
        return token_processado

def graphics_data(category):
        direct = os.listdir(f'table_data/{category}/graph')
        categories_filter = {}
        names_f = [re.split('[_|.]', i)[1] for i in direct]
        for i,j in zip(direct, names_f):
                if j != 'nlp':
                        categories_filter[j] = pd.read_csv(rf'table_data/{category}/graph/{i}')
                        try:
                                categories_filter[j].drop('Unnamed: 0', axis = 1, inplace = True)
                        except:
                                continue
                else:
                        frame = pd.read_csv(rf'table_data/{category}/graph/{i}')
                        name_mean = frame.groupby(['name_rank']).mean().reset_index().drop(['description_rank'], axis = 1)
                        name_mean['name_rank'] += 1
                        description_mean = frame.groupby(['description_rank']).mean().reset_index().drop(['name_rank'], axis = 1)
                        categories_filter[j] = [name_mean,description_mean]
        return categories_filter

def flatten_list(_2d_list):
        flat_list = []
        # Iterate through the outer list
        for element in _2d_list:
                if type(element) is list:
                # If the element is of type list, iterate through the sublist
                        for item in element:
                                flat_list.append(item)
                else:
                        flat_list.append(element)
        return flat_list

#função responsável por construir os gráficos de NLP
def plot_graph(cat, table_column, dictonary):
        fig = go.Figure()
        #adição dos traços
        fig.add_trace(
        go.Scatter
        (
        y = dictonary[cat][table_column].iloc[:,1].values,
        x = dictonary[cat][table_column].iloc[:,0].values,
        marker_color = '#52b788',
        )
        )

        fig.add_annotation(dict(xref='paper',yref='paper', x=-0.07, y=1,
                        xanchor='right', yanchor='top',
                        text='Média de preço',
                        font=dict(family='Arial',
                                size=22,
                                color = "#52b788"),
                        showarrow=False,
                        textangle=90
                        ))
        if table_column == 0:
                #nome do eixo x
                fig.add_annotation(dict(xref='paper', yref='paper', x=-0.03, y=-0.08,
                                xanchor='left', yanchor='top',
                                text='Número de palavras chave do nome',
                                font=dict(family='Arial',
                                        size=22,
                                        color = "#52b788"),
                                showarrow=False
                                )) 
        if table_column == 1:
                #nome do eixo x
                fig.add_annotation(dict(xref='paper', yref='paper', x=-0.03, y=-0.08,
                                xanchor='left', yanchor='top',
                                text='Número de palavras chave da descrição',
                                font=dict(family='Arial',
                                        size=22,
                                        color = "#52b788"),
                                showarrow=False
                                )) 

        fig.update_layout(
                margin=dict(
                l=80,
                r=30,
                b=80,
                t=30,
                pad=5
                ),
                width=600,
                height=400,
                paper_bgcolor = 'rgb(10,10,10)', # cor de fundo do papel do gráfico
                plot_bgcolor = 'rgb(10,10,10)', # cor de fundo do gráfico
                yaxis = dict(tickfont=dict(color="#52b788")),
                xaxis = dict(tickfont=dict(color="#52b788"))

        )

        #configuração dos eixos
        fig.update_xaxes(showgrid=False, zerolinecolor = 'rgb(10,10,10)')
        fig.update_yaxes(showgrid=False, zerolinecolor = 'rgb(10,10,10)')
        return fig

def brand(category):
                lista = pd.read_csv(f'table_data/{category}/brands.csv')
                brands = lista['brands']
                brands = [x for x in brands if pd.isnull(x) == False]
                basics_brand = lista['basics_brand']
                basics_brand = [x for x in basics_brand if pd.isnull(x) == False]
                popular_brand = lista['popular_brand']
                popular_brand = [x for x in popular_brand if pd.isnull(x) == False]
                upper_pop_brand = lista['upper_pop_brand']
                upper_pop_brand = [x for x in upper_pop_brand if pd.isnull(x) == False]
                intermediary_brand = lista['intermediary_brand']
                intermediary_brand = [x for x in intermediary_brand if pd.isnull(x) == False]
                marca = input("Digite marca: ").strip().lower()
                concatenacao_marca = 'brands_filter_'
                if marca in brands:
                        concatenacao_marca += marca
                        return marca, concatenacao_marca
                elif marca in basics_brand:
                        concatenacao_marca += 'basics_brand'
                        return marca, concatenacao_marca
                elif marca in popular_brand:
                        concatenacao_marca += 'popular_brand'
                        return marca, concatenacao_marca
                elif marca in upper_pop_brand:
                        concatenacao_marca += 'upper_pop_brand'
                        return marca, concatenacao_marca
                elif marca in intermediary_brand:
                        concatenacao_marca += 'intermediary_brand'
                        return marca, concatenacao_marca
                else:
                        print('Marca não identificada')
                classificacao = int(input('Classifique sua marca entre 1 e 5, onde 1 marca basica e 5 marca luxuosa'))
                if classificacao == 1:
                        concatenacao_marca += 'basics_brand'
                        return marca, concatenacao_marca
                elif classificacao == 2:
                        concatenacao_marca += 'popular_brand'
                        return marca, concatenacao_marca
                elif classificacao == 3:
                        concatenacao_marca += 'upper_pop_brand'
                        return marca, concatenacao_marca
                elif classificacao == 4:
                        concatenacao_marca += 'intermediary_brand'
                        return marca, concatenacao_marca
                else:
                        concatenacao_marca += 'luxury_brand'
                        return marca, concatenacao_marca

#função para esconder o output do dash
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

def recomendation():
        name_cliente = str(input('Insira seu nome: ')).title()
        name_classificator = {
        'excelent': [1,2],
        'median': [3,4],
        }

        description_classificator = {
        'bad': [0,1,2,3],
        'median': [4,5,6,7]
        }

        condition_classificator = {
        '1': 'excelent',
        '2': 'good',
        '3': 'median',
        '4': 'bad',
        '5': 'worst'
        }

        shipping_classificator ={
        '0': 'buyer',
        '1': 'saller'
        }

        #inicio nome do produto
        product_name = str(input('Insira o nome do produto: '))
        #primeira categoria
        main_data_dict = dict(list([[i , [pd.read_csv(f'table_data/{i}/columns.csv').drop(['Unnamed: 0'], axis = 1), open(f'table_data/{i}/subcategories.txt', 'r').read()]] for i in os.listdir('table_data')]))
        print('''Categorias: ''')

        for i in os.listdir('table_data'):
                print('\t',i.title()) 

        category = input('Digite a Categoria: ').strip().title()

        if category in [i.title() for i in main_data_dict.keys()]:
                category_data = main_data_dict[category.lower()]

        else:
                raise ValueError('Valor não encontrado. Encerrando sistema')
        #fim primeira categoria
        #tratamento nome produto
        product_name_filtered = []

        tokens = processamento(word_tokenize(product_name))
        product_name_filtered.append(tokens)
        product_name_filtered = flatten_list(product_name_filtered)
        categories_filter = graphics_data(category.lower())
        for name in product_name_filtered:
                if name not in categories_filter['names']['Word'].values:
                        product_name_filtered.remove(name)
        score_name = len(product_name_filtered)

        for classif in name_classificator:
                if score_name not in name_classificator[classif]:
                        if score_name == 0:
                                score_name = 'bad'
                        elif classif == list(name_classificator.keys())[-1]:
                                score_name = 'bad'
                        else:
                                continue
                else:
                        score_name = classif
        fig_name = plot_graph('nlp', 0, categories_filter) 

        #o dicionário está divido na seguinte lógica
        #chave (nome da categoria): [tabela em csv dos inputs do sistema de recomendação, subcategorias]
        #inicio do coletor de subcategoria
        concat_subcat = 'sub_category_name_'
        print('Selecione uma subcategoria\n')
        print(print(category_data[1]))
        sub_category = input('Digite a Subcategoria: ').strip().title()
        concat_subcat += sub_category
        subcategory = sub_category.title()
        #inicio do coletor de marcas
        brand_name, concat_brand_name = brand(category)
        #coleta do frete
        def rodar_modelo_other(df):
                model = open(f'table_data/{category}/model','rb')
                lm_new = pickle.load(model)
                model.close()
                value = lm_new.predict(df).round(2)
                return value
        new_data = category_data[0]
        new_data[concat_subcat] = 1
        new_data[concat_brand_name] = 1
        print(''' Frete
        0 - comprador
        1 - vendedor''')
        shipping = input('Digite o número conforme legenda para quem será responsavel pelo custeio do frete: ')
        if category not in  ['Other','Beauty','Home','Electronics']:
                concat_shipping = 'shipping_'
                concat_shipping += shipping
                new_data[concat_shipping] = 1
        else:
                new_data['shipping'] = shipping                
        condition = input("'Digite condição do item entre 1 e 5, onde 1 - Excelente e 5 - Péssimo: '")
        if category in ['Women','Kids']:
                concat_condition = 'item_condition_id_'
                concat_condition += condition
                new_data[concat_condition] = 1
        else:
                new_data['item_condition_id'] = condition
        price = rodar_modelo_other(new_data)
        input_user = input('Deseja adicionar uma descrição ao produto? Digite 1 para adicionar uma descrição, caso não queira, digite qualquer coisa ')

        if input_user == '1':
                product_description = str(input('Insira a descrição do produto: '))
                product_description_filtered = []
                
                sinopse = re.sub(r'[^\w\s]','', product_description)
                tokens = processamento(word_tokenize(product_description))
                product_description_filtered.append(tokens)
                product_description_filtered = flatten_list(product_description_filtered)

                for name in product_description_filtered:
                        if name not in categories_filter['names']['Word'].values:
                                product_description_filtered.remove(name)
                score_description = len(product_description_filtered)

                for classif in description_classificator:
                        if score_description in description_classificator[classif]:
                                score_description = classif
                        else:
                                score_description = 'bad'
                fig_description = plot_graph('nlp', 1, categories_filter) 
                #fim descrição
                app = Dash(__name__)
                app.layout = html.Div(children = [
                html.Div(
                        className = 'app-header',
                        children = [
                                html.H1(f'Olá, {name_cliente}!', className = "app-header--title", style = {'display': 'inline-block'}),
                                html.Img(src = '/assets/image.png', className = 'app-header--image', style = {'display': 'inline-block', 'height': '120px'})
                        ], style={'display': 'flex'}),
                html.P( className= 'app-body',
                        children = [html.P(f'Produto a ser vendido: {product_name.title()}', className = 'app-body--p1')]),
                html.Br(),  
                html.P('Estas são as caracteristicas do seu produto'),
                html.Div(className='app-body2',
                        children = [html.Div(children = [   
                html.Div(
                        className = 'app-list',
                        children = [
                                html.Div(
                                        className = 'app-list--list1',
                                        children = [
                                        html.Ul(children=[f"Categoria principal"], className = 'app-list--firstelements'),
                                        html.Ul(children = [f'Categoria secundária'], className = 'app-list--firstelements'),
                                        html.Ul(children= [f'Nome da marca'], className = 'app-list--firstelements'),
                                        html.Ul(children=[f'Condição do item'], className = 'app-list--firstelements'),
                                        html.Ul(children=[f'Tipo de frete '], className = 'app-list--firstelements')
                                ]),
                                html.Div(
                                        className = 'app-list--list2',
                                        children=[
                                        html.Ul(children=category, className = 'app-list--elements'),
                                        html.Ul(children=subcategory, className = 'app-list--elements'),
                                        html.Ul(children=brand_name.title(), className = 'app-list--elements'),
                                        html.Ul(children=condition_classificator[condition].title(), className = 'app-list--elements'),
                                        html.Ul(children=shipping_classificator[shipping].title(), className = 'app-list--elements')
                                ])
                ], style = {'display':'flex'}
                ),
                html.Div(
                        className = 'app-body--preco',
                        children = [
                        html.P(
                        children = ['Preço($)'], className = 'app-body--preco1'),
                        html.P(
                        children =  price , className = 'app-body--preco2')
                        ], style = {'display':'flex'}),
                html.P(children = 'Avaliação do nome/descrição'),
                html.Div(
                        className = 'app-body--nome',
                        children = [
                        html.P(
                        children = ['Nome'], className = 'app-body--nome1'),
                        html.P(
                        children = score_name.capitalize(), className = 'app-body--nome2')
                        ], style = {'display':'flex'}),
                html.Div(
                        className = 'app-body--descricao',
                        children = [
                        html.P(
                        children = ['Descrição'], className = 'app-body--descricao1'),
                        html.P(
                        children = score_name.capitalize(), className = 'app-body--descricao2')
                        ], style = {'display':'flex'})], className='app-body2--text'),
                
                html.Div(
                        className = 'app-body2--graph',
                        children=[
                        html.Div(children = [dcc.Graph(
                        figure=fig_name
                ),
                        html.Div(children = [dcc.Graph(
                        figure=fig_description)])])
                ])]),
                html.Div(
                        className = 'app-graph',
                        children = [
                        html.Div(children=[
                        dcc.Graph(
                                id = 'graph')
                        ], style={'display': 'inline-block'}),
                        html.Div(
                        className = 'app-RadioItems',
                        children = [
                        html.Label(['Faixa de tempo do gráfico']),
                        html.Div(children = [dcc.RadioItems(
                                                        id = 'yaxis',
                                                        options = [
                                                                {'label': 'Diário', 'value': 'day'},
                                                                {'label': '7 Dias', 'value': '7days'},
                                                                {'label': '15 Dias', 'value': '15days'}
                                                        ],
                                                        value='day',
                                                        className = 'app-RadioItems--style',
                                                        labelStyle={'display': 'block'}
                                                        )]
                                                        )
                                                ], style={'display': 'inline-block', 'vertical-align': 'top'}
                                        )
                                ], style={'width': '1400px', 'display': 'inline-block'})
                        ]
                )
        else:
                app = Dash(__name__)
                app.layout = html.Div(children = [
                html.Div(
                        className = 'app-header',
                        children = [
                                html.H1(f'Olá, {name_cliente.title()}!', className = "app-header--title", style = {'display': 'inline-block'}),
                                html.Img(src = '/assets/image.png', className = 'app-header--image', style = {'display': 'inline-block', 'height': '120px'})
                        ], style={'display': 'flex'}),
                html.P( className= 'app-body',
                        children = [html.P(f'Produto a ser vendido: {product_name.title()}', className = 'app-body--p1')]),
                html.Br(),  
                html.P('Estas são as caracteristicas do seu produto'),
                html.Div(className='app-body2',
                        children = [html.Div(children = [   
                html.Div(
                        className = 'app-list',
                        children = [
                                html.Div(
                                        className = 'app-list--list1',
                                        children = [
                                        html.Ul(children=[f"Categoria principal"], className = 'app-list--firstelements'),
                                        html.Ul(children = [f'Categoria secundária'], className = 'app-list--firstelements'),
                                        html.Ul(children= [f'Nome da marca'], className = 'app-list--firstelements'),
                                        html.Ul(children=[f'Condição do item'], className = 'app-list--firstelements'),
                                        html.Ul(children=[f'Tipo de frete '], className = 'app-list--firstelements')
                                ]),
                                html.Div(
                                        className = 'app-list--list2',
                                        children=[
                                        html.Ul(children=category, className = 'app-list--elements'),
                                        html.Ul(children=subcategory, className = 'app-list--elements'),
                                        html.Ul(children=brand_name.title(), className = 'app-list--elements'),
                                        html.Ul(children=condition_classificator[condition].title(), className = 'app-list--elements'),
                                        html.Ul(children=shipping_classificator[shipping].title(), className = 'app-list--elements')
                                ])
                ], style = {'display':'flex'}
                ),
                html.Div(
                        className = 'app-body--preco',
                        children = [
                        html.P(
                        children = ['Preço($)'], className = 'app-body--preco1'),
                        html.P(
                        children = price, className = 'app-body--preco2')
                        ], style = {'display':'flex'}),
                html.P(children = 'Avaliação do nome/descrição'),
                html.Div(
                        className = 'app-body--nome',
                        children = [
                        html.P(
                        children = ['Nome'], className = 'app-body--nome1'),
                        html.P(
                        children = score_name.capitalize(), className = 'app-body--nome2')
                        ], style = {'display':'flex'})], className='app-body2--text'),
                
                html.Div(children = [dcc.Graph(
                        figure=fig_name,
                        className= 'app-body2--graph'
                )])]),
                html.Div(
                        className = 'app-graph',
                        children = [
                        html.Div(children=[
                        dcc.Graph(
                                id = 'graph')
                        ], style={'display': 'inline-block'}),
                        html.Div(
                        className = 'app-RadioItems',
                        children = [
                        html.Label(['Faixa de tempo do gráfico']),
                        html.Div(children = [dcc.RadioItems(
                                                        id = 'yaxis',
                                                        options = [
                                                                {'label': 'Diário', 'value': 'day'},
                                                                {'label': '7 Dias', 'value': '7days'},
                                                                {'label': '15 Dias', 'value': '15days'}
                                                        ],
                                                        value='day',
                                                        className = 'app-RadioItems--style',
                                                        labelStyle={'display': 'block'}
                                                        )]
                                                        )
                                                ], style={'display': 'inline-block', 'vertical-align': 'top'}
                                        )
                                ], style={'width': '1400px', 'display': 'inline-block'})
                        ]
                )


        @app.callback(
        Output('graph', 'figure'),
        [Input(component_id='yaxis', component_property='value')]
        )

        def graph_builder(value):
                if value == 'day':
                        fig = go.Figure()
                        #adição dos traços
                        fig.add_trace(
                        go.Scatter
                        (
                        y = categories_filter['all']['Total'].values,
                        x = categories_filter['all']['Data'].values,
                        marker_color = '#52b788',
                        )
                        )

                        #configuração do layout
                        fig.update_layout(
                                title = {'text': f'<b  style = "color:#52b788;font-size:22"><br>Total de compras no ano de 2018 da categoria {category}</br>',
                                        'font_family':"Arial",
                                        'font_size':12,
                                        'xref' :'paper',
                                        'y': 0.97,
                                        'x': 0,
                                        'xanchor': 'left',
                                        'yanchor': 'bottom'},
                                margin=dict(
                                l=100,
                                r=200,
                                b=50,
                                t=100,
                                pad=5
                                ),
                                width=1000,
                                height=600,
                                paper_bgcolor = 'rgb(10,10,10)', # cor de fundo do papel do gráfico
                                plot_bgcolor = 'rgb(10,10,10)', # cor de fundo do gráfico
                                yaxis = dict(tickfont=dict(color="#52b788"))
                        
                        )

                        #configuração dos eixos
                        fig.update_xaxes(showgrid=False, visible = False)
                        fig.update_yaxes(showgrid=False, zerolinecolor = 'rgb(10,10,10)', )
                        return fig

                elif value == '7days':
                        fig = go.Figure()
                        fig.add_trace(
                        go.Scatter(
                        y = categories_filter['7d']['Total'].values,
                        x = categories_filter['7d']['Dias'].values,
                        marker_color = '#52b788',
                        )
                        )

                        #configuração do layout
                        fig.update_layout(
                                title = {'text': f'<b  style = "color:#52b788;font-size:22"><br>Total de compras no ano de 2018 da categoria {category}</br>',
                                        'font_family':"Arial",
                                        'font_size':12,
                                        'xref' :'paper',
                                        'y': 0.97,
                                        'x': 0,
                                        'xanchor': 'left',
                                        'yanchor': 'bottom'},
                                margin=dict(
                                l=100,
                                r=200,
                                b=50,
                                t=100,
                                pad=5
                                ),
                                width=1000,
                                height=600,
                                paper_bgcolor = 'rgb(10,10,10)', # cor de fundo do papel do gráfico
                                plot_bgcolor = 'rgb(10,10,10)', # cor de fundo do gráfico
                                yaxis = dict(tickfont=dict(color="#52b788"))
                        
                        )

                        #configuração dos eixos
                        fig.update_xaxes(showgrid=False, visible = False)
                        fig.update_yaxes(showgrid=False, zerolinecolor = 'rgb(10,10,10)', )
                        return fig
                else:
                        fig = go.Figure()
                        fig.add_trace(
                        go.Scatter(
                        y = categories_filter['15d']['Total'].values,
                        x = categories_filter['15d']['Dias'].values,
                        marker_color = '#52b788',
                        )
                        )

                        #configuração do layout
                        fig.update_layout(
                                title = {'text': f'<b  style = "color:#52b788;font-size:22"><br>Total de compras no ano de 2018 da categoria {category}</br>',
                                        'font_family':"Arial",
                                        'font_size':12,
                                        'xref' :'paper',
                                        'y': 0.97,
                                        'x': 0,
                                        'xanchor': 'left',
                                        'yanchor': 'bottom'},
                                margin=dict(
                                l=100,
                                r=200,
                                b=50,
                                t=100,
                                pad=5
                                ),
                                width=1000,
                                height=600,
                                paper_bgcolor = 'rgb(10,10,10)', # cor de fundo do papel do gráfico
                                plot_bgcolor = 'rgb(10,10,10)', # cor de fundo do gráfico
                                yaxis = dict(tickfont=dict(color="#52b788"))
                        
                        )

                        #configuração dos eixos
                        fig.update_xaxes(showgrid=False, visible = False)
                        fig.update_yaxes(showgrid=False, zerolinecolor = 'rgb(10,10,10)', )
                        return fig

        with suppress_stdout():
                def open_browser():
                        webbrowser.open_new("http://localhost:{}".format(8050))
                if __name__ == '__main__':
                        Timer(1, open_browser).start()
                        app.run_server(debug=True, use_reloader=False, port=8050)
        
        open_browser()
                        
recomendation()
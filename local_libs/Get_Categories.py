import numpy as np
import pandas as pd

# Classe responsável pela divisão de categorias na base de dados principal
# O objetivo principal da criação da classe foi otimizar processos e aumentar a eficiência de código, visando utilizar de "built-in functions" para aumentar a eficiência, o código
# anterior estava apresentando tempo de execução de 9-10h e essa classe executa faz a mesma lógica dentro de segundos.
# CategorySelector possui os seguintes parâmetros:
#       main_frame: a base principal de dados
#       column: coluna alvo que servirá de base para seleção de categorias
#       main_category_name: retorna uma lista com apenas os nomes das categorias principais
#       return_first_category: retorna uma dataframe com a primeira categoria e suas respectivas contagens
#       save_files: retorna os arquivos em fornado .csv (verificar armazenamento interno)
#
# CategorySelector possui 3 funções, sendo que elas são:
#
#      - name_and_count_category_level: função responsável por realizar a contagem das categorias, o funcionamento da função é realizar um split (possível alteração: é possível especificar o split),
#                                       e é armazenado os elementos dentro da posição especificada por level (depende da lista que será analisada, passar um valor para level maior que sua lista)
#                                       irá causar um erro) e armazenando dentro de uma lista, depois é utilizado do pandas para que ele conte os valores que foram armazenados dentro da lista
#                                       e faça o retorno de um dataframe com o nome das categorias e a contagem (ou caso percentage = True, também retorna as porcentagens em outro arquivo)          
#               Parâmetros:
#                   column: coluna que irá sofrer alteração
#                   level: nível ou posição da lista que será retornado as categorias
#                   percentage (padrão False): caso este parâmetro seja igual a True, retorna um dataframe com as porcentagens das categorias
#       
#      - create_files: função simples que cria arquivo de acordo com as chaves do dicionário
#               Parâmetros:
#                   values (dict): dicionário que será utilizado para criação dos arquivos
#
#      - get_categories: função responsável por coletar as categorias, dentro da função podemos dividir ela em três:
#                 - Caso main_category_name == False: 
#                       Inicialmente gera o valor da contagem dos valores das categorias e coleta os nomes e adiciona o nome da categoria principal em uma lista
#                   essa lista é importante, pois será utilizada para retorno dos índices, depois disso é utilizado uma função do numpy para que seja procurado os nomes das categorias
#                   principais dentro da category_list, voltando seu index e depois é utilizado o squeeze para redução de dimensionalidade, pois a lista estava com uma dimensão a mais,
#                   que é desnecessária, depois disso é utilizado uma função do pandas para que seja localizado o índice de todos os itens denro da lista de índices gerada anteriormente
#                   e retorna essas linhas
#                   
#                 - Caso main_category_name == str (categoria que deve ser pesquisada) e caso return_first_category == True:
#                       Faz todo o processo anteriormente detalhado, mas volta apenas um dicionário com o nome de uma categoria específica e caso return_first_category == True, retorna
#                   a categoria principal
#
#                 - Caso main_category_name == str (categoria que deve ser pesquisada) e return_first_category == False:
#                       Faz todo o processo anteriormente detalhado, sem retornar as categorias principais

class CategorySelector:

    def __init__(self, main_frame = None, column = None, main_category_name = None, return_first_category = False, save_files = False):
        self.main_frame = main_frame
        self.column = column
        self.main_category_name = main_category_name
        self.return_first_category = return_first_category
        self.save_files = save_files

    def name_and_count_category_level(column, level = int, percentage = False):
        elements = column.str.split('/')
        category_list = []

        for i in range(len(elements)):
            element = elements[i][level]
            category_list.append(element)

        category_list = pd.DataFrame(category_list, columns = ['category_name'])
        category_count, category_percentage = pd.DataFrame(category_list.value_counts('category_name').reset_index(drop = False)), pd.DataFrame(category_list.value_counts('category_name', normalize=True).reset_index(drop = False))
        category_count.rename(columns={0 : 'Count'}, inplace = True)
        category_percentage.rename(columns = {0:'Percentage'}, inplace = True)
        category_name = category_list['category_name'].unique()

        if percentage == True:
            return category_count, category_name, category_percentage
        else:
            return category_count, category_name

    def create_files(values = dict):
        for i in values:
            values[i].to_csv(f'filtro_{i}.csv',sep='\t',index=False,)


    def get_categories(self):
        
        if self.main_category_name == None:
            first_category , name = CategorySelector.name_and_count_category_level(self.column, level = 0) 
            elements = self.column.str.split('/')
            category_list = []

            for index in range(len(elements)):
                element = elements[index][0]
                category_list.append(element)
            
            category_list = np.array(category_list)
            subcategory_dict = {}

            for category_names in name:
                index = np.squeeze(np.argwhere(category_list == category_names))
                subcategory_dict[category_names] = self.main_frame.iloc[index]
            
            if self.save_files == True:
                CategorySelector.create_files(subcategory_dict)
            
            if self.return_first_category == True:
                return first_category, subcategory_dict
            
            else:
                return subcategory_dict
            
        else:
            if self.return_first_category == True:

                first_category , name = CategorySelector.name_and_count_category_level(self.column, level = 0) 
                elements = self.column.str.split('/')
                category_list = []

                for index in range(len(elements)):
                    element = elements[index][0]
                    category_list.append(element)
                
                category_list = np.array(category_list)
                subcategory_dict = {}
                index = np.squeeze(np.argwhere(category_list == self.main_category_name))
                subcategory_dict[self.main_category_name] = self.main_frame.iloc[index]

                if self.save_files == True:
                    CategorySelector.create_files(subcategory_dict)

                return first_category , subcategory_dict

            else:
                
                elements = self.column.str.split('/')
                category_list = []

                for index in range(len(elements)):
                    element = elements[index][0]
                    category_list.append(element)
                
                category_list = np.array(category_list)
                subcategory_dict = {}
                index = np.squeeze(np.argwhere(category_list == self.main_category_name))
                subcategory_dict[self.main_category_name] = self.main_frame.iloc[index]

                if self.save_files == True:
                    CategorySelector.create_files(subcategory_dict)

                return subcategory_dict
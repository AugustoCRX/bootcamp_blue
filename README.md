# Bootcamp Blue - Dados
## Grupo 02
## Turma: C014
## Integrantes:
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; · Augusto Cesar Rodrigues Xavier
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LinkedIn: https://www.linkedin.com/in/augustocrx/
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GitHub: https://github.com/AugustoCRX
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; · Emerson Lima
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LinkedIn: https://www.linkedin.com/in/emerson-lima-69ba6471/
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GitHub: https://github.com/EmersonLCruz
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; · Henrique Grandi Baldo
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LinkedIn: https://www.linkedin.com/in/henrique-grandi-baldo/
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GitHub: https://github.com/BaldoHenrique
# Desafio

&nbsp;&nbsp;&nbsp;&nbsp;O desafio apresentado conta com a coolaboração entre as empresas Blue EdTech e Hvar com o objetivo de utilizar a base de dados presente no site Kaggle com o título "Mercari Price Suggestion Challenge" com o incremento de duas colunas a mais com o nome de date (Data) e stock (Estoque), sendo que a solução proposta fica a critério do grupo.

# Dados

## Dicionário de dados:

| Nome da coluna | Descrição |
| :---- | :---- |
| test_id | Numero identificador dos itens da lista |
| name | Titulo da lista*|
| item_condition_id | Numero da condição do item, varia de 1 a 5, sendo 1 a melhor e 5 a pior |
| category_name | Categorias da lista |
| brand_name | Nome da marca do item |
| price | Preço do produto |
| shipping | Taxa de envio, pago por: 1 - pelo vendedor 0 - pelo comprador |
| item_description | Descrição completa do item* |
| date | Data |
| stock | Estoque |

*¹- Nessas colunas existe um valor chamado [rm], esse valor significa "removed" ou removido, significa que o preço (exemplo: $20) foi removido.

- ## Observações sobre os dados:

1. A observação *¹ se apresenta sempre que existe um valor de preço na descrição do produto, sejam eles frases ou valores únicos de preço;

2. As colunas date e stock foram geradas aleatoriamente;

3. Existem dados nulos, sendo que estes estão localizados nas colunas: "category_name", "brand_name" e "item_description";

4. A data varia entre os meses dentro do ano de 2018;

5. A observação [rm] está presente apenas nas colunas "item_description" e "name".

# Hipotéses

&nbsp;&nbsp;&nbsp;&nbsp;A definir

# Objetivos

- Sprint 1

    1. Organização das tarefas no Kanban
    2. Atribuição das tarefas
        
        Augusto:
        
        - Inserir o arquivo na cloud
        - Apresentação dos modelos iniciais
        - Relatório de desenvolvimento

        Emerson:

        - Visualizações iniciais
        - Inconsistência nos dados

        Henrique:

        - Verificação de tipagem
        - Limpeza dos dados nulos

    3. Repositório criado
    4. Primeiras hipóteses
    5. Primeiros modelos
    6. Inicio do relatório

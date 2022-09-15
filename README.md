# Bootcamp Blue - Dados
## Grupo 02
## Turma: C014
## Integrantes:
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; · Augusto Cesar Rodrigues Xavier
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LinkedIn: https://www.linkedin.com/in/augustocrx/
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GitHub: https://github.com/AugustoCRX
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; · Emerson Lima Cruz
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LinkedIn: https://www.linkedin.com/in/emerson-lima-69ba6471/
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GitHub: https://github.com/EmersonLCruz
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; · Henrique Grandi Baldo
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LinkedIn: https://www.linkedin.com/in/henrique-grandi-baldo/
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GitHub: https://github.com/BaldoHenrique

&nbsp;
# Desafio


&nbsp;&nbsp;&nbsp;&nbsp;O desafio apresentado conta com a coolaboração entre as empresas Blue EdTech e Hvar com o objetivo de utilizar a base de dados presente no site Kaggle com o título "Mercari Price Suggestion Challenge" com o incremento de duas colunas a mais com o nome de date (Data) e stock (Estoque), sendo que a solução proposta fica a critério do grupo.

<p></p>

# Dados

## Dicionário de dados:

| Nome da coluna | Tipo | Descrição | Observação |
| :---- | :---- | :--- | :--- |
| test_id | Numérica discreta | Representa o índice do produto | - |
| name | Categórico nominal | Titulo da lista* | - |
| item_condition_id | Catégorico ordinal | Numero que identifica a condição do item | Está em escala de 1 a 5, sendo 1 a melhor e 5 a pior |
| category_name | Categórico nominal | Categorias vinculadas ao produto | - |
| brand_name | Categórico nominal | Nome da marca do item | - |
| price | Numérica discreta | Preço do produto anunciado | Coluna alvo do arquivo teste |
| shipping | Categórico nominal | Identifica quem pagou a taxa de envio | <p>1 - Vendedor</p><p> 0 - Comprador</p> |
| item_description | Categórico nominal | Descrição completa do item* | - |
| date | Categórico ordinal | Data da venda | - |
| stock | Numérico ordinal | Quantidade em estoque | - |

*¹- Nessas colunas existe um valor chamado [rm], esse valor significa "removed" ou removido, significa que o preço (exemplo: $20) foi removido.

<p></p>

- ## Observações sobre os dados:

1. A observação *¹ se apresenta sempre que existe um valor de preço na descrição do produto, sejam eles frases ou valores únicos de preço;

2. As colunas date e stock foram geradas aleatoriamente;

3. Existem dados nulos, sendo que estes estão localizados nas colunas: "category_name", "brand_name" e "item_description";

4. A data varia entre os meses dentro do ano de 2018;

5. A observação [rm] está presente apenas nas colunas "item_description" e "name".

<p></p>

# Hipotéses

<ol>
<li> Seria possível realizar uma união ou remoção de categorias similares? Pensando no fato de algumas categorias serem insuficientes ou desnecessárias, podendo estas serem consideradas lixo?</li>
<p></p>
<li>Dentro do nome e a descrição do produto, seria possível realizar uma analise comparativa entre a quantidade de lixo, palavras relevantes e a marca dentro do preço final do produto?</li>
<p></p>
<li>Data, estoque e preço são variáveis que geralmente caminham juntas e sempre possuem alguma história para contar. Esses dados poderiam explicar através de visualizações, se existe uma variação de preço devido a uma data importante, ou quais produtos venderam mais, ou se o vendedor efetua ou não o pagamento dos fretes.</li>
</ol>

<p></p>

# Objetivos

- Sprint 1
    <ol>
    <li>Organização das tarefas no Kanban</li>
    <li>Atribuição das tarefas</li>
    <p>
        
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
        
    </p>

    <li>Repositório criado</li>
    <li> Primeiras hipóteses</li>
    <li>Primeiros modelos</li>
    <li>Inicio do relatório</li>
    </ol>


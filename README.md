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
<li> 
Seria possível realizar uma união ou remoção de categorias similares? Pensando no fato de algumas categorias serem insuficientes ou desnecessárias, podendo estas serem consideradas lixo?
<ul>
    <li>
    Dentro da Hipótese da união de categorias foi analisado: 
    que algumas categorias eram o somatório de outras como exemplo a categoria
    Handmade onde contia produtos equivalentes em preço nas demais categorias, ou seja, o produto artesanal não implicava no
    preço final do produto por esse motivo essa categoria foi fundida entre as categorias Masculino, Feminino e Infantil, assim como a categoria Collective & Vintage.
    </li>
</ul>
</li>
<p></p>
<li>Dentro do nome e a descrição do produto, seria possível realizar uma analise comparativa entre a quantidade de lixo, palavras relevantes e a marca dentro do preço final do produto?
<ul>
	<li> Verificação de necessidade de trabalhar com as variáveis 'name' e 'item_description'</li>
	<li> Essas duas variáveis não tem um padrão muito definido, o objetivo é fazer análises de NLP para conseguir criar um padrão e verificar se o modelo responde bem</li>
	<li>
    Foram feitas análises nas colunas 'name' e 'item_description'
    </li>
	<li>
    Foi contatado que as colunas não seguem um padrão significativo, os usuários utilizaram palavras aleatórias para preencher estas duas colunas
    </li>
	<li>
    Foi feita uma limpeza utilizando word_tokenize, stopwords, WordNetLemmatizer, PorterStemmer
    </li>
	<li>
    Com essa limpeza foi possível ter as palavras padronizadas
    </li>
	<li>
    Utilizando as palavras padronizadas foi feita uma varredura para ver quais se repetiam mais vezes, logo essas palavras foram consideradas mais relevantes.
    </li>
	<li>
    Foram consideradas mais relevantes as palavras que se repetiam mais de 50 vezes
    </li>
	<li>
    Com as palavras que se repetiam mais de 50 vezes, foi feita uma varredura para ver quais itens tinham mais palavras relevantes.
    </li>
	<li>
    Foi feita uma numeração de palavras relevantes para cada item
    </li>
	<li>
    De 0 a 10 os itens foram classificados
    </li>
	<li>
    No caso da coluna 'item_description' 10 foi considerada uma descrição bem feita, logo teve mais peso.
    </li>
	<li>
    No caso da coluna 'name' 1 foi considerada um nome mais acertivo
    </li>
    <ul>
	<li>Resumindo:
     		<li>
            A coluna 'iten_description' tem uma numeração de 0 a 10, onde 0 a descrição é ruim, mal feita e 10 a descrição é bem feita.
            </li>
     		<li>
            A coluna 'name' tem uma numeração de 1 a 10, onde 1 tem um nome acertivo, objetivo, e o 10 é um nome mais complicado, chama menos a atenção do comprador 
            </li>
		    <li>
            A hipótese foi confirmada, de acordo com os gráficos o 'iten_description' e 'name tem relação com o preço dos produtos
            </li>
    </ul>
</li>
</ul>
<p></p>
<li>Data, estoque e preço são variáveis que geralmente caminham juntas e sempre possuem alguma história para contar. Esses dados poderiam explicar através de visualizações, se existe uma variação de preço devido a uma data importante, ou quais produtos venderam mais, ou se o vendedor efetua ou não o pagamento dos fretes.

<ul>
    <li>
    Em relação a tempo, os dados fornecem uma visão totalmente errada da realidade, comparando com o gráfico apresentado das empresas do Mercado Livre, Americanas, Submarino, Netshoes e Maganize Luiza, ele não apresenta uma sazonalidade viável, podemos dizer que eles mais parecem um exame médico do que uma sazonalidade, então podemos descartar a coluna tempo, por conta de conter dados que não irão ajudar dentro dos modelos de inteligência artificial, com isso a hipótese de sazonalidade de torna FALSA, ela não impacta em nada nos dados.
    </li>
    <br>
    <li>
    Em relação ao frete, podemos concluir é bem variado em relação a categoria, temos categorias em que os produtos que são fretados pelo comprador são mais caros e temos outras que são totalmente o contrário então a hipótese pode ser concluida sendo uma contradição (contradição pode ser definida quando uma hipótese contêm saídas tanto verdadeiras como falsas)
    </li>
</ul>
</li>
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

- Sprint 2

    <ol>
    <li>Construção do discord</li>
    <li>Construção do primeiro modelo de machine learning</li>
    <li>Atualização dos documentos</li>
    <li>Comprovação da primeira hipotése</li>
    <li>Limpeza profunda dos dados</li>
    <li>Inicio da apresentação</li>
    </ol>


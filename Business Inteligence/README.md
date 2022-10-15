# Hipóteses e suas validações:

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

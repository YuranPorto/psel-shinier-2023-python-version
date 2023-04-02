# Versão python do desafio proposto pela Shinier
#### Projeto original realizado em php https://github.com/YuranPorto/psel-shinier-2023
<br>

### - Todos os pacotes necessários estão no arquivo Requerimentes.txt
### - Basta no terminal usar pip install requerimentes.txt
### - Se preferir pode ir instalando 1 por um, abrindo o arquivo e execultando pip install nome_do_pacot==versão
<br>

<hr><br>
<br>

## Query:
<br>
<br>

### Criada uma query para busca dos dados, sem a necessídade de uma query muito grande no arquivo principal.
### A query pode ser modificada no arquivo DB dentro da pasta SQL.
```
SELECT
  em.nome, 
  'Documento ' || cr.documento as DOCUMENTO, 
  CAST(cr.valor AS NUMERIC(10,2)) as A_PAGAR, 
  CAST(bx.valor AS NUMERIC(10,2)) as PAGO, 
  SUBSTRING(CAST(cr.emissao as DATE) FROM 9 FOR 2) || '/' || 
  SUBSTRING(CAST(cr.emissao as DATE) FROM 6 FOR 2) || '/' || 
  SUBSTRING(CAST(cr.emissao as DATE) FROM 1 FOR 4) as DATA_LANCAMENTO, 

  SUBSTRING(CAST(cr.vencto as DATE) FROM 9 FOR 2) || '/' || 
  SUBSTRING(CAST(cr.vencto as DATE) FROM 6 FOR 2) || '/' || 
  SUBSTRING(CAST(cr.vencto as DATE) FROM 1 FOR 4) as VENCIMENTO,

  SUBSTRING(CAST(bx.transmissao as DATE) FROM 9 FOR 2) || '/' || 
  SUBSTRING(CAST(bx.transmissao as DATE) FROM 6 FOR 2) || '/' || 
  SUBSTRING(CAST(bx.transmissao as DATE) FROM 1 FOR 4) as CONFIRMA_PAGAMENTO,

  SUBSTRING(CAST(bx.baixa as DATE) FROM 9 FOR 2) || '/' || 
  SUBSTRING(CAST(bx.baixa as DATE) FROM 6 FOR 2) || '/' || 
  SUBSTRING(CAST(bx.baixa as DATE) FROM 1 FOR 4) as DT_RECEBIDO


FROM CRD111 as cr
LEFT JOIN BXD111 as bx ON cr.documento = bx.documento
JOIN EMD101 as em ON cr.CGC_CPF = em.cgc_cpf
UNION
SELECT
  em.nome, 
  ma.nome_tipo,
  ma.valor_orig,
  ma.valor, 
  SUBSTRING(CAST(ma.emissao as DATE) FROM 9 FOR 2) || '/' || 
  SUBSTRING(CAST(ma.emissao as DATE) FROM 6 FOR 2) || '/' || 
  SUBSTRING(CAST(ma.emissao as DATE) FROM 1 FOR 4) as emissao, 
  
  SUBSTRING(CAST(ma.vencto as DATE) FROM 9 FOR 2) || '/' || 
  SUBSTRING(CAST(ma.vencto as DATE) FROM 6 FOR 2) || '/' || 
  SUBSTRING(CAST(ma.vencto as DATE) FROM 1 FOR 4) as vencto, 

  SUBSTRING(CAST(ma.data_pagto as DATE) FROM 9 FOR 2) || '/' || 
  SUBSTRING(CAST(ma.data_pagto as DATE) FROM 6 FOR 2) || '/' || 
  SUBSTRING(CAST(ma.data_pagto as DATE) FROM 1 FOR 4) as data_pagto,


  SUBSTRING(CAST(ma.data_modificado as DATE) FROM 9 FOR 2) || '/' || 
  SUBSTRING(CAST(ma.data_modificado as DATE) FROM 6 FOR 2) || '/' || 
  SUBSTRING(CAST(ma.data_modificado as DATE) FROM 1 FOR 4) as vencto
FROM MAN111 as ma
JOIN EMD101 as em ON ma.CNPJ_CPF = em.cgc_cpf

```
<br>

<hr><br>

# Classes:
<br>
<br>

## DataBase
<br>

### Criando a conexão com um banco de dados firebird.
### Neste exemplo, vamos demonstrar como realizar a conexão com um banco de dados Firebird utilizando a biblioteca firebirdsql em Python.
## Exemplo de uso:

```
import firebirdsql
import credentials



class DataBase:

    conn = firebirdsql.connect(
        host=credentials.HOST,
        database=credentials.DATABASE,
        port=credentials.PORT,
        user=credentials.USER,
        password=credentials.PASSWORD,
        charset='WIN1252'
    )

    def execute(self, sql):
        try:
            cur =self.conn.cursor()
            cur.execute(sql)
            return cur

        except Exception(BaseException):
            print(f'Erro ao conectar no banco de dados {Exception(BaseException)}')

```
<br>

### A classe DataBase possui um método execute que recebe como parâmetro uma instrução SQL e retorna um cursor para manipulação dos dados retornados. 
### Para realizar a conexão, é necessário passar as informações de host, database, port, user, password e charset.
<br>

### A partir desse exemplo, você pode adaptar a conexão com o seu próprio banco de dados Firebird em Python.
<br>
<hr><br>

## CriaCsv:
<hr>
<br>

#### A classe CriaCsv é responsável por criar um arquivo CSV que contém dados financeiros de uma clínica. 
#### A classe possui um construtor que instancia um objeto da classe DataBase (importada do arquivo Database.py) 
#### para acessar o banco de dados da clínica. Em seguida, a classe utiliza o método execute() do objeto Database 
#### para executar um script SQL (contido no arquivo SQL/query.sql) e recuperar dados financeiros do banco de dados.
<br>

#### Os dados recuperados são armazenados em uma lista chamada dadosBd, que será usada posteriormente para criar o arquivo CSV. 
#### Além disso, a classe possui uma lista chamada cabecalho, que define os títulos das colunas do arquivo CSV.
<br>

#### O arquivo CSV é criado utilizando a biblioteca pandas. A lista dadosBd é convertida em um DataFrame do pandas, 
#### que é então salvo como um arquivo CSV no caminho 'Files/Finaceiro.#### csv' com o separador de campo ';'. 
#### O parâmetro index=False é utilizado para não incluir o índice do DataFrame no arquivo CSV.
<br>

## Métodos
#### A classe CriaCsv não possui métodos públicos além do construtor.
<br>

## Atributos
#### cur: objeto cursor do banco de dados, utilizado para executar o script SQL contido em 'SQL/query.sql' e recuperar os dados financeiros do banco de dados da clínica.
#### dadosBd: lista que armazena os dados financeiros recuperados do banco de dados.
#### pegaDados: dicionário vazio que não é utilizado na classe.
#### dadosDbIndex: inteiro que representa o índice atual da lista dadosBd. É inicializado com o valor 0.
#### cabecalho: lista que contém os títulos das colunas do arquivo CSV.
#### csv: objeto DataFrame do pandas que é utilizado para armazenar os dados financeiros da clínica e, posteriormente, exportados para um arquivo CSV.
<br>
<br>

## Exemplo de uso
```
from .Database import DataBase as Database
import pandas as pd

db = Database()

class CriaCsv():

    cur = db.execute(open('SQL/query.sql', 'r').read())

    dadosBd = []
    pegaDados = {}
    dadosDbIndex = 0
    for dado in cur.fetchall():
        temp = list(dado)
        temp.insert(0, '')
        temp.insert(3, 'Dinheiro')
        dadosBd.append(temp)

    cabecalho = [
        'Nome da clinica',
        'Nome do paciente',
        'Descricao do lancamento',
        'Forma de pagamento',
        'Valor a pagar',
        'Valor pago',
        'Data de criacao do lancamento',
        'Data de vencimento',
        'Data de confirmacao ',
        'Data de recebimento'
    ]

    csv = pd.DataFrame(dadosBd)
    csv.to_csv('Files/Finaceiro.csv', header=cabecalho, sep=';', index=False)
    print('CSV CRIADO')

```
<br>

#### Neste exemplo, a classe CriaCsv é utilizada para criar um arquivo CSV chamado 'Financeiro.csv' que contém os dados financeiros da clínica.
#### Os dados financeiros são recuperados do banco de dados da clínica utilizando o objeto Database e o método execute(). 
#### Em seguida, os dados são armazenados em uma lista e, posteriormente, convertidos em um DataFrame do pandas. Finalmente, 
#### o DataFrame é salvo como um arquivo CSV no caminho 'Files/Financeiro.csv' com
<br>

<br>

<hr><br>

## CriaExcel
<hr>
<br>

#### Classe responsável por criar uma planilha do Excel a partir de um arquivo CSV.
<br>

#### Atributos
#### arquivoCsv (str): caminho do arquivo CSV que será lido
#### planilha (Workbook): instância da classe Workbook do openpyxl que representa a planilha Excel de base.
#### abaPlanilha (Worksheet): instância da classe Worksheet do openpyxl que representa a aba ativa da planilha Excel.
#### fill (PatternFill): instância da classe PatternFill do openpyxl que define a cor de fundo das células da primeira linha.
#### font (Font): instância da classe Font do openpyxl que define o estilo da fonte das células da primeira linha.
#### tamanhoColuna (list): lista que armazena a largura de cada coluna da planilha.
#### Métodos
#### __init__(): método construtor que inicializa a planilha Excel de base e a aba ativa.
<br>

#### criar_planilha(): método que lê o arquivo CSV, itera sobre cada linha e célula do arquivo, e adiciona as informações na planilha Excel. 
#### Além disso, ajusta a largura das colunas, aplica a cor de fundo e estilo na primeira linha da planilha, e salva a planilha em um arquivo com nome diferente.
<br>

### Exemplo de uso:
<br>

```
criar_excel = CriaExcel()
criar_excel.criar_planilha()

```
<br>

#### Após a execução do código, será criada uma planilha do Excel com as informações contidas no arquivo CSV.

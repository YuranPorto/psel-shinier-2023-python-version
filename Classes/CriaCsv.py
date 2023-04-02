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

import os.path
import time

from Classes.CriaCsv import CriaCsv
from Classes.CriaExcel import CriaExcel

cria_csv = CriaCsv
cria_excel = CriaExcel


financeiro_csv = 'Files/Finaceiro.csv'
financeiro_xlsx = 'Files/Financeiro.xlsx'
nome_arquivo = 'Financeiro.csv' if financeiro_csv else 'Financeiro.xlsx'


def execucao():

    if os.path.isfile(financeiro_csv) or os.path.isfile(financeiro_xlsx):
        escolha = str(input(f'Já existe um {nome_arquivo} dejasa substitui-lo? S/N: ')).upper()
        if escolha.upper() == 'S' or escolha.upper() == 'SIM':
            time.sleep(1)
            print('Gerando arquivo CSV ...')
            time.sleep(0.5)
            cria_csv()
            return True

    elif not os.path.isfile(financeiro_csv):
        time.sleep(1)
        print('Gerando arquivo CSV ...')
        time.sleep(1)
        cria_csv()
        time.sleep(1)
        print('Gerando arquivo Excel')
        time.sleep(1)
        cria_excel()
        time.sleep(1)
    elif os.path.isfile(financeiro_csv) and not os.path.isfile(financeiro_xlsx):
        time.sleep(1)
        print('Gerando arquivo Excel')
        time.sleep(1)
        cria_excel()
        return True

execucao()

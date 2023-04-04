import os.path
import time

from Classes.CriaExcel import CriaExcel

financeiro_csv = 'Files/Financeiro.csv'
financeiro_xlsx = 'Files/Financeiro.xlsx'
nome_arquivo = 'Financeiro.csv' if financeiro_csv else 'Financeiro.xlsx'

#cria_csv = CriaCsv
cria_excel = CriaExcel()


def execucao():
    if os.path.exists(financeiro_csv) or os.path.exists(financeiro_xlsx):
        escolha = str(input(f'Já existe um {nome_arquivo}, deseja substituí-lo? S/N: ')).upper()
        if escolha.upper() == 'S' or escolha.upper() == 'SIM':
            from Classes.CriaCsv import CriaCsv
            cria_csv = CriaCsv
            time.sleep(1)
            print('Gerando arquivo CSV ...')
            time.sleep(0.5)
            cria_csv()
            time.sleep(1)
            print('Gerando arquivo Excel ... ')
            time.sleep(1)
            cria_excel.gera_excel()
        else:
            return False
    if os.path.exists(financeiro_csv) is False:
        from Classes.CriaCsv import CriaCsv
        cria_csv = CriaCsv
        time.sleep(1)
        print('Gerando arquivo CSV ...')
        time.sleep(1)
        cria_csv()
        time.sleep(1)
        cria_excel.gera_excel()

        return True

    if os.path.exists(financeiro_csv) is True and os.path.exists(financeiro_xlsx) is False:
        time.sleep(1)
        print('Gerando arquivo Excel ... ')
        time.sleep(1)
        cria_excel.gera_excel()

        return True


# def execucao():
#     if os.path.isfile(financeiro_csv) or os.path.isfile(financeiro_xlsx):
#         escolha = str(input(f'Já existe um {nome_arquivo} dejasa substitui-lo? S/N: ')).upper()
#         if escolha.upper() == 'S' or escolha.upper() == 'SIM':
#             time.sleep(1)
#             print('Gerando arquivo CSV ...')
#             time.sleep(0.5)
#             CriaCsv.CriaCsv()
#             return True
#     else:
#         if os.path.isfile(financeiro_csv) is False:
#             time.sleep(1)
#             print('Gerando arquivo CSV ...')
#             time.sleep(1)
#             CriaCsv.CriaCsv()
#             time.sleep(1)
#             print('Gerando arquivo Excel')
#             time.sleep(1)
#             CriaExcel.CriaExcel()
#             time.sleep(1)
#         else:
#             time.sleep(1)
#             print('Gerando arquivo Excel')
#             time.sleep(1)
#             CriaExcel.CriaExcel()
#             return True

execucao()

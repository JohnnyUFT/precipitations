import os
import csv
import re
import pandas as pd
from sqlalchemy import create_engine


def get_meta_data(row):
    return row[0].split(': ')[1].replace(' ', '').replace(':', '')

def read_file():
    PATH = os.environ.get('PATH_DATA')
    FILE = os.environ.get('FILE_NAME')
    FILE_READ = 0
    ROW_NUMBER = 0
    
    try:
        file_to_read = f'{PATH}\\{FILE}'
        with open(file_to_read, mode="r") as infile:
            table_01 = []
            table_02 = []

            pd_local = pd.DataFrame()
            pd_data = pd.DataFrame()

            for line in infile:
                line_data = re.split(',|;', line)
                print('\n', line_data)

                # if(ROW_NUMBER >= 0 and ROW_NUMBER < 9):
                #     print('\nfirst', line_data)
                #     table_01.append(line_data)
                # elif(ROW_NUMBER >= 11 and ROW_NUMBER < 23):
                #     print('\nsecond', line_data)
                #     table_02.append(line_data)

                ROW_NUMBER += 1
                
                if ROW_NUMBER >= 30:  # just for fun
                    return []

        # sucesso ao fazer a leitura do arquivo: incrementa FILE_NUMBER
        FILE_READ += 1

    except BaseException:
        print('Erro ao ler arquivo ', file_to_read)
        print('Qtd arquivos lidos com sucesso: ', FILE_READ)
        return []  # TODO: remover


def main():
    read_file()


if __name__ == '__main__':
    main()
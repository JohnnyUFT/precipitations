import os
import csv
import re
import pandas as pd
from sqlalchemy import create_engine


def read_file():
    PATH = 'C:\\Users\\johnny.gomes\\Downloads\\thiago\\data'
    FILE_READ = 0
    ROW_NUMBER = 0

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(PATH):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))

    for f in files:
        print('\n')
        print('Lendo Arquivo', FILE_READ + 1)
        print('Nome:', f)

        try:
            with open(f, mode="r") as infile:
                table_01 = []
                table_02 = []

                pd.DataFrame()

                for line in infile:
                    line_data = re.split(',|;', line)
                    print('\n', line_data)

                    if(ROW_NUMBER >= 0 and ROW_NUMBER < 9):
                        print('\nfirst', line_data)
                        table_01.append(line_data)
                    elif(ROW_NUMBER >= 11 and ROW_NUMBER < 23):
                        print('\nsecond', line_data)
                        table_02.append(line_data)

                    ROW_NUMBER += 1

            # sucesso ao fazer a leitura do arquivo: incrementa FILE_NUMBER
            FILE_READ += 1

            if FILE_READ <= 4:  # just for fun
                break

        except BaseException:
            print('Erro ao ler arquivo ', f)
            print('Qtd arquivos lidos com sucesso: ', FILE_READ)
            break  # TODO: remover
        
def main():
    read_file()


if __name__ == '__main__':
    main()

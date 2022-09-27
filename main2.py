# Caso 2: utilizacao de .csv unico com dados de varios locais
# este caso deve ser utilizado caso o arquivo 'data/prec_temp.csv' exista
# e esteja devidamente limpo e organizado.

import os
import re
from bd_config import create_connection, insert_into_local, insert_into_data, close_connection

DB_NAME = os.environ.get('DB_NAME')
PATH = os.environ.get('PATH_DATA')
FILE = os.environ.get('FILE_NAME')

def clean_data(row):
    return row[0].split(': ')[1].replace(':', '')

def remove_break_line(row):
    return row.replace('\n', '')

def read_file():
    FILE_READ = 0
    ROW_NUMBER = 0
    
    conn = create_connection(DB_NAME)
    
    try:
        file_to_read = f'{PATH}\\{FILE}'
        with open(file_to_read, mode="r") as infile:

            for row in infile:
                row_data = re.split(',|;', row)
                if row_data[0].startswith('Nome:'):
                    row_data = clean_data(row_data)
                    # insert tabela local
                    last_row_id = insert_into_local(conn, row_data)
                elif row_data[0].startswith('Data'):
                    continue
                elif row_data[0].startswith('201', 0, 4):
                    row_data.append(last_row_id)
                    # insert tabela data
                    print(row_data)
                    insert_into_data(conn, tuple(row_data))
                

                ROW_NUMBER += 1
                
                # if ROW_NUMBER >= 30:  # just for fun
                #     close_connection(conn)
                #     return None

        # sucesso ao fazer a leitura do arquivo: incrementa FILE_NUMBER
        FILE_READ += 1

    except Exception as e:
        print(e)
        print('Erro ao ler arquivo', FILE)
        print('Qtd arquivos lidos com sucesso: ', FILE_READ)
        
        close_connection(conn)
        
        return None  # TODO: remover


def main():
    read_file()


if __name__ == '__main__':
    main()
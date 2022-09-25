import os
import csv
import re
import pandas as pd
from sqlalchemy import create_engine

def get_meta_data(row):
    return row[0].split(': ')[1].replace(' ', '').replace(':', '')

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
        
        df_meta = pd.read_csv(f, sep=',|;', 
                  engine='python', header=None, nrows=9,)
        
        meta_columns = ['nome','codigo_estacao','latitude','longitude','altitude','situacao',
                       'data_inicial','data_final','periodicidade',]
        
        df_meta = df_meta.apply(get_meta_data, axis=1)
        df_meta = df_meta.rename({'0':'nome', '1':'codigo_estacao', '2':'latitude',
                                  '3':'longitude', '4':'altitude', '5':'situacao',
                                  '6':'data_inicial', '7':'data_final', '8':'periodicidade',}, axis=0)
        df_meta.index = meta_columns
        print(df_meta)
        # print(df_meta.to_dict())
        print('\n')
        
        df_data = pd.read_csv(f, sep=',|;', 
                  engine='python', header=None, skiprows=11,)
        df_data.columns = ['data_medicao','dias_precip','mensal_aut','precipitacao_total',
                       'mensal_aut_mb','pressao_atmosferica','media_mensal_aut',
                       'temperatura_media','mensal_aut_c','vento','velocidade_maxima',
                       'vento_rev','velocidade_media']
        
        print(df_data)

        FILE_READ += 1
        if FILE_READ >= 3:  # just for fun
                break

def main():
    read_file()


if __name__ == '__main__':
    main()

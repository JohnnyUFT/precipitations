import os
import pandas as pd
from bd_config import (create_connection, insert_into_local,
                       insert_into_data, close_connection)

PATH = os.environ.get('PATH_DATA')
DB_NAME = os.environ.get('DB_NAME')

def get_meta_data(row):
    return row[0].split(': ')[1].replace(':', '')

def read_file():
    FILE_READ = 0

    # abre a conexao com o banco definido no .env
    conn = create_connection(DB_NAME)
    
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
        
        df_meta = df_meta.apply(get_meta_data, axis=1)
        
        # insert tabela local
        last_row_id = insert_into_local(conn, tuple(df_meta))
        
        df_data = pd.read_csv(f, sep=',|;', 
                  engine='python', header=None, skiprows=11, 
                  keep_default_na=True, na_values=['','null', 'Null', 'NULL'],
                  on_bad_lines='warn',
                  usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],)
        
        # # elimina ultima coluna:
        # if df_data.shape[1] == 13:
        #     df_data.drop([11,12], axis=1, inplace=True)
        print(df_data.shape)
        
        # insert tabela data
        for row in df_data.itertuples():
            insert_into_data(conn, row[1:] + (last_row_id,))
        
        FILE_READ += 1
        
        # df_data.columns = ['local_id','data_medicao','dias_precip','mensal_aut','precip_total',
        #                'mensal_aut_mb','pressao_atmosferica','media_mensal_aut',
        #                'temperatura_media','mensal_aut_c','vento','velocidade_maxima',
        #                'vento_rev','velocidade_media',]
        # df_data['local_id'] = last_row_id
        
        # # print('\ndf origin', df_data.head())
        # df_data1 = df_data.apply(tuple, axis=1)
        # print('\ndf tuple', df_data1.head())
        # for row in df_data1:
        #     print('\nrow', row)
        #     # insert tabela data
        #     insert_into_data(conn, row)

        # FILE_READ += 1
        # if FILE_READ == 18:  # just for fun
        #     close_connection(conn)
        #     df_data.to_csv('df_data.csv', index=False)

def main():
    read_file()


if __name__ == '__main__':
    main()

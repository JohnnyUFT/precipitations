import os
import csv
# import pandas as pd

PATH = "C:\\Users\\johnny.gomes\\Downloads\\thiago\\data"
FILE_READ = 0
ROW_NUMBER = 0

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(PATH):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))

for f in files:
    print('Lendo Arquivo', FILE_READ+1)
    print('Nome:', f)
    
    try:
        new_file = open(f)
        csvreader = csv.reader(new_file, delimiter=',')
    
        table_01 = []
        table_02 = []
        for row in csvreader:
            if(ROW_NUMBER >= 0 and ROW_NUMBER < 9):
                # pd.DataFrame()
                table_01.append(row)
            elif(ROW_NUMBER >= 11 and ROW_NUMBER < 23):
                print('\n',row)
                table_02.append(row)
            
            ROW_NUMBER+=1
                
        print('\n',table_01)
        print('\n',table_02)

        # sucesso ao fazer a leitura do arquivo: incrementa FILE_NUMBER
        FILE_READ+=1
        
        if FILE_READ <= 4:# just for fun
            break
    
    except:
        print('Erro ao ler arquivo ', f)
        print('Qtd arquivos lidos com sucesso: ', FILE_READ)
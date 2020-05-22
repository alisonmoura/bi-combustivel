import os
import glob
import pandas as pd

FOLDER_PATH = 'datasets-copy'
os.chdir(FOLDER_PATH)

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = []

# 
# Percorre todos os arquivos .csv na pasta FOLDER_PATH
# Copias as colunas 'Região - Sigla', 'Revenda', 'Data da Coleta', 'Bandeira'
# Cria as colunas 'Id_Bandeira', 'Id_Revenda' e 'qtd_Postos_Por_Bandeira'
# Concatena todos as planilhas em uma só ('datas.csv')
# 
for f in all_filenames:
    data = pd.read_csv(f, encoding='utf-16', delimiter='\t')
    data = data.filter(items=['Região - Sigla', 'Revenda', 'Data da Coleta', 'Bandeira'], axis=1)
    data.insert(4, "Id_Bandeira", 0) 
    data.insert(5, "Id_Revenda", 0) 
    data.insert(6, "qtd_Postos_Por_Bandeira", 0) 
    combined_csv = pd.concat([data])

combined_csv.to_csv( "datas.csv", index=False, encoding="utf-16", sep="\t")    

# combined_csv = pd.concat([pd.read_csv(f, encoding="utf-16", delimiter='\t') for f in all_filenames ])
# combined_csv.to_csv( "datas.csv", index=False, encoding="utf-16", sep=",")

# data_import = pd.read_csv('datas.csv', encoding="utf-16", delimiter=',', na_filter=False)
# print(data_import.shape, '\n', data_import.head(5))
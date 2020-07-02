import os
import glob
import time
import pandas as pd
import preparer

FOLDER_PATH = 'datasets'
OUT_PATH = 'output'
OUT_FILENAME = 'etl.csv'

start = time.time()

if(not os.path.isdir(OUT_PATH)):
    print('Criando pasta {0}...'.format(OUT_PATH))
    os.mkdir(OUT_PATH)

os.chdir(FOLDER_PATH)

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.DataFrame()

# print(all_filenames)

# 
# Percorre todos os arquivos .csv na pasta FOLDER_PATH
# Copias as colunas 'Região - Sigla', 'Revenda', 'Data da Coleta', 'Bandeira'
# Cria as colunas 'Id_Bandeira', 'Id_Revenda' e 'qtd_Postos_Por_Bandeira'
# Concatena todos as planilhas em uma só ('datas.csv')
# 
for f in all_filenames:
    data = pd.read_csv(f, encoding='utf-16', delimiter='\t')
    combined_csv = pd.concat([combined_csv, data])

# combined_csv = combined_csv.head(500)

combined_csv = preparer.prepare(combined_csv)

os.chdir('../{0}'.format(OUT_PATH))
combined_csv.to_csv(OUT_FILENAME, index=False, encoding='utf-16', sep='\t')

end = time.time()
print("\nFinalizado em: %.2f segundos" % (end - start))
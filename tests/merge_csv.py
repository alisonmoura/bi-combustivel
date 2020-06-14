import os
import glob
import pandas as pd

FOLDER_PATH = 'datasets'
OUT_PATH = 'output'
OUT_FILENAME = 'data.csv'

if(not os.path.isdir(OUT_PATH)):
    print('Criando pasta {0}...'.format(OUT_PATH))
    os.mkdir(OUT_PATH)

os.chdir(FOLDER_PATH)

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = []
bandeiras = set()
revendas = set()
bandeiras_com_id = {}
revendas_com_id = {}
bandeiras_data = []
revendas_data = []

# 
# Percorre todos os arquivos .csv na pasta FOLDER_PATH
# Copias as colunas 'Região - Sigla', 'Revenda', 'Data da Coleta', 'Bandeira'
# Cria as colunas 'Id_Bandeira', 'Id_Revenda' e 'qtd_Postos_Por_Bandeira'
# Concatena todos as planilhas em uma só ('datas.csv')
# 
for f in all_filenames:
    data = pd.read_csv(f, encoding='utf-16', delimiter='\t')
    data = data.filter(items=['Estado - Sigla', 'Data da Coleta', 'Valor de Venda'], axis=1)
    # data.insert(4, 'Id_Bandeira', 0) 
    # data.insert(5, 'Id_Revenda', 0) 
    # data.insert(6, 'qtd_Postos_Por_Bandeira', 0) 
    combined_csv = pd.concat([data])

combined_csv = combined_csv.head(50)
# print(combined_csv)

# #
# # Percorre o vetor combinado juntando as Bandeiras e Revendas em set's (sem repetições)
# #
# for index, row in combined_csv.filter(items=['Bandeira', 'Revenda'], axis=1).iterrows():
#     bandeiras.add(row['Bandeira'])
#     revendas.add(row['Revenda'])

# for i in range(len(bandeiras)):
#     bandeira = bandeiras.pop()
#     bandeiras_com_id[bandeira] = i

# for i in range(len(revendas)):
#     revenda = revendas.pop()
#     revendas_com_id[revenda] = i

for i, row in combined_csv.iterrows():
    [dia, mes, ano] = row['Data da Coleta'].split('/')
    valor = float(row['Valor de Venda'].replace(',', '.'))
    valor = "%.2f" % valor

    combined_csv.loc[i,'Dia'] = dia
    combined_csv.loc[i,'Mes'] = mes
    combined_csv.loc[i,'Ano'] = ano
    combined_csv.loc[i,'Valor'] = valor
    # print(dia, mes, ano)

    # ['Estado - Sigla', 'Data da Coleta', 'Valor de Venda']
    # combined_csv.iloc[i] = {
    #     'Dia': dia,
    # }
    # combined_csv.iloc[i] = {
    #     'Id_Bandeira': bandeiras_com_id[row['Bandeira']],
    #     'Id_Revenda': revendas_com_id[row['Revenda']]
    # }
    # bandeiras_data.append(bandeiras_com_id[row['Bandeira']])
    # revendas_data.append(revendas_com_id[row['Revenda']])

# print(bandeiras_data, revendas_data)

# combined_csv['Id_Bandeira'] = bandeiras_data
# combined_csv['Id_Revenda'] = revendas_data

print(combined_csv)

# os.chdir('../{0}'.format(OUT_PATH))
# combined_csv.to_csv(OUT_FILENAME, index=False, encoding='utf-16', sep='\t')    

# # combined_csv = pd.concat([pd.read_csv(f, encoding='utf-16', delimiter='\t') for f in all_filenames ])
# # combined_csv.to_csv( 'datas.csv', index=False, encoding='utf-16', sep=',')

# # data_import = pd.read_csv('datas.csv', encoding='utf-16', delimiter=',', na_filter=False)
# # print(data_import.shape, '\n', data_import.head(5))
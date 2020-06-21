import pandas as pd

def prepare(combined_csv):
    # print(combined_csv)

    combined_csv = combined_csv.filter(items=['Estado - Sigla', 'Data da Coleta', 'Valor de Venda', 'Produto'], axis=1)

    #
    # Percorre o vetor combinado juntando as Bandeiras e Revendas em set's (sem repetições)
    #
    for i, row in combined_csv.iterrows():
        [dia, mes, ano] = row['Data da Coleta'].split('/')
        valor = str(row['Valor de Venda']).replace(',', '.')
        valor = float(valor)
        valor = "%.2f" % valor

        combined_csv.loc[i,'Dia'] = dia
        combined_csv.loc[i,'Mes'] = mes
        combined_csv.loc[i,'Ano'] = ano
        combined_csv.loc[i,'Valor'] = valor

    print(combined_csv)
    return combined_csv
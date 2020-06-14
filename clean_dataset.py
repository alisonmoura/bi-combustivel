import pandas as pd
import numpy as np

PATH="datas.csv"

data = pd.read_csv(PATH, encoding="utf-16", delimiter=',')

small = data.head(100)

print(small)

small = small.filter(items=['Região - Sigla', 'Revenda', 'Data da Coleta', 'Bandeira'], axis=1)
small.insert(4, "Id_Bandeira", 0) 
small.insert(5, "Id_Revenda", 0) 
small.insert(6, "qtd_Postos_Por_Bandeira", 0) 

print(small)

# small = np.delete(small, 4, 1)
# np.savetxt("small.csv", small, delimiter="\t", encoding="utf-16")
# small.to_csv( "small.csv", index=False, encoding="utf-16", sep="\t")``
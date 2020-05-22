import pandas as pd
import numpy as np

bandeiras = set()
bandeiras_com_id = {}
FILE_PATH = 'small.csv'
POS = -3

datas = pd.read_csv(FILE_PATH, encoding="utf-16", delimiter='\t')
datas = np.array(datas)

# Adiciona as bandeiras no set (sem repetição)
for data in datas:
    bandeiras.add(data[POS])

print(len(bandeiras), bandeiras)

for i in range(len(bandeiras)):
    bandeira = bandeiras.pop()
    bandeiras_com_id[bandeira] = i

# print(bandeiras_com_id)

for i in range(len(datas)):
    data = datas[i]
    bandeira_id = bandeiras_com_id[data[POS]]
    print(bandeira_id)
    # datas[i].append()
    # np.insert(datas, -1, bandeira_id, axis=1)
    # np.concatenate((datas, X_out)) 

# print(datas)

# combined_csv.to_csv( "datas.csv", index=False, encoding="utf-16", sep=",")

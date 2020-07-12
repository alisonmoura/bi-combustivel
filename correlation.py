import time
import pandas as pd
from scipy.stats import spearmanr

# Timer
start = time.time()

# Leitura dos dataset's (CSV)
dataset1 = pd.read_csv('datasets/csv_outputMS_ETANOL.csv', delimiter=';')
dataset2 = pd.read_csv('datasets/csv_outputMT_ETANOL.csv', delimiter=';')

data1 = []
data2 = []

# Extração do preço do combustível em um vetor 1-dimensional
for i in range(dataset1.shape[0]):
    data1.append(dataset1.loc[i]['precovenda'])
    data2.append(dataset2.loc[i]['precovenda'])

# print(data1, data2)

# Métrica de correlação de Spearman 
# Não assumimos os dados como ditribuição Gaussiana, por isso não utilizamos a correlação de Pearson
corr, _ = spearmanr(data1, data2)
print('Spearmans correlation: %.3f' % corr)
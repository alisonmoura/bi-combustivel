import os
import glob
import time
import pandas as pd
import numpy as np
import preparer

DATA_PATH = 'datas'
CHUNKS_OUT_PATH = 'chunks_out'
OUT_PATH = 'output'
OUT_FILENAME = 'etl.csv'

start = time.time()

if(not os.path.isdir(OUT_PATH)):
    print('Criando pasta {0}...'.format(OUT_PATH))
    os.mkdir(OUT_PATH)

if(not os.path.isdir(CHUNKS_OUT_PATH)):
    print('Criando pasta {0}...'.format(CHUNKS_OUT_PATH))
    os.mkdir(CHUNKS_OUT_PATH)

os.chdir(DATA_PATH)

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.DataFrame()
print('Lendo e combinando os datasets (csv)...')

for f in all_filenames:
    data = pd.read_csv(f, encoding='utf-16', delimiter='\t')
    combined_csv = pd.concat([combined_csv, data])

chunks = np.array_split(combined_csv, 40)
os.chdir('../{0}'.format(CHUNKS_OUT_PATH))
print('Gerando os chunks...')

for i in range(len(chunks)):
    print('Gerando etl-{0}.csv...'.format(str(i)))
    result = preparer.prepare(chunks[i])
    result.to_csv('etl-{0}.csv'.format(str(i)), index=False, encoding='utf-16', sep='\t')

all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
result_csv = pd.DataFrame()
print('Juntando os chunks...')

for f in all_filenames:
    data = pd.read_csv(f, encoding='utf-16', delimiter='\t')
    result_csv = pd.concat([result_csv, data])

print('Gerando resultado final...')
os.chdir('../{0}'.format(OUT_PATH))
result_csv.to_csv(OUT_FILENAME, index=False, encoding='utf-16', sep='\t')

end = time.time()
print("\nFinalizado em: %.2f segundos" % (end - start))
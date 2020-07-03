
import time
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from skits.preprocessing import HorizonTransformer
from keras.models import Sequential
from keras.layers import Dense

# Timer
start = time.time()

# Leitura dos dataset's (CSV)
dataset1 = pd.read_csv('datasets/csv_output_etanol_DF.csv', delimiter=';')
dataset2 = pd.read_csv('datasets/csv_output_etanol_GO.csv', delimiter=';')

data1 = []
data2 = []
n_steps = 2

# Extração do preço do combustível em um vetor 1-dimensional
for i in range(dataset1.shape[0]):
    data1.append(dataset1.loc[i]['precovenda'])
    data2.append(dataset2.loc[i]['precovenda'])

# Conversão para numpy array
datas = np.array([data1])
datas_extra = np.array([data2])

# Transformando a série temporal no dataset de treino utilizando uma janela de tamanho n_steps + 1
ht = HorizonTransformer(horizon=n_steps+1)
datas = ht.fit_transform(datas.reshape(-1, 1))
datas_extra = ht.fit_transform(datas_extra.reshape(-1, 1))

# Eliminação dos exemplos com valores NaN
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp = imp.fit(datas)
datas = imp.transform(datas)
datas_extra = imp.transform(datas_extra)

y = datas[:,-1]
X = datas[:, [0, 1]]

y_extra = datas_extra[:,-1]
X_extra = datas_extra[:, [0, 1]]

# Cria o modelo
model = Sequential()
model.add(Dense(100, activation='relu', input_dim=n_steps))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# Inicia o KFold Cross Validation
kf = KFold(n_splits=5)
kf.get_n_splits(X)

r2_scores = []
mae_scores = []
mse_scores = []

for train_index, test_index in kf.split(X):
        
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    # Adicionando a outra série temporal
    X_test = np.concatenate((X_test, X_extra)) 
    y_test = np.concatenate((y_test, y_extra)) 

    model.fit(X_train, y_train, epochs=200, verbose=0)
    y_pred = model.predict(X_test, verbose=0)
    
    # Coleta das métricas
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    
    r2_scores.append(r2)
    mae_scores.append(mae)
    mse_scores.append(mse)

    print("\n=============ITERATION SCORES=============\n")

    print('R-squared: %.3f' % r2)
    print('Mean Absolute Error: %.3f' % mae)
    print('Mean Square Error: %.3f' % mse)

# Convertento métricas para numpy para pegar a média dos valores
r2_scores = np.array(r2_scores)
mae_scores = np.array(mae_scores)
mse_scores = np.array(mse_scores)

print("\n=============FINAL SCORES=============\n")
print("R-squared: %f" % (r2_scores.sum()/r2_scores.size))
print("Mean Absolute Error: %f" % (mae_scores.sum()/mae_scores.size))
print("Mean Square Error: %f" % (mse_scores.sum()/mse_scores.size))

end = time.time()
print("\n=============TIME=============\n")
print("It took: %.2f seconds" % (end - start))
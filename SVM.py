# データの読み込み
import pandas as pd
import numpy as np
df = pd.read_csv('All-Results\\All_Results.csv',delimiter=',')

X = df.iloc[:,1:].values

X_new = []
for i in range(1,601):
    n = 60*(i-1)
    m = 60*i
    X_new.append(np.reshape(X[n:m],(1,5940))[0].tolist())
X_new = np.array(X_new)
X = X_new

y = np.zeros((600))
for i in range(150):
    y[i] = 0
for i in range(150,300):
    y[i] = 1
for i in range(300,450):
    y[i] = 2
for i in range(450,600):
    y[i] = 3
    
# NaNを中央値で埋める
from sklearn.preprocessing import Imputer
missing_value_to_median = Imputer(strategy='median')
missing_value_to_median.fit(X)
X_median = missing_value_to_median.transform(X)

# 学習アルゴリズム
from sklearn.svm import SVC
# パイプライン
from sklearn.pipeline import Pipeline
# 正規化
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
svm = SVC(C=100,gamma=0.1,kernel = 'rbf')

from sklearn.model_selection import StratifiedShuffleSplit
ss = StratifiedShuffleSplit(n_splits=10,   
                            train_size=0.8,
                            test_size =0.2,  
                            random_state=0)  


accs = []
for train_index, test_index in ss.split(X_median,y): 
    
    X_train, X_test = X_median[train_index], X_median[test_index] 
    y_train, y_test = y[train_index], y[test_index] 
    
    X_train_new = []
    for i in range(480):
        X_train_new.append(np.reshape(X_train[i],(60,99)).tolist())
    X_train_new = np.array(X_train_new).reshape(28800,99)
    
    y_train_new = np.zeros(28800)
    for i in range(480):
        y_train_new[60*i:60*(i+1)] = y_train[i]
        
    X_test_new = []
    for i in range(120):
        X_test_new.append(np.reshape(X_test[i],(60,99)).tolist())
    X_test_new = np.array(X_test_new).reshape(7200,99)
    
    y_test_new = np.zeros(7200)
    for i in range(120):
        y_test_new[60*i:60*(i+1)] = y_test[i]
        
        
    X_train_new = mms.fit_transform(X_train_new)
    X_test_new= mms.transform(X_test_new)
    svm.fit(X_train_new, y_train_new)         
    preds = svm.decision_function(X_test_new)
    preds_mean = np.zeros((120,4))
    for i in range(120):
        preds_bop_mean = np.mean(preds[60*i:60*(i+1),0])
        preds_cool_mean = np.mean(preds[60*i:60*(i+1),1])
        preds_hard_mean = np.mean(preds[60*i:60*(i+1),2])
        preds_post_mean = np.mean(preds[60*i:60*(i+1),3])
        preds_mean[i,0] = preds_bop_mean 
        preds_mean[i,1] = preds_cool_mean 
        preds_mean[i,2] = preds_hard_mean 
        preds_mean[i,3] = preds_post_mean 
        
    m = 0
    for i in range(120):
        if np.argmax(preds_mean[i]) == y_test[i]:
            m += 1
            acc = m/120
    print(acc)
    
accs = np.array(accs)
print(accs.mean())
print(accs.std())
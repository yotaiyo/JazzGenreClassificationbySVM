import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import RandomizedSearchCV

#データの読み込み
df = pd.read_csv('All_Results\\All_Results.csv',delimiter=',')
X = df.iloc[:,1:].values

#クラスラベルを作成
y = np.zeros((36000))
for i in range(9000):
    y[i] = 0
for i in range(9000,18000):
    y[i] = 1
for i in range(18000,27000):
    y[i] = 2
for i in range(27000,36000):
    y[i] = 3
    
#NaNを中央値で埋める
from sklearn.preprocessing import Imputer
missing_value_to_median = Imputer(strategy='median')
missing_value_to_median.fit(X)
X_median = missing_value_to_median.transform(X)

#8:2 Shuffle
ss = StratifiedShuffleSplit(n_splits=1, 
                  train_size=0.8, 
                  test_size=0.2, 
                  random_state=0)
train_index, test_index = next(ss.split(X_median, y))
X_train_median, X_test_median = X_median[train_index], X_median[test_index]
y_train_median, y_test_median = y[train_index], y[test_index]

#RandomizedSearchCV
pipe = Pipeline([('scl', MinMaxScaler()),
                 ('clf', SVC())])

param_range = [0.1,1,10,100,1000]
param_range2 = [0.01,0.1,1.0,10,100]

param_grid = {'clf__C': param_range, 
              'clf__gamma' : param_range2,
              'clf__kernel': ['rbf']}

gs = RandomizedSearchCV(pipe, 
                        param_grid,  
                        cv=5,
                        n_iter=12)

gs = gs.fit(X_train_median,y_train_median)
print(gs.best_score_)
print(gs.best_params_)

#最も良かったパラメータの組み合わせでトレーニング&評価
ss = StratifiedShuffleSplit(n_splits=10,   
                            train_size=0.8,  
                            test_size =0.2,  
                            random_state=0)  

scores = []
for train_index, test_index in ss.split(X_median,y): 
    
    X_train, X_test = X_median[train_index], X_median[test_index] 
    y_train, y_test = y[train_index], y[test_index] 

    clf = gs.best_estimator_
    clf.fit(X_train, y_train)       
    score = clf.score(X_test, y_test)
    scores.append(score)

scores = np.array(scores)
print(scores)
print(scores.mean())
print(scores.std())
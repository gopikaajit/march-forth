#!/usr/bin/python3.5m

import pandas as pd
import sklearn
import warnings
warnings.filterwarnings('ignore')



meta_data = pd.read_csv('PS_20174392719_1491204439457_log.csv')
del meta_data['nameDest']
del meta_data['nameOrig']

del meta_data['isFlaggedFraud']
print('\nNumber of transactions:-',len(meta_data))



R = meta_data.loc[(meta_data.type == 'TRANSFER') | (meta_data.type == 'CASH_OUT')]
print('\nNumber of transactions after narrowing the search to transfer and cash_out:-',len(R))
Cols = R[['step','amount','oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest']]
y = R['isFraud']
X = Cols

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 

 

from sklearn import linear_model
logitic = linear_model.LogisticRegression()
model = logitic.fit(X_train,y_train)
predictions = model.predict(X_test)
print('\nclassification report:-\n',sklearn.metrics.classification_report(y_test,predictions))

arr = sklearn.metrics.confusion_matrix(y_test, predictions)
print(arr)
print('Test accuracy of logistic regression:-\n',sklearn.metrics.accuracy_score(y_test,predictions))

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
model = gnb.fit(X_train,y_train)
predictions = model.predict(X_test)
print('classification report:-',sklearn.metrics.classification_report(y_test,predictions))
print('confusion_matrix:-',sklearn.metrics.confusion_matrix(y_test, predictions))
print('Test accuracy of naive bayes algoritm is:-',sklearn.metrics.accuracy_score(y_test,predictions))





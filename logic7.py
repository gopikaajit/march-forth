#!/usr/bin/python3.5m
import plotly
import seaborn as sns
import pandas as pd
import sklearn
import warnings
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

meta_data = pd.read_csv('PS_20174392719_1491204439457_log.csv')                                        #to read the.csv file
meta_data = meta_data.rename(columns={'oldbalanceOrg':'oldBalanceOrig', 'newbalanceOrig':'newBalanceOrig', \
                        'oldbalanceDest':'oldBalanceDest', 'newbalanceDest':'newBalanceDest'})
print('\nNumber of transactions:-',len(meta_data))

X = meta_data.loc[(meta_data.type == 'TRANSFER') | (meta_data.type == 'CASH_OUT')]                                          #data cleaning part
print('\nNumber of transactions after narrowing the search to transfer and cash_out:-',len(X))   
randomState = 5
np.random.seed(randomState)      


y = X['isFraud']
del X['isFraud']

X = X.drop(['nameOrig', 'nameDest', 'isFlaggedFraud'], axis = 1)


X.loc[X.type == 'TRANSFER', 'type'] = 0
X.loc[X.type == 'CASH_OUT', 'type'] = 1
X.type = X.type.astype(int)
X.loc[(X.oldBalanceDest == 0) & (X.newBalanceDest == 0) & (X.amount != 0), \
      ['oldBalanceDest', 'newBalanceDest']] = - 1
X.loc[(X.oldBalanceOrig == 0) & (X.newBalanceOrig == 0) & (X.amount != 0), \
      ['oldBalanceOrig', 'newBalanceOrig']] = - 2
X['errorBalanceOrig'] = X.newBalanceOrig + X.amount - X.oldBalanceOrig
X['errorBalanceDest'] = X.oldBalanceDest + X.amount - X.newBalanceDest

from sklearn.model_selection import StratifiedShuffleSplit
sss = sklearn.model_selection.StratifiedShuffleSplit(n_splits=100, test_size=0.5, random_state=42)     #splitting dataset
for train_index, test_index in sss.split(X, y):
	X_train, X_test= X.iloc[train_index], X.iloc[test_index]
	y_train, y_test = y.iloc[train_index], y.iloc[test_index]


from sklearn import linear_model
logitic = linear_model.LogisticRegression(solver = 'sag')                                                            #
model = logitic.fit(X_train,y_train)                                                                   #
predictions = model.predict(X_test)                                                                    #
print('\nclassification report:-\n',sklearn.metrics.classification_report(y_test,predictions))         #machine learning part

arr = sklearn.metrics.confusion_matrix(y_test, predictions)                                            #
print(arr)
print('Test accuracy of logistic regression:-\n',sklearn.metrics.accuracy_score(y_test,predictions))   #

from sklearn.ensemble import GradientBoostingClassifier
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1)
model=clf.fit(X_train, y_train)
predictions = model.predict(X_test)
print('classification report:-\n',sklearn.metrics.classification_report(y_test,predictions))
print('confusion_matrix:-\n',sklearn.metrics.confusion_matrix(y_test, predictions))
print('Test accuracy of gradient boosting classifier is:-\n',sklearn.metrics.accuracy_score(y_test,predictions))

Xfraud = X.loc[y == 1]    
XnonFraud = X.loc[y == 0]
                  
correlationNonFraud = XnonFraud.loc[:, X.columns != 'step'].corr()
mask = np.zeros_like(correlationNonFraud)
indices = np.triu_indices_from(correlationNonFraud)
mask[indices] = True

grid_kws = {"width_ratios": (.9, .9, .05), "wspace": 0.2}
f, (ax1, ax2, cbar_ax) = plt.subplots(1, 3, gridspec_kw=grid_kws, \
                                     figsize = (14, 9))

cmap = sns.diverging_palette(220, 8, as_cmap=True)
ax1 =sns.heatmap(correlationNonFraud, ax = ax1, vmin = -1, vmax = 1, \
    cmap = cmap, square = False, linewidths = 0.5, mask = mask, cbar = False)
ax1.set_xticklabels(ax1.get_xticklabels(), size = 16); 
ax1.set_yticklabels(ax1.get_yticklabels(), size = 16); 
ax1.set_title('Genuine \n transactions', size = 20)

correlationFraud = Xfraud.loc[:, X.columns != 'step'].corr()
ax2 = sns.heatmap(correlationFraud, vmin = -1, vmax = 1, cmap = cmap, \
 ax = ax2, square = False, linewidths = 0.5, mask = mask, yticklabels = False, \
    cbar_ax = cbar_ax, cbar_kws={'orientation': 'vertical', \
                                 'ticks': [-1, -0.5, 0, 0.5, 1]})
ax2.set_xticklabels(ax2.get_xticklabels(), size = 16); 
ax2.set_title('Fraudulent \n transactions', size = 20);

cbar_ax.set_yticklabels(cbar_ax.get_yticklabels(), size = 14);

plt.show()

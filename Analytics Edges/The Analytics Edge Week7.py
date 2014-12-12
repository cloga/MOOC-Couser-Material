# The Analytics Edge Week7

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, ward_tree, Ward
from sklearn import metrics

train = pd.read_csv('train.csv')
exclude = ['UserID', 'Happy']
columns = [c for c in train.columns if c not in exclude]
x_train = train[columns].fillna(-1)

from sklearn.feature_extraction import DictVectorizer
v = DictVectorizer()
X = v.fit_transform(x_train.to_dict(outtype='records')).toarray()
y = train['Happy'].values

from sklearn.cross_validation import train_test_split
data_train, data_test, target_train, target_test = train_test_split(X, y)



from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import datetime
estimators = {}
estimators['bayes'] = GaussianNB()
estimators['tree'] = tree.DecisionTreeClassifier()
estimators['forest_100'] = RandomForestClassifier(n_estimators = 100)
estimators['forest_10'] = RandomForestClassifier(n_estimators = 10)
estimators['svm_c_rbf'] = svm.SVC()
estimators['svm_c_linear'] = svm.SVC(kernel='linear')
estimators['svm_linear'] = svm.LinearSVC()
estimators['svm_nusvc'] = svm.NuSVC()
estimators['KNN'] = KNeighborsClassifier()
estimators['LR'] = LogisticRegression()

for k in estimators.keys():
    start_time = datetime.datetime.now()
    print '----%s----' % k
    estimators[k] = estimators[k].fit(data_train, target_train)
    pred = estimators[k].predict(data_test)
    print("%s Score: %0.2f" % (k, estimators[k].score(data_test, target_test)))
    scores = cross_validation.cross_val_score(estimators[k], data_test, target_test, cv=5)
    print("%s Cross Avg. Score: %0.2f (+/- %0.2f)" % (k, scores.mean(), scores.std() * 2))
    end_time = datetime.datetime.now()
    time_spend = end_time - start_time
    print("%s Time: %0.2f" % (k, time_spend.total_seconds()))

test = pd.read_csv('test.csv')
x_test = test[columns].fillna(-1)
data_test = v.transform(x_test.to_dict(outtype='records')).toarray()
target_test = test['Happy'].values
pred = estimators[k].predict(data_test)
from sklearn.svm import SVC
from sklearn.datasets import load_iris, load_digits, fetch_openml
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, LabelBinarizer, KBinsDiscretizer, Binarizer
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import check_random_state
from dl85 import DL85Booster, DL85Classifier, BOOST_SVM2
from sklearn.metrics import silhouette_score as sc
import xgboost as xgb
import time
import numpy as np
import pandas as pd
import sys

# dataset = load_digits(2)
# X = dataset.data
# y = dataset.target
# print(X.shape)
# print(y.shape)
# enc = KBinsDiscretizer(n_bins=2, encode='ordinal', strategy='uniform')
# X = enc.fit_transform(X)
# enc = OneHotEncoder(sparse=False, handle_unknown='ignore')
# X = enc.fit_transform(X)


# X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
# random_state = check_random_state(0)
# permutation = random_state.permutation(X.shape[0])
# X = X[permutation]
# y = y[permutation]
# X = X.reshape((X.shape[0], -1))
# X = X.astype('int32')
# y = y.astype('int32')
# print(X.shape)
# print(y.shape)
# print(X[0, :])
# sys.exit(0)


# train = np.genfromtxt("../datasets/mnist_train.csv", delimiter=",")
# test = np.genfromtxt("../datasets/mnist_test.csv", delimiter=",")
# data = np.concatenate((train, test))
# X = data[:, 1:]
# y = data[:, 0]
# enc = KBinsDiscretizer(n_bins=2, encode='ordinal', strategy='uniform')
# X = enc.fit_transform(X)
# enc = OneHotEncoder(sparse=False, handle_unknown='ignore')
# X = enc.fit_transform(X)
# print(X.shape)
# print(y.shape)
# # print(X[0, :])
# sys.exit(0)


train = np.genfromtxt("../datasets/mnist_train.csv", delimiter=",")
test = np.genfromtxt("../datasets/mnist_test.csv", delimiter=",")
# data = np.concatenate((train, test))
X_train, y_train = train[:, 1:], train[:, 0]
X_test, y_test = test[:, 1:], test[:, 0]
enc = Binarizer(threshold=10)
X_train = enc.fit_transform(X_train)
X_test = enc.fit_transform(X_test)
# enc = LabelBinarizer()
# y_train = enc.fit_transform(y_train)[:, 0]
# y_test = enc.transform(y_test)[:, 0]
enc = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
y_train = enc.fit_transform(y_train.reshape(y_train.shape[0], 1))
y_test = enc.transform(y_test.reshape(y_test.shape[0], 1))
X_train, y_train = X_train.astype('int32'), y_train.astype('int32')
X_test, y_test = X_test.astype('int32'), y_test.astype('int32')
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)
y_train = y_train.ravel()
y_test = y_test.ravel()
print(y_train.shape, y_test.shape)
# print(X_train[0, :])
print(set(y_train), set(y_test))
# sys.exit(0)


# X_train = np.load("../datasets/binary-mnist/original_28x28/binary_digits_binary_pixels/x_train.npy", allow_pickle=True)
# y_train = np.load("../datasets/binary-mnist/original_28x28/binary_digits_binary_pixels/y_train.npy", allow_pickle=False)
# X_test = np.load("../datasets/binary-mnist/original_28x28/binary_digits_binary_pixels/x_test.npy", allow_pickle=True)
# y_test = np.load("../datasets/binary-mnist/original_28x28/binary_digits_binary_pixels/y_test.npy", allow_pickle=True)
# print(X_train.shape, y_train.shape)
# print(X_test.shape, y_test.shape)
# print(set(y_train))
# X = np.concatenate((X_train, X_test))
# y = np.concatenate((y_train, y_test))
# print(X_train[0, :])
# print(set(y_train))
# sys.exit(0)


# X = np.load("../datasets/binary-mnist/binarized_mnist.npz", allow_pickle=True)
# lst = X.files
# for item in lst:
#     print(item)
#     # print(X[item])
# print(X['train_data'].shape)
# print(X['train_length'])
# print(X['valid_length'])
# print(type(X))
# print(X.f)
# print(set(X['train_data'][:, -1]))
# sys.exit(0)


# data = pd.read_csv("../datasets/matchmaker.csv", delimiter=",", header=None)
# for col in [1, 2, 3, 4, 6, 7, 8, 9]:
#     data[col] = data[col].astype('category')
# cat_columns = data.select_dtypes(['category']).columns
# data[cat_columns] = data[cat_columns].apply(lambda x: x.cat.codes)
# dataset = data.to_numpy()
# X = dataset[:, :-1]
# y = dataset[:, -1]
# enc = KBinsDiscretizer(n_bins=8, encode='ordinal', strategy='uniform')
# X = enc.fit_transform(X)
# enc = OneHotEncoder(sparse=False, handle_unknown='ignore')
# X = enc.fit_transform(X)
# enc = LabelBinarizer()
# y = enc.fit_transform(y)
# y = y.ravel()
# np.savetxt("../datasets/matchmake.txt", np.concatenate((y.reshape(X.shape[0], 1), X), axis=1), fmt="%d", delimiter=" ")

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# X_train = X_train.astype('int32')
# y_train = y_train.astype('int32')
# print(X_train.shape)
# print(X.shape)


# print()
# print("lpdl8 d1")
# parameters = {'regulator': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 10, 100, 1000, 10000, 100000, 1000000]}
# grid = GridSearchCV(estimator=DL85Booster(max_depth=1, min_sup=1, time_limit=600, max_estimators=0, model=BOOST_SVM2),
#                     param_grid=parameters, scoring='accuracy', cv=4, n_jobs=1, verbose=10)
# grid.fit(X_train, y_train)
# print(grid.best_estimator_)
# y_pred = grid.predict(X_test)
# print("train_fold:", accuracy_score(y_train, grid.predict(X_train)), "test_fold:", accuracy_score(y_test, y_pred))
# # print(grid.cv_results_)
# print()
#
#
# print("lpdl8 d2")
# parameters = {'regulator': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 10, 100, 1000, 10000, 100000, 1000000]}
# grid = GridSearchCV(estimator=DL85Booster(max_depth=2, min_sup=1, time_limit=600, max_estimators=0, model=BOOST_SVM2),
#                     param_grid=parameters, scoring='accuracy', cv=4, n_jobs=-1, verbose=10)
# # GridSearchCV(SVC(), param_grid_poly, refit=True, verbose=0, cv=4)
# grid.fit(X_train, y_train)
# print(grid.best_estimator_)
# y_pred = grid.predict(X_test)
# print("train_fold:", accuracy_score(y_train, grid.predict(X_train)), "test_fold:", accuracy_score(y_test, y_pred))
# # print(grid.cv_results_)


# print("SVM linear")
# param_grid_linear = {'C': [0.1, 1, 10, 100, 1000], 'kernel': ['linear']}
# grid = GridSearchCV(SVC(max_iter=1000), param_grid_linear, refit=True, verbose=10, cv=4, scoring='accuracy', n_jobs=1)
# grid.fit(X_train, y_train)
# print(grid.best_estimator_)
# y_pred = grid.predict(X_test)
# print("train_fold:", accuracy_score(y_train, grid.predict(X_train)), "test_fold:", accuracy_score(y_test, y_pred))
# # print(grid.cv_results_)
#
#
# print()
# print("SVM non-linear")
# best_train, best_test = [], []
# param_grid_poly = {'C': [0.1, 1, 10, 100, 1000], 'kernel': ['poly', 'rbf'], 'gamma': [1, 0.1, 0.01, 0.001, 0.0001], 'degree': [2, 3, 4]}
# grid = GridSearchCV(SVC(max_iter=1000), param_grid_poly, refit=True, verbose=10, cv=4, scoring='accuracy', n_jobs=1)
# grid.fit(X_train, y_train)
# print(grid.best_estimator_)
# y_pred = grid.predict(X_test)
# print("train_fold:", accuracy_score(y_train, grid.predict(X_train)), "test_fold:", accuracy_score(y_test, y_pred))
# # print(grid.cv_results_)


print()
print("AdaBoost linear")
param_grid_ada = {'n_estimators': [50, 100, 1000]}
grid = GridSearchCV(estimator=AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=1)), param_grid=param_grid_ada, refit=True, verbose=10, cv=4, scoring='accuracy', n_jobs=1)
grid.fit(X_train, y_train)
print(grid.best_estimator_)
y_pred = grid.predict(X_test)
print("train_fold:", accuracy_score(y_train, grid.predict(X_train)), "test_fold:", accuracy_score(y_test, y_pred))
# print(grid.cv_results_)


print()
print("AdaBoost non-linear")
param_grid_ada = {'base_estimator': [DecisionTreeClassifier(max_depth=2), DecisionTreeClassifier(max_depth=3)], 'n_estimators': [50, 100, 1000]}
grid = GridSearchCV(estimator=AdaBoostClassifier(), param_grid=param_grid_ada, refit=True, verbose=10, cv=4, scoring='accuracy', n_jobs=1)
grid.fit(X_train, y_train)
print(grid.best_estimator_)
y_pred = grid.predict(X_test)
print("train_fold:", accuracy_score(y_train, grid.predict(X_train)), "test_fold:", accuracy_score(y_test, y_pred))
# print(grid.cv_results_)


print()
print("XGBoost linear")
param_grid_xgb = {'n_estimators': [50, 100, 1000], 'objective': ['binary:logistic', 'binary:logitraw']}
grid = GridSearchCV(estimator=xgb.XGBClassifier(max_depth=1), param_grid=param_grid_xgb, refit=True, verbose=10, cv=4, scoring='accuracy', n_jobs=1)
grid.fit(X_train, y_train)
print(grid.best_estimator_)
y_pred = grid.predict(X_test)
print("train_fold:", accuracy_score(y_train, grid.predict(X_train)), "test_fold:", accuracy_score(y_test, y_pred))
# print(grid.cv_results_)


print()
print("XGBoost non-linear")
param_grid_xgb = {'max_depth': [2, 3], 'n_estimators': [50, 100, 1000], 'objective': ['binary:logistic', 'binary:logitraw']}
grid = GridSearchCV(estimator=xgb.XGBClassifier(), param_grid=param_grid_xgb, refit=True, verbose=10, cv=4, scoring='accuracy', n_jobs=1)
grid.fit(X_train, y_train)
print(grid.best_estimator_)
y_pred = grid.predict(X_test)
print("train_fold:", accuracy_score(y_train, grid.predict(X_train)), "test_fold:", accuracy_score(y_test, y_pred))
# print(grid.cv_results_)


# print()
# print("lpdl8 d1")
# best_train, best_test = [], []
# parameters = {'regulator': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 10, 100, 1000, 10000, 100000, 1000000]}
# kf = StratifiedKFold(n_splits=5)
# for train_index, test_index in kf.split(X, y):
#     X_train, y_train, X_test, y_test = X[train_index], y[train_index], X[test_index], y[test_index]
#     grid = GridSearchCV(estimator=DL85Booster(max_depth=1, min_sup=1, time_limit=180, max_estimators=0, model=BOOST_SVM2),
#                         param_grid=parameters, scoring='accuracy', cv=4, n_jobs=-1, verbose=0)
#     # GridSearchCV(SVC(), param_grid_poly, refit=True, verbose=0, cv=4)
#     grid.fit(X_train, y_train)
#     print(grid.best_estimator_)
#     y_pred = grid.predict(X_test)
#     best_train.append(accuracy_score(y_train, grid.predict(X_train)))
#     best_test.append(accuracy_score(y_test, y_pred))
#     print("train_fold:", best_train[-1], "test_fold:", best_test[-1])
#     # print(grid.cv_results_)
# print()
# print("train:", best_train, np.mean(best_train))
# print("test:", best_test, np.mean(best_test))
#
#
# print("lpdl8 d2")
# best_train, best_test = [], []
# parameters = {'regulator': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 10, 100, 1000, 10000, 100000, 1000000]}
# kf = StratifiedKFold(n_splits=5)
# for train_index, test_index in kf.split(X, y):
#     X_train, y_train, X_test, y_test = X[train_index], y[train_index], X[test_index], y[test_index]
#     grid = GridSearchCV(estimator=DL85Booster(max_depth=2, min_sup=1, time_limit=180, max_estimators=0, model=BOOST_SVM2),
#                         param_grid=parameters, scoring='accuracy', cv=4, n_jobs=-1, verbose=0)
#     # GridSearchCV(SVC(), param_grid_poly, refit=True, verbose=0, cv=4)
#     grid.fit(X_train, y_train)
#     print(grid.best_estimator_)
#     y_pred = grid.predict(X_test)
#     best_train.append(accuracy_score(y_train, grid.predict(X_train)))
#     best_test.append(accuracy_score(y_test, y_pred))
#     print("train_fold:", best_train[-1], "test_fold:", best_test[-1])
#     # print(grid.cv_results_)
# print()
# print("train:", best_train, np.mean(best_train))
# print("test:", best_test, np.mean(best_test))


# clf_results = cross_validate(estimator=AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=1), n_estimators=100), X=X, y=y, scoring='accuracy', cv=5, n_jobs=-1, verbose=0, return_train_score=True, return_estimator=True, error_score=np.nan)
# print("train:", clf_results['train_score'], np.mean(clf_results['train_score']))
# print("test:", clf_results['test_score'], np.mean(clf_results['test_score']))
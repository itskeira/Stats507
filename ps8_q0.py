#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Stats 507, Fall 2021
#
# Author: Han Qiu
# Date: December 12, 2021
# 79: -------------------------------------------------------------------------

# imports: --------------------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from numpy import mean

import warnings
warnings.filterwarnings("ignore")

## Question 0 - Slurm
df = pd.read_csv("~/itskeira/Stats507/train.csv")
df[['material']] = df_u[['material']]
df = df.drop_duplicates(subset=['material'])
df_u = pd.read_csv("~/itskeira/Stats507/unique_m.csv")
u_df = df_u.drop_duplicates(subset=['material'])

# +
# 80% training dataset with 20% testing set
x_train1, x_test1, y_train1, y_test1 = train_test_split(u_df, u_df, test_size = 0.2)

# 10% testing set with 10% validation set
x_val1, x_test1, y_val1, y_test1 = train_test_split(x_test1, y_test1, test_size = 0.5)
# -

x_train = pd.merge(df, x_train1.iloc[:,-1:], on='material')
y_train = x_train[['critical_temp']]
x_train.drop(['material', 'critical_temp'], axis=1, inplace=True)

x_test = pd.merge(df, x_test1.iloc[:,-1:], on='material')
y_test = x_test[['critical_temp']]
x_test.drop(['material', 'critical_temp'], axis=1, inplace=True)

x_val = pd.merge(df, x_val1.iloc[:,-1:], on='material')
y_val = x_val[['critical_temp']]
x_val.drop(['material', 'critical_temp'], axis=1, inplace=True)

# +
# random forest model
val_rf = RandomForestRegressor(max_depth=30, 
                               n_estimators=110, 
                               random_state=1)

cv = KFold(n_splits=10, random_state=1, shuffle=True)
scores = cross_val_score(val_rf, x_test, y_test, scoring='neg_mean_squared_error', cv=cv, n_jobs=5)
print("Random Forest MSE: ", mean(abs(scores)))

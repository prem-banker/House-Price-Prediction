#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import array
import matplotlib.pyplot as plt

dataset = pd.read_csv("data_hackathon_pdpu.csv")
#dataset = dataset.drop('ATM',axis=1)
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,18].values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelEncoder_X0 = LabelEncoder()
labelEncoder_X2 = LabelEncoder()
labelEncoder_X17 = LabelEncoder()
X[:, 0] = labelEncoder_X0.fit_transform(X[:, 0])
X[:,17] = labelEncoder_X17.fit_transform(X[:, 17])
X[:,2] = labelEncoder_X17.fit_transform(X[:, 2])


oneHotEncoder =OneHotEncoder(categorical_features=[0,2,17], handle_unknown='ignore')
oneHotEncoder.fit(X)
oneHotEncoder.categories_
X_t = oneHotEncoder.transform(X).toarray()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_t, y, test_size = 0.2, random_state = 0)
y_t = y_test

from sklearn.ensemble import RandomForestRegressor
rfr_regressor = RandomForestRegressor(n_estimators=800,random_state=0)
rfr_regressor.fit(X_train,y_train)
y_pred_rfr = rfr_regressor.predict(X_test)

rfr_regressor.score(X_test,y_test)
print(rfr_regressor.score(X_test,y_test))



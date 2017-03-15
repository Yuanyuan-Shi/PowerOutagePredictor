#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: Yuanyuan Shi

"""
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error

# Power outage class
def f(row):
    """function that categories days with more than 8 outages as extreme, 
                                3-8 outages as bad, and 0-2 as normal"""
    if row['Total_outages'] > 8:
        val = 2
    elif row['Total_outages'] > 2:
        val = 1
    else:
        val = 0
    return val

# Load data function: load data for neural network training
# Input: None
# Output: x_train, y_train, x_test, y_test
def load_data():   
    data = pd.read_csv('../../Data/WeatherOutagesAllJerry.csv')
    data = data.dropna(how = 'all')
    data['category'] = data.apply(f, axis=1)
    data.head()

    # Seperate training and testing dataset
    train,test=train_test_split(data,test_size=0.1,random_state=567)
    x_train = train[['Day_length_hr','Avg_Temp_F','Avg_humidity_percent','Avg_windspeed_mph','Max_windspeed_mph',
                 'Precipitation_in','Event_thunderstorm']]
    y_train = train['category']

    x_test = test[['Day_length_hr','Avg_Temp_F','Avg_humidity_percent','Avg_windspeed_mph','Max_windspeed_mph',
                 'Precipitation_in','Event_thunderstorm']]
    y_test = test['category']

    # data normalization
    x_train = preprocessing.normalize(x_train) # training dataset
    x_test = preprocessing.normalize(x_test) #testing dataset
    return x_train, y_train, x_test, y_test

# Oversample algoritm
# This function oversample from under-reprented class
# Input: X-feature, y-response, R1-oversample ratio for bad case, R2-oversample ratio for extreme case
# Output: X_resam, y_resam
def balance_sample(X, y, R1, R2):
    from imblearn.over_sampling import RandomOverSampler 
    # Apply the random over-sampling
    ros = RandomOverSampler(ratio=R1,random_state=6)
    x_res, y_res = ros.fit_sample(X[y!=2], y[y!=2])
    ros2 = RandomOverSampler(ratio=R2,random_state=6)
    x_res2, y_res2 = ros2.fit_sample(X[y!=1], y[y!=1])

    X_resam = np.concatenate((x_res,x_res2[y_res2==2]), axis=0)
    y_resam = np.concatenate((y_res, y_res2[y_res2==2]),axis=0)
    return X_resam, y_resam
  

def neural_network_clf(x_train, y_train, x_test, y_test):
    clf = MLPClassifier(max_iter=1000,activation='identity', solver='lbfgs', 
                        alpha=1e-5,hidden_layer_sizes=(5, 3), random_state=1)
    clf.fit(x_train, y_train) 
    y_train_pred = clf.predict(x_train)
    y_test_pred = clf.predict(x_test)

    print("Train error for normalized data",mean_squared_error(y_train,y_train_pred))
    print("Test error for normalized data",mean_squared_error(y_test,y_test_pred))
    
    



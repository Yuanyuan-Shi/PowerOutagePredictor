#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:31:39 2017

@author: Yuanyuan Shi

"""
import nn_sandbox as nn


# Load data function: load data for neural network training
# Input: None
# Output: x_train, y_train, x_test, y_test
def test_load_data():   
    x_train, y_train, x_test, y_test = nn.load_data()
    assert (not x_train.empty), "Function load_data not works properly!"
    print("Pass test_load_data()")


# Oversample algoritm
# This function oversample from under-reprented class
# Input: X-feature, y-response, R1-oversample ratio for bad case, R2-oversample ratio for extreme case
# Output: X_resam, y_resam
def test_balance_sample():
    x_train, y_train, x_test, y_test = nn.load_data()
    # Apply the random over-sampling
    x_train, y_train = nn.balance_sample(x_train, y_train, 0.3, 0.3)
    N2 = len(y_train[y_train==2])
    N0 = len(y_train[y_train==0])
    assert (N2*1.0/N0>0.25), "Function balance_sample not works properly!"
    print("Pass test_balance_sample()")
    
  
def test_neural_network_clf():
    x_train, y_train, x_test, y_test = nn.load_data()
    # Apply the random over-sampling
    x_train, y_train = nn.balance_sample(x_train, y_train, 0.3, 0.3)
    nn.neural_network_clf(x_train, y_train, x_test, y_test)
    print("Pass test_neural_network_clf()")
    




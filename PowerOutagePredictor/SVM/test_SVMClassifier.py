from SVM.SVMClassifier import *
import numpy as np
from sklearn.externals import joblib
from nose.tools import with_setup
import math

# Setup
scaler = joblib.load("scaler.pkl")
zero = np.array([[12,70,80,8,5,10,0.]])
one = np.array([[9,50,70,20,15,30,0.5]])
two = np.array([[8,30,60,50,30,50,0.5]])

zero = zero.reshape(1, -1)
one = one.reshape(1, -1)
two = two.reshape(1, -1)

"""
Test probability outputs of model.
"""
def test_predictOutageProba():
    zeroPredict = predictOutageProba(zero)
    assert math.isclose(0.96614198, zeroPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.03266029, zeroPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.00119773, zeroPredict[0,2], rel_tol=1e-05)

    onePredict = predictOutageProba(one)
    assert math.isclose(0.88164684, onePredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.11012898, onePredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.00822418, onePredict[0,2], rel_tol=1e-05)

    twoPredict = predictOutageProba(two)
    assert math.isclose(0.04806885, twoPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.3045513, twoPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.64737985, twoPredict[0,2], rel_tol=1e-05)

"""
Test classification outputs of model
"""
def test_predictOutage():
    assert predictOutage(zero) == 0
    assert predictOutage(one) == 1
    assert predictOutage(two) == 2
    return

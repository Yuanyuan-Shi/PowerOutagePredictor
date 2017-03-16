import math
import numpy as np
import pandas as pd
from TreeClassifier import *
from sklearn.externals import joblib

# Create test data
weather0 = pd.DataFrame()
weather1 = pd.DataFrame()
weather2 = pd.DataFrame()
weather0 = weather0.append({"Day_length_hr": 12, 
                "Avg_Temp_F": 70,
                "Avg_humidity_percent": 80,
                "Max_windspeed_mph": 8,
                "Avg_windspeed_mph": 5,
                "Max_windgust_mph": 10,
                "Precipitation_in": 0.1},
                ignore_index=True)
weather1 = weather1.append({"Day_length_hr": 10, 
                "Avg_Temp_F": 50,
                "Avg_humidity_percent": 70,
                "Max_windspeed_mph": 30,
                "Avg_windspeed_mph": 15,
                "Max_windgust_mph": 30,
                "Precipitation_in": 0.5},
                ignore_index=True)
weather2 = weather2.append({"Day_length_hr": 8, 
                "Avg_Temp_F": 30,
                "Avg_humidity_percent": 60,
                "Max_windspeed_mph": 50,
                "Avg_windspeed_mph": 30,
                "Max_windgust_mph": 50,
                "Precipitation_in": 0.5},
                ignore_index=True)


def test_predictOutageProba_dt():
    """Test probability outputs of the model"""
    # decision tree
    zeroPredict = predictOutageProba(weather0,'dt')
    assert math.isclose(0.40800982, zeroPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.33279156, zeroPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.25919863, zeroPredict[0,2], rel_tol=1e-05)

    onePredict = predictOutageProba(weather1,'dt')
    assert math.isclose(0.03327038, onePredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.15051901, onePredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.81621062, onePredict[0,2], rel_tol=1e-05)

    twoPredict = predictOutageProba(weather2,'dt')
    assert math.isclose(0.03327038, twoPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.15051901, twoPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.81621062, twoPredict[0,2], rel_tol=1e-05)
    
    return


def test_predictOutageProba_rf():
    # random forest
    zeroPredict = predictOutageProba(weather0,'rf')
    assert math.isclose(0.6080934, zeroPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.3351444, zeroPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.05676219, zeroPredict[0,2], rel_tol=1e-05)

    onePredict = predictOutageProba(weather1,'rf')
    assert math.isclose(0.21820651, onePredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.60820715, onePredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.17358635, onePredict[0,2], rel_tol=1e-05)

    twoPredict = predictOutageProba(weather2,'rf')
    assert math.isclose(0.04692218, twoPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.29712351, twoPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.65595431, twoPredict[0,2], rel_tol=1e-05)
    
    return

def test_predictOutageProba_et():
    """Test probability outputs of the model"""
    # extra trees
    zeroPredict = predictOutageProba(weather0,'et')
    assert math.isclose(0.57055553, zeroPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.32320114, zeroPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.10624333, zeroPredict[0,2], rel_tol=1e-05)

    onePredict = predictOutageProba(weather1,'et')
    assert math.isclose(0.21184234, onePredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.37707334, onePredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.41108432, onePredict[0,2], rel_tol=1e-05)

    twoPredict = predictOutageProba(weather2,'et')
    assert math.isclose(0.15464471, twoPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.22724488, twoPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.61811041, twoPredict[0,2], rel_tol=1e-05)
    
    return

def test_predictOutageProba_ab():
    """Test probability outputs of the model"""
    # AdaBoost
    zeroPredict = predictOutageProba(weather0,'ab')
    assert math.isclose(0.57178065, zeroPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.36478664, zeroPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.06343271, zeroPredict[0,2], rel_tol=1e-05)

    onePredict = predictOutageProba(weather1,'ab')
    assert math.isclose(0.44784516, onePredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.41639007, onePredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.13576478, onePredict[0,2], rel_tol=1e-05)

    twoPredict = predictOutageProba(weather2,'ab')
    assert math.isclose(0.04308163, twoPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.94353618, twoPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.01338219, twoPredict[0,2], rel_tol=1e-05)
    
    return

def test_predictOutageProba_gb():
    """Test probability outputs of the model"""  
    # Gradient Boost
    zeroPredict = predictOutageProba(weather0,'gb')
    assert math.isclose(0.71547103, zeroPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.2560004 , zeroPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.02852857, zeroPredict[0,2], rel_tol=1e-05)

    onePredict = predictOutageProba(weather1,'gb')
    assert math.isclose(0.45132737, onePredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.54599083, onePredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.0026818 , onePredict[0,2], rel_tol=1e-05)

    twoPredict = predictOutageProba(weather2,'gb')
    assert math.isclose(0.00180422, twoPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.12376263, twoPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0.87443314, twoPredict[0,2], rel_tol=1e-05)
    
    return

def test_predictOutageProba_bg():
    """Test probability outputs of the model"""    
    # Bagging
    zeroPredict = predictOutageProba(weather0,'bg')
    assert math.isclose(0.9, zeroPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.1, zeroPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0, zeroPredict[0,2], rel_tol=1e-05)

    onePredict = predictOutageProba(weather1,'bg')
    assert math.isclose(0.9, onePredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.1, onePredict[0,1], rel_tol=1e-05)
    assert math.isclose(0., onePredict[0,2], rel_tol=1e-05)

    twoPredict = predictOutageProba(weather2,'bg')
    assert math.isclose(0.9, twoPredict[0,0], rel_tol=1e-05)
    assert math.isclose(0.1, twoPredict[0,1], rel_tol=1e-05)
    assert math.isclose(0., twoPredict[0,2], rel_tol=1e-05)
    
    return


def test_predictOutage():
    """Test classification outputs of the model"""
    assert predictOutage(weather0,'dt') == 0
    assert predictOutage(weather1,'dt') == 2
    assert predictOutage(weather2,'dt') == 2
    
    assert predictOutage(weather0,'rf') == 0
    assert predictOutage(weather1,'rf') == 1
    assert predictOutage(weather2,'rf') == 2
    
    assert predictOutage(weather0,'et') == 0
    assert predictOutage(weather1,'et') == 2
    assert predictOutage(weather2,'et') == 2
    
    assert predictOutage(weather0,'ab') == 0
    assert predictOutage(weather1,'ab') == 0
    assert predictOutage(weather2,'ab') == 1
    
    assert predictOutage(weather0,'gb') == 0
    assert predictOutage(weather1,'gb') == 1
    assert predictOutage(weather2,'gb') == 2
    
    assert predictOutage(weather0,'bg') == 0
    assert predictOutage(weather1,'bg') == 0
    assert predictOutage(weather2,'bg') == 0
    
    return

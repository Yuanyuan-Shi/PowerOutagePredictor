"""
predict the probabilities of outages falling into one of the three
categories: 0-2, 3-7, 8+ outages.

Params:

weatherData - A pandas DataFrame with shape (# of samples, 7),
where 7 represents the required features to make predictions. The
required features in order are: day length (hrs), average temperature
(F), average humidity (%), max windspeed (mph), average windspeed (mph),
max windgust (mph), precipitation (in). For the tree-based method package,
only 5 of the 7 features will be used for best results. Please name them
as 'Day_length_hr','Avg_Temp_F','Avg_humidity_percent','Max_windspeed_mph',
and 'Precipitation_in' respectively.

method - a string representing a method supported
         default method is ExtraTrees if no method specified
        'dt' for DecisionTree,
        'rf' for RandomForest, 
        'et' for ExtraTrees,                               
        'ab' for AdaBoost
        'gb' for GradientBoost
        'bg' for Bagging

Returns:
Numpy array with shape (# of samples, 3). Columns 0, 1, and 2
correspond to the 3 classes of outages 0-2, 3-7, and 8+, respectively,
where the values are the probabilities. The order of the samples are
maintained.

Raises:
ValueError - if shape of weatherData is not (:, 7)
ValueError - if method is not one of 'dt', 'rf', 'et','ab','gb','bg' or None.
"""

import pandas as pd
from sklearn import preprocessing
from sklearn.externals import joblib

def predictOutageProba(weatherData,method=None):
    """predict the probabilities of outages falling into one of the three
categories: 0-2, 3-7, 8+ outages.
"""
    if weatherData.shape[1] != 7:
        raise ValueError("7 features are required. See documentation.")
    if method == 'dt':
        model = joblib.load('dt.pkl')
    elif method == 'rf':
        model = joblib.load('rf.pkl')
    elif method == 'et' or method is None:
        model = joblib.load('et.pkl')
    elif method == 'ab':
        model = joblib.load('ab.pkl')
    elif method == 'gb':
        model = joblib.load('gb.pkl')
    elif method == 'bg':
        model = joblib.load('bg.pkl')
    else:
        raise ValueError("method has to be 'dt', 'rf', 'et','ab','gb' or 'bg'")
    scaler = joblib.load("scaler.pkl")
    weather = weatherData[['Day_length_hr','Avg_Temp_F','Avg_humidity_percent',
                           'Max_windspeed_mph','Precipitation_in']]
    scaledData = scaler.transform(weather)
    return model.predict_proba(scaledData)

"""
Predict the number outages falling into one of the three
categories: 0-2, 3-7, 8+ outages.

Params:

weatherData - A numpy 2d array or like with shape (# of samples, 7),
where 7 represents the required features to make predictions. The
required features in order are: day length (hrs), average temperature
(F), average humidity (%), max windspeed (mph), average windspeed (mph),
max windgust (mph), precipitation (in). For the tree-based method package,
only 5 of the 7 features will be used for best results. Please name them
as 'Day_length_hr','Avg_Temp_F','Avg_humidity_percent','Max_windspeed_mph',
and 'Precipitation_in' respectively.

method - a string representing a method supported
         default method is ExtraTrees if no method specified
        'dt' for DecisionTree,
        'rf' for RandomForest, 
        'et' for ExtraTrees,                               
        'ab' for AdaBoost
        'gb' for GradientBoost
        'bg' for Bagging

Returns:
Numpy array with shape (# of samples, 1). The values 0, 1, and 2
correspond to the 3 classes of outages 0-2, 3-7, and 8+, respectively.
The order of the samples are maintained.

Raises:
ValueError - if shape of weatherData is not (:, 7)
ValueError - if method is not one of 'dt', 'rf', 'et','ab','gb' or 'bg'.
"""
def predictOutage(weatherData,method=None):
    """Predict the number outages falling into one of the three
categories: 0 (0-2), 1 (3-7), 2 (8+) outages."""
    if weatherData.shape[1] != 7:
        raise ValueError("7 features are required. See documentation.")
    if method == 'dt':
        model = joblib.load('dt.pkl')
    elif method == 'rf':
        model = joblib.load('rf.pkl')
    elif method == 'et' or method is None:
        model = joblib.load('et.pkl')
    elif method == 'ab':
        model = joblib.load('ab.pkl')
    elif method == 'gb':
        model = joblib.load('gb.pkl')
    elif method == 'bg':
        model = joblib.load('bg.pkl')
    else:
        raise ValueError("method has to be 'dt', 'rf', 'et','ab','gb' or 'bg'")
    scaler = joblib.load("scaler.pkl")
    weather = weatherData[['Day_length_hr','Avg_Temp_F','Avg_humidity_percent',
                           'Max_windspeed_mph','Precipitation_in']]
    scaledData = scaler.transform(weather)
    return model.predict(scaledData)

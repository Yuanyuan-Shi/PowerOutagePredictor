from sklearn.externals import joblib
from sklearn.svm import SVC
import numpy as np
from sklearn.preprocessing import StandardScaler

"""
Predict the probabilities of outages falling into one of the three
categories: 0-2, 3-7, 8+ outages.

Params:
weatherData - A numpy 2d array or like with shape (# of samples, 7),
where 7 represents the required features to make predictions. The
required features in order are: day length (hrs), average temperature
(F), average humidity, max windspeed (mph), average windspeed (mph),
max windgust (mph), precipitation (in).

Returns:
Numpy array with shape (# of samples, 3). Columns 0, 1, and 2
correspond to the 3 classes of outages 0-2, 3-7, and 8+, respectively,
where the values are the probabilities. The order of the samples are
maintained.

Raises:
ValueError - if shape of weatherData is not (:, 7)
"""
def predictOutageProba(weatherData):
    if weatherData.shape[1] != 7:
        raise ValueError("7 features are required. See documentation.")
    model = joblib.load("SVCmodel.pkl")
    scaler = joblib.load("scaler.pkl")
    scaledData = scaler.transform(weatherData)
    return model.predict_proba(scaledData)

"""
Predict the number outages falling into one of the three
categories: 0-2, 3-7, 8+ outages.

Params:
weatherData - A numpy 2d array or like with shape (# of samples, 7),
where 7 represents the required features to make predictions. The
required features in order are: day length (hrs), average temperature
(F), average humidity, max windspeed (mph), average windspeed (mph),
max windgust (mph), precipitation (in).

Returns:
Numpy array with shape (# of samples, 1). The values 0, 1, and 2
correspond to the 3 classes of outages 0-2, 3-7, and 8+, respectively.
The order of the samples are maintained.

Raises:
ValueError - if shape of weatherData is not (:, 7)
"""
def predictOutage(weatherData):
    if weatherData.shape[1] != 7:
        raise ValueError("7 features are required. See documentation.")
    model = joblib.load("SVCmodel.pkl")
    scaler = joblib.load("scaler.pkl")
    scaledData = scaler.transform(weatherData)
    return model.predict(scaledData)

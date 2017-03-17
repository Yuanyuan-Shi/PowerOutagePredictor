# API Documentation


## SVM module

### PredictOutageProba(weatherData)
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


### PredictOutage(weatherData)
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

## TreeClassifier module

### PredictOutageProba(weatherData, method)
Predict the probabilities of outages falling into one of the three
categories: 0-2, 3-7, 8+ outages using the specified method.

Params:
* weatherData - A pandas DataFrame with shape 1 by 7,
where 7 represents the required features to make predictions. The
required features in order are: day length (hrs), average temperature
(F), average humidity (%), max windspeed (mph), average windspeed (mph),
max windgust (mph), precipitation (in). For the tree-based method module,
only 5 of the 7 features will be used for best results. Please name them
as 'Day_length_hr','Avg_Temp_F','Avg_humidity_percent','Max_windspeed_mph',
and 'Precipitation_in' respectively. You can give any number for the other 
two unused parameters.
* method - a string representing a method supported, the default method is ExtraTrees if no method specified
     * 'dt' for DecisionTree,
     * 'rf' for RandomForest, 
     * 'et' for ExtraTrees,
     * 'ab' for AdaBoost,
     * 'gb' for GradientBoost,
     * 'bg' for Bagging.

Returns:
Numpy array with shape (# of samples, 3). Columns 0, 1, and 2
correspond to the 3 classes of outages 0-2, 3-7, and 8+, respectively,
where the values are the probabilities. The order of the samples are
maintained.

Raises:
* ValueError - if shape of weatherData is not (:, 7)
* ValueError - if method is not one of 'dt', 'rf', 'et','ab','gb','bg' or None.

## Neural Network module

### PredictOutage(weatherData, method)
Predict the number outages falling into one of the three
categories: 0 (0-2), 1 (3-7), 2 (8+ outages).

Params:
* weatherData - A pandas DataFrame with shape 1 by 7,
where 7 represents the required features to make predictions. The
required features in order are: day length (hrs), average temperature
(F), average humidity (%), average windspeed (mph), max windspeed (mph), 
precipitation (in) and event thunderstorm. For the neural network method module,
please name them as 'Day_length_hr','Avg_Temp_F','Avg_humidity_percent','Avg_windspeed_mph','Max_windspeed_mph',
'Precipitation_in','Event_thunderstorm'

Methods:
* neural_network_clf(x_train, y_train, x_test, y_test)
It takes the train and test data as input, and returns the values 0, 1, and 2
correspond to the 3 classes of outages 0-2, 3-7, and 8+, respectively.
Also, it returns the training and testing error.

Raises:
* ValueError - if load data not successfully
* ValueError - if between-class imbalance beyond certain threshold. 


## Linear module
We tried Multiple Linear Regression, Lasso, Ridge but none of them could get a satisfactory result.
We didn't write them into .py packages but just briefly tested them in ipython notebook.
The result is [here](https://github.com/rkastilani/PowerOutagePredictor/tree/master/PowerOutagePredictor/Linear).






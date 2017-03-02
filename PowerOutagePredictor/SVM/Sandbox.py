from sklearn.svm import SVR
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import ShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

data = pd.read_csv("../../Data/WeatherOutagesAll_RK.csv", index_col="Date")
scaler = StandardScaler()
splitter = ShuffleSplit(n_splits=1, random_state=0)
xTrain = None
yTrain = None
xTest = None
yTest = None
df = None

for train, test in splitter.split(data):
    xTrain = scaler.fit_transform(data.iloc[train, 1:])
    yTrain = data.iloc[train, 0]
    xTest = scaler.transform(data.iloc[test, 1:])
    yTest = data.iloc[test, 0]
    cRange = np.logspace(-5, 7, 5)
    gammaRange = np.logspace(-5, 7, 5)
    paramGrid = dict(gamma=gammaRange, C=cRange)
    grid = GridSearchCV(SVR(cache_size=3000), param_grid=paramGrid, cv=ShuffleSplit(n_splits=5))
    grid.fit(xTrain, yTrain)
    print("The best parameters are %s with a score of %0.2f"
      % (grid.best_params_, grid.best_score_))
    df = pd.DataFrame(grid.cv_results_)
print(df)
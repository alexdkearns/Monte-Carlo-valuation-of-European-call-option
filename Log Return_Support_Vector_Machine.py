# imports required packages
import matplotlib.pyplot
import numpy as np
import datetime as dt
from pandas_datareader import data as pdr
from pylab import plt, mpl

end = dt.datetime.now()  # sets end of time frame as todays date
start = end - dt.timedelta(days=3650)  # sets the beginning time 5 years from today's date
# ticker = str(input("Enter Stock Ticker: "))
data = pdr.get_data_stooq('AAPL', start, end)  # Pulls data from google finance using the previously specified dates

print(data.head())  # Prints top lines of the dataset
data['Log Returns'] = np.log(data['Close'] / data['Close'].shift(1))  # calculates the log returns using the daily Closing price

print(data.head())
lags = 6

cols = []

for lag in range(1, lags + 1):
    col = 'lag_{}'.format(lag)
    data[col] = np.sign(data['Log Returns'].shift(lag))
    cols.append(col)
data.dropna(inplace=True)

from sklearn.svm import SVC

model = SVC(gamma='auto')

model.fit(data[cols], np.sign(data['Log Returns']))
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

data['Prediction'] = model.predict(data[cols])
data['Strategy'] = data['Prediction'] * data['Log Returns']

data[['Log Returns', 'Strategy']].cumsum().apply(np.exp).plot(figsize=(10, 6))
plt.savefig('myfig2.png') # saves plots to image (included in repository)

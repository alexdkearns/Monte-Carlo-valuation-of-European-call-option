import numpy as np
import datetime as dt
from pandas_datareader import data as pdr
from pylab import plt, mpl



end = dt.datetime.now()
start = end - dt.timedelta(days=1825)

data = pdr.get_data_stooq('GOOG', start, end)

print(data.head())
data['Log Returns'] = np.log(data['Close'] / data['Close'].shift(1))
data['vola'] = data['Log Returns'].rolling(252).std() * (np.sqrt(252))

#data['vola'].plot()
#plt.style.use('seaborn')
#mpl.rcParams['font.family'] = 'serif'
#plt.savefig('myfig.png')
data[['Close', 'vola']].plot(subplots=True, figsize=(10, 6))
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
plt.savefig('myfig.png')
#
# Monte Carlo valuation of European call Option
# in Black-Scholes-Merton model
# bsm_mcs_euro.py
#
import numpy as np

# parameter Values
S0 = 100.  # initial index level
K = 105.  # strike price
T = 1.0  # time-to-maturity
r = 0.05  # riskless short rate
sigma = 0.2  # volatility


I = 100000  # number of simulations

# Valuation Algorithm

z = np.random.standard_normal(I)  # pseudorandom numbers
ST = S0 * np.exp((r - 0.05 * sigma * 2) * T + sigma * np.sqrt(T) * z)
 # index values at maturity
hT = np.maximum(ST - K, 0)  # inner values at maturity
C0 = np.exp(-r * T) * sum(hT) / I  # Monte Carlo Estimator

# Result Output
print("Value of European call Option %5.3f" % C0)



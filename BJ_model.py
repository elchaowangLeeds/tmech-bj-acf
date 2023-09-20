import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller as ADF


# Load dataset
filename = 'data.xlsx'
df = pd.read_excel(filename, engine='openpyxl')
# inputs = ['angular_speed', 'theta']
# output = 'torque'

theta = df['theta']
speed = df['angular_speed']
torque = df['torque']


# Model Identification
# Plot ACF and PACF to identify potential AR and MA orders

plot_acf(torque, lags=4000)
plt.show()

plot_pacf(torque, lags=50)
plt.show()






















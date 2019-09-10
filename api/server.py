import numpy as np
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
import json
from models import adam_regression

def get_stock_data(x):
    """
    Get a specific stock data thing
    """

def get_weekly_time_series(x):
    data, meta_data = ts.get_weekly(symbol=x)

    return data["4. close"]


def plot_time_series(data, index, title):
    data[index].plot()
    plt.title(title)
    plt.show()

    return 0

# Read in credentials for making an alphavantage call
file = open('credentials.txt', 'r')
key = file.read().strip()
file.close()

ts = TimeSeries(key=key, output_format='pandas', indexing_type='date')
ti = TechIndicators(key=key, output_format='pandas', indexing_type='date')

msft_y_data = get_weekly_time_series("MSFT")
data, meta_data = ti.get_sma(symbol="MSFT", interval="weekly")
msft_x_data = data["SMA"]

# make sure the data's dates match up

adam_regression(msft_x_data, msft_y_data)

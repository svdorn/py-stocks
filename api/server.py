import numpy as np
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import json

def get_stock_data(x):
    """
    Get a specific stock data thing
    """

def get_weekly_time_series(x):
    data, meta_data = ts.get_weekly(symbol=x)

    plot_time_series(data, "4. close", "MSFT Time Series Weekly")

    return data, meta_data


# Manage alphavantage calls to ensure that we aren't hitting the api limits
def api_limits(x):
    """
    Get a specific stock data thing
    """

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

get_weekly_time_series("MSFT")

import numpy as np
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import json
from models import adam_regression

def get_stock_data(x):
    """
    Get a specific stock data thing
    """

def get_weekly_time_series(x):
    data, meta_data = ts.get_weekly(symbol=x)

    return data

def get_sma_data(x):
    y_train, y_train_metadata = ts.get_weekly(symbol=x)
    x_train, x_train_metadata = ti.get_sma(symbol=x, interval='weekly')
    # merge the data so that the dates match up
    data = pd.merge(x_train, y_train, how='inner', left_index=True, right_index=True)

    return data

# Read in credentials for making an alphavantage call
file = open('credentials.txt', 'r')
key = file.read().strip()
file.close()

ts = TimeSeries(key=key, output_format='pandas', indexing_type='date')
ti = TechIndicators(key=key, output_format='pandas', indexing_type='date')

data = get_sma_data(x="MSFT")

adam_regression(data['SMA'], data['4. close'])

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_time_series(data, index, title):
    data[index].plot()
    plt.title(title)
    plt.show()

    return 0

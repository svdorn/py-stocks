import numpy as np
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout
from keras.optimizers import Adam
import matplotlib.pyplot as plt
from sklearn.preprocessing import  MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.wrappers.scikit_learn import KerasRegressor

EPOCHS = 10
LEARNING_RATE = 0.2

def build_regressor():
    model = Sequential()

    model.add(Dense(32, activation='relu', input_dim=4))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1))

    model.compile(Adam(lr=LEARNING_RATE), 'mean_squared_error', metrics=['mae','accuracy'])

    return model

def adam_regression(x, y):
    print(y)
    # scale the data
    sc = MinMaxScaler()
    x = sc.fit_transform(x)
    y = y.reshape(-1,1)
    y = sc.fit_transform(y)
    print(y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    model = KerasRegressor(build_fn=build_regressor, batch_size=32,epochs=EPOCHS)

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    y_pred = y_pred.reshape(-1,1)
    predictions = sc.inverse_transform(y_pred)

    print(y_pred)
    print(predictions)

    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    plt.show()

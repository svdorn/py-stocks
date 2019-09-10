import numpy as np
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam

def adam_regression(x_train, y_train):

    epochs = 100
    learning_rate = 0.8

    model = Sequential()

    model.add(Dense(28, activation='relu', input_shape=(28,)))
    model.add(Dense(28, activation='relu'))
    model.add(Dense(4))
    print("compiling")

    model.compile(Adam(lr=learning_rate), 'mean_squared_error')

    print("fitting")
    print(x_train)
    print(y_train)
    model.fit(x_train, y_train, epochs=epochs)

    print("predicting")
    predictions = model.predict(x_train)

    print(predictions)

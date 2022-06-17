import pandas
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Use historical sentiment and volatility data to from regression model
df = pandas.read_csv("./data.csv")
df.drop("Date")

# Use 80% of the data for training
trainData = df.sample(frac=0.8, random_state=0)
testData = df.drop(trainData.index)

train_ans = df.pop(df.columns[1])
test_ans = df.pop(df.columns[1])

def buildModel():
    model = keras.Sequential([
        layers.Dense(64, activation=tf.nn.relu, input_shape=[len(trainData.keys())]),
        layers.Dense(64, activation=tf.nn.relu),
        layers.Dense(1)
    ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(
        loss = 'mse',
        optimizer = optimizer,
        metrics=['mae','mse']
    )

    return model

def trainModel(model):
    # Stop training if the model stops improving
    stop = keras.callbacks.EarlyStopping(monitor="val_loss", patience=10)

    model.fit(
        trainData, train_ans,
        epochs=1000, validation_split = 0.2, verbose=0,
    )
    model.save('sentiVol.h5')

trainModel(buildModel())
# write fastapi code to create an API for the model: lstm_model.hdf5


from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from tensorflow.keras.models import load_model
from tensorflow import keras
import tensorflow as tf
import pandas as pd
import numpy as np
from typing import Union
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# edit the above fastapi code to create an API for lstm_model.hdf5
# input data: HUMIDITY, year, month, day, hour, minute, second
# output data: temperature

# import the required libraries

# load the model
model = load_model('lstm_model.hdf5')

# create a function to predict the temperature
app = FastAPI()


def predict_temperature(HUMIDITY, year, month, day, hour, minute, second):
    # create a dataframe with the input data
    df = pd.DataFrame({'HUMIDITY': [HUMIDITY], 'year': [year], 'month': [
                      month], 'day': [day], 'hour': [hour], 'minute': [minute], 'second': [second]})
    # # create a TimeseriesGenerator object
    # data_gen = TimeseriesGenerator(
    #     df.values, df.values, length=2, batch_size=1)
    # print("GEN :> ", data_gen)
    # predict the temperature
    data_gen = np.array(
        [[[HUMIDITY], [year], [month], [day], [hour], [minute], [second]]])
    data_gen = data_gen.reshape(None, None, 1)
    print(data_gen.shape)
    # data_gen = np.array(
    #     [[[75], [2020], [1], [1], [1], [1], [1]]])
    print(data_gen.shape)
    temperature = model.predict(data_gen)[0][0][0]
    # return the temperature
    return temperature


# create a function to create an API for the model
app = FastAPI()


@app.get("/predict_temperature/{HUMIDITY}/{year}/{month}/{day}/{hour}/{minute}/{second}")
def predict_temperature_api(HUMIDITY: float, year: int, month: int, day: int, hour: int, minute: int, second: int):
    # predict the temperature
    temperature = predict_temperature(
        HUMIDITY, year, month, day, hour, minute, second)
    # return the temperature
    return {"temperature": temperature}

# # run the API
# # uvicorn create_api:app --reload

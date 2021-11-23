import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score
import joblib


class Trainer:
    model = None
    pandas_datasource = None
    predictions_datasource = pd.DataFrame(data={
        'accelX': [0.0], 'accelY': [0.0], 'accelZ': [0.0],
        'gyroX': [0.0], 'gyroY': [0.0], 'gyroZ': [0.0]
    })
    predictions_datasource_length = 5


    def __init__(self, model_filename, pandas_datasource = None):
        self.model_filename = model_filename
        self.pandas_datasource = pandas_datasource

        if model_filename and pandas_datasource is None:
            self.load_model()


    def create_model(self):
        x = self.pandas_datasource.drop('state', axis=1)
        y = self.pandas_datasource['state']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

        self.model = ExtraTreesClassifier()
        self.model.fit(x_train, y_train)

        predictions = self.model.predict(x_test)
        print(f"accuracy: {accuracy_score(y_test, predictions)}")


    def append_new_data(self, esp32_data):
        accelX, accelY, accelZ, gyroX, gyroY, gyroZ = esp32_data
        new_data = pd.DataFrame({
            'accelX': [accelX], 'accelY': [accelY], 'accelZ': [accelZ],
            'gyroX': [gyroX], 'gyroY': [gyroY], 'gyroZ': [gyroZ]
        })

        self.predictions_datasource = (
            self.predictions_datasource
                .append(new_data, ignore_index=True)
                .tail(self.predictions_datasource_length)
        )


    def predict(self):
        if (self.predictions_datasource.size > 0):
            return self.model.predict(self.predictions_datasource)[-1]


    def persist_model(self):
        if not os.path.exists('models'):
            os.makedirs('models')

        joblib.dump(self.model, f"models/{self.model_filename}.joblib")


    def load_model(self):
        self.model = joblib.load(f"models/{self.model_filename}.joblib")
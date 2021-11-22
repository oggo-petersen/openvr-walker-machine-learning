import csv
import pandas as pd

class CSVHandler:
    file = None
    filename = None
    pandas_datasource = None
    writer = None
    header = ['accelX','accelY', 'accelZ', 'gyroX', 'gyroY', 'gyroZ', 'state']

    def __init__(self, filename):
        self.filename = filename


    def open_csv(self):
        self.file = open(self.filename, 'r')


    def create_header(self):
        self.write_row(self.header)


    def write_row(self, data):
        self.file = open(self.filename, 'a', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(data)
        self.file.close()


    def read_with_pandas(self):
        self.pandas_datasource = pd.read_csv(self.filename)


    def gather_data(self):
        self.create_header()

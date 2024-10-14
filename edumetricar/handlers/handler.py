import pandas as pd
from io import BytesIO

class Handler:
    def __init__(self, data_format='csv'):
        self.data_format = data_format

    def process_data(self, raw_data):
        if self.data_format == 'csv':
            data = pd.read_csv(BytesIO(raw_data))
        elif self.data_format == 'xlsx':
            data = pd.read_excel(BytesIO(raw_data))
        else:
            raise ValueError("Formato de datos no soportado")
        return data

    def filter_data(self, data, column, value):
        return data[data[column] == value]
from getters.getter import Get
from handlers.handler import Handler

class API:
    def __init__(self, source_url, data_format='csv'):
        self.getter = Get(source_url)
        self.handler = Handler(data_format)

    def fetch_and_process_data(self):
        # Obtener datos
        raw_data = self.getter.download_data()

        # Procesar datos
        processed_data = self.handler.process_data(raw_data)

        return processed_data

    def fetch_filter_data(self, column, value):
        # Obtener y procesar datos
        data = self.fetch_and_process_data()

        # Filtrar datos
        filtered_data = self.handler.filter_data(data, column, value)

        return filtered_data
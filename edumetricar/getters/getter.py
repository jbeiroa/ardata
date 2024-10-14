import requests

class Get:
    def __init__(self, source_url):
        self.source_url = source_url

    def download_data(self):
        response = requests.get(self.source_url)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Error al descargar datos: {response.status_code}")
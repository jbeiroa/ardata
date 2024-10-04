"""
scraper.py
"""

import requests
from bs4 import BeautifulSoup

url_ra = ['https://www.argentina.gob.ar/educacion/evaluacion-e-informacion-educativa/base-de-datos-por-escuela-2011',
          'https://www.argentina.gob.ar/educacion/evaluacion-e-informacion-educativa/base-de-datos-por-escuela-2012',
          'https://www.argentina.gob.ar/educacion/evaluacion-e-informacion-educativa/base-de-datos-por-escuela-2013',
          'https://www.argentina.gob.ar/educacion/evaluacion-e-informacion-educativa/base-de-datos-por-escuela-2014',
          'https://www.argentina.gob.ar/educacion/evaluacion-e-informacion-educativa/base-de-datos-por-escuela-2015',
          'https://www.argentina.gob.ar/base-de-datos-por-escuela-2016',
          'https://www.argentina.gob.ar/educacion/evaluacion-e-informacion-educativa/base-de-datos-por-escuela-2017',
          'https://www.argentina.gob.ar/educacion/evaluacion-e-informacion-educativa/base-de-datos-por-escuela-2018',
          'https://www.argentina.gob.ar/educacion/evaluacion-e-informacion-educativa/base-de-datos-por-escuela-2019',
          'https://www.argentina.gob.ar/educacion/evaluacion-e-informacion-educativa/base-de-datos-por-escuela-2020',
          'https://www.argentina.gob.ar/educacion/evaluacion-e-informacion-educativa/base-de-datos-por-escuela-2021',
          'https://www.argentina.gob.ar/educacion/evaluacion-e-informacion-educativa/base-de-datos-por-escuela-2022',
          'https://www.argentina.gob.ar/base-de-datos-por-escuela-2016']

class Scraper():
    """Scraper class
    """
    def __init__(self):
        pass
    
    def get_RA(self, url):
        """_summary_

        Args:
            url (_type_): _description_
        """
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', href=True)
            file_links = [link['href'] for link in links if link['href'].endswith('.csv') or link['href'].endswith('.xlsx')]
            if file_links:
                return file_links
            else:
                print("No se encontraron archivos .csv o .xlsx en la página.")
        else:
            print(f"Error al acceder a la página: {response.status_code}")

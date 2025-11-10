import requests
from bs4 import BeautifulSoup

# URL del sitio que queremos scrapear
url = "https://diariosur.es/"

# Hacemos la petición HTTP GET a la página
# (puedes añadir timeout=10 o headers con un User-Agent si el sitio lo requiere)
response = requests.get(url)

# Creamos el objeto BeautifulSoup con el HTML obtenido
# 'html.parser' usa el parser de Python incluido por defecto
soup = BeautifulSoup(response.text, 'html.parser')

# Buscamos todas las etiquetas <h2> (titulares, en muchos medios suelen estar en este nivel)
titulos = soup.find_all('h2')

# Recorremos solo los 10 primeros resultados encontrados
for i, titulo in enumerate(titulos[:10]):
    # get_text(strip=True) extrae el texto interno del <h2> y elimina espacios/saltos al principio y final
    print(f"{i+1}. {titulo.get_text(strip=True)}")

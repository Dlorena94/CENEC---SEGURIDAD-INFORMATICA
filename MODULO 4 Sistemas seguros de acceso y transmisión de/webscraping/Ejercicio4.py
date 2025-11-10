import csv

import requests
from bs4 import BeautifulSoup

# URL base del sitio de práctica de scraping
url = "https://books.toscrape.com/"

# Hacemos la petición HTTP GET:
# - timeout para no quedarnos colgados
# - headers con User-Agent para evitar bloqueos tontos
res = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
res.raise_for_status()  # Lanza excepción si no es 2xx

# Parseamos el HTML con BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')

# Seleccionamos los "pods" de producto (cada libro)
# books.toscrape.com usa <article class="product_pod"> para cada libro
libros = soup.select("article.product_pod")

# Creamos el archivo CSV en UTF-8
with open("libros.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Fila de encabezados
    writer.writerow(["Título", "Precio"])

    # Tomamos solo los 5 primeros (como en tu ejemplo)
    for libro in libros[:5]:
        # El título está en el atributo 'title' del enlace dentro del <h3>
        titulo = libro.h3.a["title"]

        # El precio está en un span con clase .price_color (ej: '£51.77')
        precio_raw = libro.select_one(".price_color").get_text(strip=True)

        # (Opcional) Limpiar precio: quitar símbolo de moneda y convertir a float
        # - books.toscrape usa '£'. Si quieres conservar el símbolo, omite esto.
        precio_num = precio_raw.replace("£", "").strip()

        # Escribimos la fila en el CSV (puedes poner precio_raw si prefieres con símbolo)
        writer.writerow([titulo, precio_num])

print("✅ Datos guardados en libros.csv")

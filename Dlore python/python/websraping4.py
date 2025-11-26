import csv
 
import requests
from bs4 import BeautifulSoup
 
url = "https://books.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
 
libros = soup.select("article.product_pod")
 
# Creamos el archivo CSV
with open("libros.csv", "w", newline="", encoding="utf-8") as f:
	writer = csv.writer(f)
	writer.writerow(["Título", "Precio"])  # Encabezados
 
	for libro in libros[:5]:
    	titulo = libro.h3.a['title']
    	precio = libro.select_one(".price_color").text
    	writer.writerow([titulo, precio])
 
print("✅ Datos guardados en libros.csv")

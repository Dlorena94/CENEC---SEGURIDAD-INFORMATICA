import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

libros = soup.select("article.product_pod")

for libro in libros[:5]:
    titulo = libro.h3.a['title']
    precio = libro.select_one(".price_color").text
    print(f"{titulo} - {precio}")

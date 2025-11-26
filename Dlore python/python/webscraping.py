 
import requests
from bs4 import BeautifulSoup
 
url = "https://www.elmundo.es/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
 
titulos = soup.find_all('h2')
 
for i, titulo in enumerate(titulos[:10]):
	print(f"{i+1}. {titulo.get_text(strip=True)}")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import csv


import requests
from bs4 import BeautifulSoup


BASE = "https://www.tiempo.com/"
CITIES = {
    "Madrid": "madrid.htm",
    "Barcelona": "barcelona.htm",
    "Málaga": "malaga.htm",
}


rows = []


for ciudad, slug in CITIES.items():
    url = BASE + slug
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    r.raise_for_status()


    soup = BeautifulSoup(r.text, "html.parser")


    # Selectores sencillos (ajusta si cambian en la web)
    temp_el = soup.select_one(".dato-temperatura")
    estado_el = soup.select_one(".descripcion")


    temperatura = temp_el.get_text(strip=True) if temp_el else ""
    estado = estado_el.get_text(strip=True) if estado_el else ""


    rows.append([ciudad, temperatura, estado])


# Guardar CSV
with open("meteo.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ciudad", "temperatura", "estado"])
    writer.writerows(rows)


print("✅ Datos guardados en meteo.csv")
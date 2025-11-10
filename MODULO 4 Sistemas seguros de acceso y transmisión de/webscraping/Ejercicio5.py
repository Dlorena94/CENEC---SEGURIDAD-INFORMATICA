#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from urllib.parse import urldefrag, urljoin

import requests
from bs4 import BeautifulSoup

# URL base: si pasas una URL por argumento la usa, si no usa example.com
BASE_URL = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"

def fetch_html(url):
    """Descarga el HTML de la URL dada y lo devuelve como texto."""
    r = requests.get(url, timeout=10)
    r.raise_for_status()  # si no es 2xx lanza excepción
    return r.text

def extract_links(base_url, html):
    """
    Extrae todos los <a href="...">, resuelve enlaces relativos a absolutos
    y elimina fragmentos (#lo-que-sea).
    """
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.select('a[href]'):
        href = a.get("href", "").strip()
        # Ignorar mailto:, tel:, javascript:, y anclas puras '#'
        if not href or href.startswith(("mailto:", "tel:", "javascript:", "#")):
            continue
        # Convertir relativo -> absoluto
        absolute = urljoin(base_url, href)
        # Quitar el fragmento (parte tras #)
        absolute, _ = urldefrag(absolute)
        links.append(absolute)

    # Quitar duplicados manteniendo orden
    seen = set()
    unique = []
    for u in links:
        if u not in seen:
            seen.add(u)
            unique.append(u)
    return unique

def check_link_head(url):
    """Hace HEAD al enlace y devuelve (status_code, ok_200)."""
    try:
        r = requests.head(url, allow_redirects=True, timeout=10)
        return r.status_code, (r.status_code == 200)
    except requests.RequestException:
        return None, False  # error de red, DNS, timeout, etc.

def main():
    print(f"Analizando enlaces en: {BASE_URL}\n")

    try:
        html = fetch_html(BASE_URL)
    except Exception as e:
        print(f"[ERROR] No se pudo descargar {BASE_URL}: {e}")
        sys.exit(1)

    links = extract_links(BASE_URL, html)
    print(f"Encontrados {len(links)} enlaces.\n")

    ok, fail = 0, 0
    for url in links:
        status, is_ok = check_link_head(url)
        if is_ok:
            ok += 1
            print(f"[OK  ] 200 -> {url}")
        else:
            fail += 1
            st = status if status is not None else "ERROR"
            print(f"[FAIL] {st} -> {url}")

    print("\nResumen:")
    print(f"  OK (200): {ok}")
    print(f"  No 200 / error: {fail}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rastreador sencillo para books.toscrape.com:
  1) Visita páginas internas del mismo dominio.
  2) Extrae todos los <a href="...">.
  3) Comprueba cada enlace con HEAD (y GET si HEAD falla).
Marca OK únicamente cuando el código es 200.
"""

import time
from collections import deque
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"
DOMAIN = urlparse(BASE_URL).netloc
TIMEOUT = 10
UA = "Mozilla/5.0 (compatible; LinkChecker/mini/1.0)"

# Límites de seguridad para no volvernos locos
MAX_PAGES = 2000   # máximo de páginas HTML a rastrear
DELAY = 0.0        # segundos entre peticiones (sube si quieres ser más educado)

def get_html(url: str) -> str | None:
    """Descarga HTML; devuelve None si hay error."""
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=TIMEOUT)
        r.raise_for_status()
        # Solo consideramos HTML
        ctype = r.headers.get("Content-Type", "")
        if "text/html" not in ctype:
            return None
        return r.text
    except requests.RequestException:
        return None

def absolutize(base: str, href: str) -> str:
    """Convierte href relativo a absoluto y quita el #fragment."""
    absu = urljoin(base, href.strip())
    absu, _ = urldefrag(absu)
    return absu

def same_domain(url: str) -> bool:
    return urlparse(url).netloc == DOMAIN

def extract_links(base_url: str, html: str) -> list[str]:
    """Saca todos los <a href> HTTP/HTTPS, filtra mailto/tel/js/anchors."""
    soup = BeautifulSoup(html, "html.parser")
    out = []
    for a in soup.select("a[href]"):
        href = (a.get("href") or "").strip()
        if not href or href.startswith(("mailto:", "tel:", "javascript:", "#")):
            continue
        url = absolutize(base_url, href)
        scheme = urlparse(url).scheme
        if scheme in ("http", "https"):
            out.append(url)
    # Deduplicar manteniendo orden
    seen = set()
    uniq = []
    for u in out:
        if u not in seen:
            seen.add(u)
            uniq.append(u)
    return uniq

def head_then_get(url: str):
    """Intenta HEAD; si no es 200, reintenta con GET rápido (stream=True)."""
    try:
        r = requests.head(url, headers={"User-Agent": UA},
                          allow_redirects=True, timeout=TIMEOUT)
        if r.status_code == 200:
            return r.status_code, True, r.url
        # plan B: GET ligero (algunos bloquean HEAD o devuelven 405/403)
        r = requests.get(url, headers={"User-Agent": UA},
                         allow_redirects=True, timeout=TIMEOUT, stream=True)
        return r.status_code, (r.status_code == 200), r.url
    except requests.RequestException:
        return None, False, None

def crawl_and_check(start_url: str = BASE_URL):
    to_visit = deque([start_url])
    visited_pages = set()
    all_links = set()  # todos los href encontrados (únicos)

    print(f"Rastreando {start_url} (dominio: {DOMAIN})\n")

    # 1) CRAWL páginas internas
    while to_visit and len(visited_pages) < MAX_PAGES:
        url = to_visit.popleft()
        if url in visited_pages:
            continue
        if not same_domain(url):
            continue

        html = get_html(url)
        visited_pages.add(url)

        if html is None:
            print(f"[PAGE] ERROR -> {url}")
            continue

        links = extract_links(url, html)
        print(f"[PAGE] OK ({len(links)} enlaces) -> {url}")
        # Guardar todos los enlaces encontrados
        for link in links:
            all_links.add(link)
            # Encolar para visitar solo si es HTML probable del mismo dominio
            if same_domain(link):
                # Heurística básica: evita añadir archivos (imágenes, CSS, etc)
                path = urlparse(link).path.lower()
                if not path.endswith((".jpg", ".jpeg", ".png", ".gif", ".css", ".js", ".svg", ".ico", ".xml")):
                    if link not in visited_pages:
                        to_visit.append(link)

        if DELAY:
            time.sleep(DELAY)

    print(f"\nPáginas visitadas: {len(visited_pages)}")
    print(f"Enlaces totales encontrados (únicos): {len(all_links)}\n")

    # 2) COMPROBAR cada enlace con HEAD/GET
    ok, fail = 0, 0
    for link in sorted(all_links):
        status, is_ok, final_url = head_then_get(link)
        if is_ok:
            ok += 1
            print(f"[OK  ] 200 -> {link}")
        else:
            fail += 1
            st = status if status is not None else "ERROR"
            redir = f" → {final_url}" if final_url and final_url != link else ""
            print(f"[FAIL] {st} -> {link}{redir}")

    print("\nResumen:")
    print(f"  OK (200): {ok}")
    print(f"  No 200 / error: {fail}")

if __name__ == "__main__":
    crawl_and_check(BASE_URL)

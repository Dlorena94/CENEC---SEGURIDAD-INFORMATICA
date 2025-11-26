import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin # Para construir URLs absolutas

def verificar_enlaces(url_base):
    """Extrae todos los enlaces de una URL y verifica su código de estado HTTP."""
    
    print(f"[*] Accediendo a la URL base: {url_base}")
    
    try:
        # 1. Obtener el HTML
        res_base = requests.get(url_base, timeout=10)
        res_base.raise_for_status() # Lanza una excepción para errores 4xx/5xx
        
        soup = BeautifulSoup(res_base.text, 'html.parser')
        
        # 2. Extraer todos los elementos <a>
        enlaces_a = soup.find_all('a', href=True)
        
        if not enlaces_a:
            print("[!] No se encontraron etiquetas <a> con atributo href.")
            return

        print(f"[*] Se encontraron {len(enlaces_a)} enlaces en total.")
        print("-" * 40)
        
        # 3. Iterar y Verificar cada Enlace
        
        for a in enlaces_a:
            href_relativo = a['href']
            
            # Construir URL absoluta: Necesario para enlaces internos (ej. catalogue/...)
            url_completa = urljoin(url_base, href_relativo)
            
            # Usar requests.head() para verificar el estado sin descargar el contenido
            try:
                # El método HEAD es más rápido y eficiente para solo verificar el encabezado
                res_head = requests.head(url_completa, timeout=5)
                codigo_estado = res_head.status_code
                
                # Clasificar el resultado
                if codigo_estado == 200:
                    estado = "✅ OK (200)"
                elif codigo_estado >= 400:
                    estado = f"❌ ROTO ({codigo_estado})"
                else:
                    estado = f"⚠️ REDIRECCIÓN/OTRO ({codigo_estado})"
                    
                print(f"{estado} | {url_completa}")
                
            except requests.exceptions.RequestException as e:
                # Capturar errores de red (ej. DNS fallido, timeout)
                print(f"🛑 ERROR DE CONEXIÓN | {url_completa} ({e.__class__.__name__})")
                
    except requests.exceptions.RequestException as e:
        print(f"[CRITICAL] Fallo al acceder a la URL base: {e}")

if __name__ == "__main__":
    URL_BASE = "https://books.toscrape.com/"
    verificar_enlaces(URL_BASE)
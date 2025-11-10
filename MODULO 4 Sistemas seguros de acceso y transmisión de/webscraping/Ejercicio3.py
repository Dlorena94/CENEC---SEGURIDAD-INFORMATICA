import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# Opcional: esperas explícitas para evitar sleeps fijos
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# --- Configuración de Chrome ---
options = Options()
# Modo sin interfaz gráfica. En Chrome reciente, "--headless=new" suele ser más estable.
options.add_argument("--headless=new")
# Tamaño de ventana virtual (algunas webs cambian el layout según el viewport)
options.add_argument("--window-size=1920,1080")
# Opcionales útiles en contenedores/CI:
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# Crea el driver. webdriver_manager descarga el binario de ChromeDriver si hace falta.
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

try:
    # Navega a la página objetivo
    driver.get("https://www.malaga.es/agenda/")

    # --- Esperar a que cargue contenido ---
    # Evita usar sleep fijo; espera hasta que exista un elemento clave.
    # Ajusta el selector a algo representativo de la página (clase, id, etc.)
    # Si no conoces un selector concreto, el sleep puede mantenerse como fallback.
    try:
        # Espera hasta 10s a que aparezcan tarjetas/listado de agenda
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".agenda, .listado, main, article"))
        )
    except Exception:
        # Si no encuentra el selector, haz una espera corta como plan B
        time.sleep(5)

    # Captura el HTML renderizado por el navegador (incluye cambios del JS)
    html = driver.page_source

    # --- Guardar el HTML en disco ---
    ruta = os.path.join(os.getcwd(), "agenda_page.html")
    print(f"Guardando HTML en: {ruta}")

    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
        print("✅ HTML guardado correctamente.")

except Exception as e:
    print("❌ Ocurrió un error:", e)

finally:
    # Cierra el navegador siempre
    driver.quit()

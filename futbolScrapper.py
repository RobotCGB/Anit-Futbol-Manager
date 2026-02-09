import time
import subprocess
from playwright.sync_api import sync_playwright

VENV_PYTHON = "./venvFutbol/bin/python"
MODO_FUTBOL = "./modoFutbol.py"
MODO_NORMAL = "./modoNormal.py"

def ejecutar_script(ruta_script):
    """Ejecuta un script Python dentro del entorno virtual"""
    subprocess.run([VENV_PYTHON, ruta_script], check=True)

def check_estado():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://hayahora.futbol")

        page.wait_for_function("""
        () => {
            const el = document.querySelector('h1.hero-title.blocked');
            return el && (el.innerText === 'SÍ' || el.innerText === 'NO');
        }
        """)

        valor = page.inner_text("h1.hero-title.blocked")
        browser.close()
        return valor

if __name__ == "__main__":
    while True:
        estado = check_estado()
        print(f"Estado actual: {estado}")
        if estado == "SÍ":
            print("Ejecutando modoFutbol.py")
            ejecutar_script(MODO_FUTBOL)
        elif estado == "NO":
            print("Ejecutando modoNormal.py")
            ejecutar_script(MODO_NORMAL)
        else:
            print("Valor inesperado:", estado)

        time.sleep(300)  # espera 5 minutos

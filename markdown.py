import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

url = "https://www.fib.upc.edu"

# 1. Descargar el HTML de la página
response = requests.get(url)
html = response.text

# 2. Convertir HTML a Markdown directamente
markdown = md(html, heading_style="ATX")

# 3. Guardar el resultado en un archivo
with open("pagina_convertida.md", "w", encoding="utf-8") as file:
    file.write(markdown)

print("Página convertida a Markdown y guardada como 'pagina_convertida.md'")
import os
import requests
import html2text
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# URL de la web a descargar
url = "https://www.fib.upc.edu/"  # ⚠️ Reemplázalo con la web que quieras

# Carpeta donde se guardarán los archivos
output_folder = "temp"
os.makedirs(output_folder, exist_ok=True)

# Descargar la página web
response = requests.get(url)
response.raise_for_status()
html = response.text

# Analizar el HTML con BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Configurar html2text para conservar enlaces e imágenes sin descargarlas
h = html2text.HTML2Text()
h.ignore_links = False
h.ignore_images = False
h.ignore_emphasis = False
h.bypass_tables = False

# Convertir HTML a Markdown
markdown = h.handle(html)

# Añadir un encabezado principal
markdown = "# Bienvenido a la Conversión Markdown\n\n" + markdown

# Resaltar un título con negrita
markdown = markdown.replace("Documentos", "**Documentos importantes**")

# Añadir un índice o tabla de contenidos al principio
markdown = "## Índice\n\n" + "- [Documentos importantes](#documentos-importantes)\n\n" + markdown

# Agregar un comentario con HTML (esto es ignorado por la mayoría de los procesadores Markdown)
markdown += "\n\n<!-- Este es un comentario agregado en Markdown -->"

# Lista de extensiones de archivos a descargar (excluyendo imágenes)
extensiones_permitidas = (".pdf", ".zip", ".docx", ".xlsx", ".pptx")

# Lista para almacenar enlaces externos y su contenido
enlaces_externos = []

# Descargar archivos enlazados en <a> y NO descargar imágenes
for tag in soup.find_all("a"):  # Solo procesamos enlaces <a>
    file_url = tag.get("href")  # Obtener URL del enlace

    if file_url:
        file_url = urljoin(url, file_url)  # Convertir URL relativa a absoluta
        file_name = os.path.basename(urlparse(file_url).path)  # Obtener nombre del archivo

        # Si el enlace es a un archivo descargable
        if file_name.endswith(extensiones_permitidas):
            file_path = os.path.join(output_folder, file_name)

            try:
                file_data = requests.get(file_url)
                file_data.raise_for_status()

                with open(file_path, "wb") as file:
                    file.write(file_data.content)

                print(f"📥 Archivo descargado: {file_name}")

                # Reemplazar la URL en el Markdown con la ruta local
                markdown = markdown.replace(file_url, file_path)

            except requests.exceptions.RequestException as e:
                print(f"❌ Error descargando {file_url}: {e}")

        # Si el enlace es externo y no es un archivo descargable, descargamos su contenido y lo agregamos al markdown
        elif urlparse(file_url).netloc != urlparse(url).netloc:
            try:
                # Obtener el contenido del enlace externo
                external_response = requests.get(file_url)
                external_response.raise_for_status()
                external_html = external_response.text

                # Convertir el HTML del enlace externo a Markdown
                external_markdown = h.handle(external_html)

                # Crear un título estilizado con el enlace original
                markdown += f"\n\n## **Contenido de la página ['{file_url}']({file_url})**\n\n"

                # Añadir el contenido del enlace al Markdown principal
                markdown += external_markdown

                print(f"📥 Contenido de {file_url} añadido al Markdown.")

            except requests.exceptions.RequestException as e:
                print(f"❌ Error cargando el contenido de {file_url}: {e}")

# Guardar el Markdown actualizado con rutas locales y contenido adicional
md_file_path = os.path.join(output_folder, "pagina_con_contenido.md")
with open(md_file_path, "w", encoding="utf-8") as f:
    f.write(markdown)

print("✅ Markdown actualizado con estilo adicional, archivos descargados y contenido de enlaces externos.")

# Si deseas también guardar los enlaces externos por separado
if enlaces_externos:
    enlaces_md_path = os.path.join(output_folder, "enlaces_externos.md")
    with open(enlaces_md_path, "w", encoding="utf-8") as f:
        f.write("# Enlaces Externos\n\n" + "\n".join(enlaces_externos))

    print("✅ Enlaces externos guardados en 'enlaces_externos.md'")


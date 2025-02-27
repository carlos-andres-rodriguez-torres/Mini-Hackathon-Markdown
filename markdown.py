import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

url = "https://www.fib.upc.edu"

# 1. Download the HTML of the page
response = requests.get(url)
html = response.text

# 2. Convert HTML to Markdown directly
markdown = md(html, heading_style="ATX")

# 3. Save the result to a file
with open("markdown.md", "w", encoding="utf-8") as file:
    file.write(markdown)

print("Page converted to Markdown and saved as 'markdown.md'")
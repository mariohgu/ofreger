import re
import os
from pdfminer.high_level import extract_text

# pip install pdfminer.six
# Herramienta de OCR (Reconocimiento Óptico de Caracteres) como Pytesseract


def extract_using_regex(pattern, text):
    """Extrae el texto usando una expresión regular."""
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1)
    return None


file = os.path.dirname(__file__)
pdf_path = os.path.join(file, "documentos", "02.pdf")

text = extract_text(pdf_path)

# Extraer texto usando las expresiones regulares definidas
description_text = extract_using_regex(
    r"del peligro inminente:\s+(.*?)\s+\d+\.\d+\.+\s+[A-Z]", text
)
latitud = extract_using_regex(r"Latitud:\s+(.*?)\s+Longitud:\s", text)
longitud = extract_using_regex(r"Longitud:\s+(.*?)\s+Norte:\s", text)
tumbes_text = extract_using_regex(
    r"Ubigeo:\s+\nTumbes\s+(.*?)\s+\d+\.\d+\.+\s+[A-Z]", text
)

items = []

if tumbes_text:
    # Dividir el texto extraído en sus componentes individuales
    items.extend([item.strip() for item in tumbes_text.split("\n") if item.strip()])
else:
    print("No se encontró el texto relacionado con 'Tumbes'.")

if latitud:
    cleaned_text = latitud.replace(" ", "")
    items.append(cleaned_text)
else:
    print("No se encontró el texto relacionado con 'Latitud'.")

if longitud:
    cleaned_text = longitud.replace(" ", "")
    items.append(cleaned_text)
else:
    print("No se encontró el texto relacionado con 'Longitud'.")

if description_text:
    cleaned_text = description_text.replace("\n", " ")
    cleaned_text = cleaned_text.replace("  ", " ")
    items.append(cleaned_text)
else:
    print("No se encontró el texto relacionado con 'del peligro inminente'.")

print(items)

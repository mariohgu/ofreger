import re
from pdfminer.high_level import extract_text

# pip install pdfminer.six
from io import BytesIO


def extract_using_regex(pattern, text):
    """Extrae el texto usando una expresión regular."""
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1)
    return None


def process_pdf(file):
    # Convertir el archivo cargado en un objeto BytesIO para que pdfminer pueda procesarlo
    file_bytes = BytesIO(file.read())

    # Extraer texto del archivo PDF
    text = extract_text(file_bytes)

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

    return items

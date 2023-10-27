import re
import os
from pdfminer.high_level import extract_text

file = os.path.dirname(__file__)
pdf_path = os.path.join(file, 'documentos', '02.pdf')


text = extract_text(pdf_path)
print(text)
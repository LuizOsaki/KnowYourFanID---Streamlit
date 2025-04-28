import pytesseract
from PIL import Image
import re

def validate_document(file_path):
    try:
        img=Image.open(file_path)
        text=pytesseract.image_to_string(img)

        #Busca simples de CPF no texto extraído
        cpf_pattern=r'\d{3}\.\d{3}\.\d{3}-\d{2}'
        cpf_found=re.findall(cpf_pattern, text)

        return{
            "document_text_excerpt":
            text[:300],
            "cpf_detetected":
            bool(cpf_found),
            "cpf_numbers":cpf_found
        }
    except Exception as e:
        return {"error": str(e)}
from PyPDF2 import PdfReader
from tqdm import tqdm
import os


def f22() -> int:
    file = 'NF -.pdf'
    with open(file, 'rb') as file_bin:
        pdf = PdfReader(file_bin)
        page = pdf.pages[0]
        rows = page.extract_text().split('\n')
        



        
        cnpj = ''.join(char for char in rows[25] if char.isnumeric())
        cnpj = cnpj[4:]
        nome = rows[20]
        print(cnpj)
        print(nome)
        new_path = f'NF {nome}-{cnpj}.pdf'
        os.rename(file, new_path)

        
f22()
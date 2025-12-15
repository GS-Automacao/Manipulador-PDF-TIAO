from PyPDF2 import PdfReader
from tqdm import tqdm
import re
import os


def pegar_numeros(texto: str):
    return ''.join(re.findall(r'\d+', str(texto)))

def pegar_texto(texto: str):
    return ''.join(re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ ]+', str(texto)))

def f27() -> int:
    file = '-22121.pdf'
    
    with open(file, 'rb') as file_bin:
        pdf = PdfReader(file_bin)
        page = pdf.pages[0]
        text = page.extract_text().split('\n')
        for i in enumerate(text):
            print(i)
            
    
f27()
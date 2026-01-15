from PyPDF2 import PdfReader
from tqdm import tqdm
import re
import os

def pegar_maiusculas(texto: str) -> str:
    return ''.join(re.findall(r'[A-ZÀ-ÖØ-Þ ]', texto))


def pegar_numeros(texto: str):
    return ''.join(re.findall(r'\d+', str(texto)))

def pegar_texto(texto: str):
    return ''.join(re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ ]+', str(texto)))

def f27() -> int:
    file = 'NF - CONDOMINIO COSTA MAREE.pdf'

    palavras_ignoradas = ['E-mail', 'Email']
    
    with open(file, 'rb') as file_bin:
        pdf = PdfReader(file_bin)
        page = pdf.pages[0]
        text = page.extract_text().split('\n')
        
        cliente = text[37]
        cliente = cliente.split()
        cliente = ' '.join(cliente)
        cliente = pegar_texto(cliente)
        if any(palavra in cliente for palavra in palavras_ignoradas):
            cliente = cliente.replace('E-mail', '').replace('Email', '').strip()
        cliente = pegar_maiusculas(cliente)
        print(cliente)
 


f27()
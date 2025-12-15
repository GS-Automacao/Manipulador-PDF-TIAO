from PyPDF2 import PdfReader
from tqdm import tqdm
import os
import re

def pegar_numeros(texto: str):
    return ''.join(re.findall(r'\d+', str(texto)))

def pegar_texto(texto: str):
    return ''.join(re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ ]+', str(texto)))


def f25() -> int:
    files = [file for file in os.listdir() if file.lower().endswith('.pdf')]
    n_arqs = len(files)
    for file in tqdm(files):
        with open(file, 'rb') as file_bin:
            pdf = PdfReader(file_bin)
            rows = pdf.pages[0].extract_text().split('\n')
        for row in rows:
            if 'Data de Emissão' in row:
                num_nf = row.split()[0]
                break
        for row in rows[::-1]:
            if 'Nome/Razão Social' in row:
                nome_cliente = row[18:]
                nome_cliente = nome_cliente.translate(str.maketrans({'/': '', '\\': '', '|': ''}))
                novo_nome = f'{nome_cliente}-{num_nf}.pdf'
                os.rename(file, novo_nome)
                break
        
            elif 'Número da Nota' in rows:
                n_nota = rows[4]
                n_nota = pegar_numeros(n_nota)
                nome_cliente = rows[19].split(':')
                nome_cliente = nome_cliente[1:]
                nome_cliente = pegar_texto(nome_cliente)
                novo_nome = f'{nome_cliente}-{n_nota}.pdf'
                os.rename(file, novo_nome)
                break

            else:
                n_nota2 = rows[4]
                n_nota2 = pegar_numeros(n_nota2)
                nome_cliente2 = rows[18].split()
                nome_cliente2 = nome_cliente2[2:]
                nome_cliente2 = pegar_texto(nome_cliente2)
                novo_nome = f'{nome_cliente2}-{n_nota2}.pdf'
                os.rename(file, novo_nome)
                break
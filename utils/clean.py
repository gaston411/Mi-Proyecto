"""
Paquete donde se guardan todas las funcinoes utilizadas para la limipeza de
los textos.
"""

import nltk
import re
import json
from utils import utils_fun

stops = nltk.corpus.stopwords.words('spanish')
# black_list = json.load(open('black_list.json', 'r'))['black_list']
# black_list = json.load(open('utils/black_list.json', 'r'))['black_list']
#black_list = utils_fun.open_json('utils/black_list.json')['black_list']


def remove_stops(texto: str) -> str:
    """
    Función que elimina stopwords
    Params:
        **texto**:texto a ser limpiado de stopwords

    """
    texto = [
        i for i in texto.split() if i not in stops
    ]
    return ' '.join(texto)


def general(txt: str, bert=False, nums=False) -> str:
    """
    Elimina caracteres no deseados
    Params:
        **txt**:texto a ser limpiado de caracteres no desaeados
    """
    if nums:
        txt = re.sub(r'\d+', ' ', txt)
    if not bert:
        txt = txt.translate(str.maketrans(
            'áéíóúýàèìòùÁÉÍÓÚÀÈÌÒÙÝ', 'aeiouyaeiouAEIOUAEIOUY'))
        txt = txt.lower()
        txt = re.sub(r'[^\w\s]', '', txt)

    txt = txt.replace('\r', ' ').replace('\n', ' ').replace("\v", ' ').replace(
        "\t", ' ').replace("\f", ' ').replace("\a", ' ').replace("\b", ' ')
    txt = re.sub(' +', ' ', txt)
    txt = txt.strip()
    return txt



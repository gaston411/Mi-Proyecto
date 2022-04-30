import json
from database import sql
from typing import List, Dict, Optional
import re


def open_json(json_path: str, encoding: Optional[str] = None) -> Dict:
    """Función utilitaria para abrir jsons

    Params:
        **json_path**: dirección del archivo a abrir
    Returns:
        **aux**: diccionario de python parseado del json
        **encoding**: tipo de encodign a utilizar. Ej.: "utf-8"
    """
    with open(json_path, "r", encoding=encoding) as f:
        aux = json.load(f)
    return aux


def save_json(newDictionary: Dict, name_file: str, encoding: Optional = None) -> None:
    """
        Guarda un diccionario con su nombre de archivo que recibe como parametro como un archivo json
    Params:
        **newDictionary**: diccionario de python para guardar como json
        **name_file**: path del json donde será guardado

    ```
    python_dict = {'a':0, 'b':1}
    save_json(python_dict, 'path/to/json/save')
    ```

    """
    with open(name_file, "w", encoding=encoding) as outfile:
        json.dump(newDictionary, outfile)


def get_context(central_word: str, sentence: str, window_word: int = 15, **flags) -> List:
    """devuelve contextos de numeros

    :returns: list

    """
    context = []
    aux = re.findall(
        central_word,
        sentence,
        **flags)
    t = sentence.split()

    for symbol in aux:
        for i, word in enumerate(t):
            if re.search(symbol, word):
                context.append(
                    ' '.join(t[i - window_word:i + window_word]))
    return list(set(context))

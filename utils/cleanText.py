'''
Se hace la eliminacion de texto entre corchetes, acentos, signos de puntuacion (excepto . y :), palabras con numeros.
Se eliminan los espacios de sobra
Se eliminan \r, \t, \v, \f, \a
'''
import re, string, unicodedata

def limpiarTexto1(txt: str, bert=False, nums=False) -> str:
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

    '''
    Eliminamos caracteres especiales: tabulador horizontal(\t), tabulador vertical(\v), 
    retorno de carro(\r), avance de pagina(\f), 
    caracter de retroceso: Marca el límite de una palabra(\b), 
    '''
    txt = txt.replace('\r', ' ').replace("\v", ' ').replace(
        "\t", ' ').replace("\f", ' ').replace("\a", ' ').replace("\b", ' ')
    txt = re.sub(' +', ' ', txt)
    txt = txt.strip()
    return txt

def limpiarTexto2(text:str) -> str:
    """
    Elimina caracteres no deseados
    Limpia caracteres numéricos, saltos de línea, saltos de página, correo electrónico
    Params:
        **txt**:texto a ser limpiado de caracteres no desaeados
    """
    text = re.sub('\d\n','',text)
    text = re.sub(' +\n','\n',text)
    text = re.sub('\n+','\n',text)
    text = re.sub('\n',' \n',text)
    text = re.sub('\d \n','',text)
    text = re.sub('\x0c','',text)
    text = re.sub('\u200b\n','',text)
    text = re.sub(r'[nN]º|[nN][. ]º','',text)
    text = re.sub('[a-zA-Z]+.com','',text)
    text = re.sub('\d{2,15}','',text)
    return text

import re

def limpiarTexto3(text: str, bert=False, nums=False) -> str:
    """
    Elimina palabras no deseados
    Params:
        **text**:texto a ser limpiado de palabras no desaeadas
    """
    text = re.sub('[a-z1-9.]+[).-] [s|S]e encuentra contestad[a|o] .+[. \n]','',text)
    text = re.sub('[0-9]+[. ]+[yY]a fue contestado.+[.\n]','',text)
    text = re.sub('[fF]oja [1-9].+\n', '', text)
    text = re.sub('[pP]regunta[ 0-9]+[)].+\n|[rR]espuesta[ 0-9]+[)].+\n','',text)#elimina oraciones comenzadas en preguta/respuesta.
    text = re.sub('V[. ]+[S\n\.]+', '', text)
    text = re.sub('[A-Z][.][A-Z][.]','',text)
    return text

# limpiar titulos
def limpiar_palabras(text: str) -> str:
    '''
    Limpiar palabras en títulos. Solamente deja palabras y espacios en blanco.
    Params:
        **text**:texto a ser limpiado de palabras no desaeadas
    '''
    text = re.sub(r'(I{1,3}|IV|V|VI{1,4}|IX|X)[). -]|[^\w\s]',' ',text)
    text=text.lower()
    text = [
        i for i in text.split() if len(i) > 3
    ]
    return ' '.join(text)

# Limpieza de texto de los expedientes sin títulos en números romanos y mayúsculas
import re, string, unicodedata

def limpiarDfSinTitulos(txt: str, bert=False, nums=False) -> str:
    '''
    Limpiar palabras en títulos. Solamente deja palabras, espacios en blanco, numeros, -, ).
    Params:
        **text**:texto a ser limpiado de palabras no desaeadas
    '''
    if not bert:
        txt = txt.translate(str.maketrans(
            'áéíóúýàèìòùÁÉÍÓÚÀÈÌÒÙÝ', 'aeiouyaeiouAEIOUAEIOUY'))

    txt = txt.replace('\r', ' ').replace("\v", ' ').replace(
        "\t", ' ').replace("\f", ' ').replace("\a", ' ').replace("\b", ' ')
    txt = re.sub(' +', ' ', txt)
    txt = re.sub('\n+', '\n', txt)
    txt = re.sub(r'[^\w\.\s\d)-]', '', txt)
    txt = re.sub(r'[A-Z][\.][A-Z][\.]', '', txt)
    txt = txt.strip()
    return txt


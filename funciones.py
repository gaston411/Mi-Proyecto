'''

Busqueda de titulos - opcion no utilizada para buscar numeros romanos.
Se crea un nuevo dataframe de titulos según distintos criterios.
busca titulos que comienzan con numeros romanos.

'''
def buscarTitulosRomanos(text):
    # Expresiones regulares para encontrar los numeros romanos
    tituloNroRomano =re.compile(r'([iI]{1,3}[-.)]+[A-Z-a-z ]+)|([iI][vV][-.)]+[\D][\w\s]+)|([vV][iI]{1,3}[-.)]+[\w\s]+)')# I a IV (excepto V y X)
    titulosNroRomanoVX = re.compile(r'[\W][vV][-.)]+[\w+\s]+|[\W][xX][-.)]+[\w\s]+[:\n]')# V y X
    titulosRomanosEncontrados = []
    for m in tituloNroRomano.finditer(text):
        titulosRomanosEncontrados.append(m.group())
    
    #el método finditer, que devuelve un iterador que podemos usar en el bucle for:
    # cada m es un objeto tipo matcher ... print m.groups()
    for m in titulosNroRomanoVX.finditer(text):
        titulosRomanosEncontrados.append(m.group())

    return titulosRomanosEncontrados

# titulosConNroRomano: lista que guarda los titulos que comienzan con numeros romanos   
titulosConNroRomano=[]
for expediente in dfLimpio:
    titulosConNroRomano.append(buscarTitulosRomanos(expediente))



#crear un dataframe a partir de varias listas.
# crear un df de titulos.
import pandas as pd 

titulos = list(zip(titulosMayusculasStop, titulosConNroRomanoStop, titulosConNroLatinoStop))
dfTitulos = pd.DataFrame(titulos, columns=['mayusculas','romanos', 'latinos'])


#dfTitulos.dtypes
#dfTitulos.info()
#dfTitulos.describe()



'''
Crear n-gramas
'''
from nltk import ngrams

sentence = 'this is a foo bar sentences and i want to ngramize it'

n = 6
sixgrams = ngrams(sentence.split(), n)

for grams in sixgrams:
  print grams




'''
Crear nube de palabras
'''
# Import the wordcloud library
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Join the different processed titles together.
long_string = ','.join(list(df1[0]))

# Create a WordCloud object
wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')

# Generate a word cloud
wordcloud.generate(long_string)

# Visualize the word cloud
wordcloud.to_image()


'''
convertir en excel un df
'''
from pandas import ExcelWriter

writer = ExcelWriter('E:/Descargas-E/titulos_en_mayusculas.xlsx')
dfTitulosMayusculasConStops.to_excel(writer, 'Hoja de datos', index=False)
writer.save()



# funcion para encontrar titulos
# Encontrar la ubicacion del titulo en el documento
titulosPosicion=[]

for titulo in titulosMayusculas[0]:
    inicioTitulo = dfLimpio[0].index(titulo)
    palabrasPorTitulo = len(titulo)
    finalTitulo = inicio + palabrasPorTitulo
    titulosPosicion.append((titulo, inicioTitulo, finalTitulo, palabrasPorTitulo))

pprint(titulosPosicion)





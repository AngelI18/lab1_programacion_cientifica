import string

class diccionario:
    caracteres_acentados = {
        'á' : 'a',
        'é' : 'e',
        'í' : 'i',
        'ó' : 'o',
        'ú' : 'u',
        'ü' : 'u'
        }

    caracteres_especiales = set(string.punctuation + '¡¿´¨{}')
    arch = open("stopwords","r")
    stop_words = arch.read().split('\n')
    arch.close()

def normalizarTexto(texto):
    d = diccionario

    newTexto = ""
    for i in range(len(texto)):
        if texto[i] in d.caracteres_acentados:
            newTexto += d.caracteres_acentados[texto[i]]
        elif texto[i] in d.caracteres_especiales:
            newTexto += ""
        else:
            newTexto += texto[i]
    palabras = newTexto.split(' ')
    palabrasFiltradas = [palabra for palabra in palabras if palabra not in d.stop_words]

    return palabrasFiltradas
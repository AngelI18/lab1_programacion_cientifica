__all__ = ['CalculoDelTF']

def CalculoDelTF(documento, bag_of_words):
    
    bag_of_words = list(set(bag_of_words))
    lista_tf = []
    total_palabras = len(documento)
    
    for palabra in bag_of_words:
        # frecuencia relativa
        tf = documento.count(palabra) / total_palabras
        lista_tf.append(tf)
    
    return lista_tf

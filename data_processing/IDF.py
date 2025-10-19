__all__ = ['CalculoIDF']

def CalculoIDF(documentos, bag_of_words):
    import math  
    N = len(documentos)
    idf_lista = []

    for palabra in bag_of_words:
        numero_de_documetos_palabra = 0
        for doc in documentos:
            if palabra in doc:
                n_w += 1
        # IDF logaritmo natural
        idf = math.log(N / (1 + numero_de_documetos_palabra))
        idf_lista.append(idf)
    
    return idf_lista
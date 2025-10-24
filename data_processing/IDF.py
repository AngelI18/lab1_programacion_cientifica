import math

__all__ = ['calculoIdf']

import math

def calculoIdf(lista_doc):
    largo_corpus = len(lista_doc)
    idf = {}

    for doc in lista_doc:
        for palabra in set(doc):
            if palabra not in idf:
                idf[palabra] = 0
            idf[palabra] += 1  

    for palabra, df in idf.items():
        idf[palabra] = math.log(largo_corpus / (1 + df))

    return idf



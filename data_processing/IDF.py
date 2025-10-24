import math

__all__ = ['calculoIdf']

def calculoIdf(lista_doc):

    largo_corpus = len(lista_doc)
    idf = {}

    for doc in lista_doc:
        for palabra in set(doc):  
            idf[palabra] = idf.get(palabra, 0) + 1

    for palabra, df in idf.items():
        idf[palabra] = math.log(largo_corpus / (1 + df))

    return idf


import math
__all__ = ['CalculoIDF']

def CalculoIDF(corpus):
    num_doc = len(corpus)
    doc_frec = {}
    for doc in corpus:
        words_unique = set(doc)
        for word in words_unique:
            doc_frec[word] +=1
    
    inv_doc_frec = {word : math.log(num_doc/(1+doc_count)) for word, doc_count in doc_frec.items()}
    return inv_doc_frec
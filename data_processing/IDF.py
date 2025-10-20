import math
__all__ = ['IDF_corpus']

def IDF_corpus(corpus):
    if not corpus or all(isinstance(word,str) for word in corpus):
        print('IDF no es calculable, no hay un corpus de documentos')
        return {}

    num_doc = len(corpus)
    doc_frec = {}
    for doc in corpus:
        words_unique = set(doc)
        for word in words_unique:
            doc_frec[word] = doc_frec.get(word,0) + 1
    
    inv_doc_frec = {word : math.log(num_doc/(1+doc_count)) for word, doc_count in doc_frec.items()}
    return inv_doc_frec
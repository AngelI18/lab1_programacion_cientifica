__all__ = ['TF_corpus','TF_doc']

def TF_doc(doc):
    if not doc:
        return {}
    length = len(doc)
    word_counter = {}
    for word in doc:
        word_counter[word] = word_counter.get(word,0) + 1
    return {word: (count/length) for word, count in word_counter.items()}

def TF_corpus(corpus):
    list_doc_tf = []
    count = 1
    for doc in corpus:
        tf = TF_doc(doc)
        if tf:
            list_doc_tf.append(tf)
        else:
            print(f'doc_{count}_normalizado vacio')
        count +=1

    return list_doc_tf
    
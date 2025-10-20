from collections import Counter

__all__ = ['TF']

def TF(doc):
    length = len(doc)
    word_counter = Counter(doc)
    tf = {word: (count/length) for word, count in word_counter.items()}
    return tf
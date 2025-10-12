__all__ = ['delete_stop_words_es','delete_stop_words_en']

class _stop_words:
    def __init__(self, words):
        self.words = set(words)
    
    @classmethod
    def spanish(cls):
        with open('data/stop_words_spanish.txt','r',encoding='UTF-8') as arch:
            words_list = [line.strip() for line in arch if line.strip()]
        return cls(words_list)
    @classmethod
    def english(cls):
        with open("data/stop_words_english.txt","r") as arch :
            words_list = [line.strip() for line in arch if line.strip()]
        return cls(words_list)


def delete_stop_words_es(tokens):
    stop_words_es = _stop_words.spanish()
    return [word for word in tokens if word not in stop_words_es.words]
    


def delete_stop_words_en(tokens):
    stop_words_en = _stop_words.english()
    return [word for word in tokens if word not in stop_words_en.words]
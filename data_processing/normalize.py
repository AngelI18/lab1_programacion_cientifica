import string

__all__ = ['normalize_text']

class _diccionary:

    def __init__(self):
        self.caracteres_acentados = self._cargar_caracteres_acentados()
        self.caracteres_especiales = set(string.punctuation + '¡¿´¨{}')-{'\n','\r',' '}
        self.contractions = self._carga_contracciones()

    def _cargar_caracteres_acentados(self):
        caracteres_acentados = {
            'á' : 'a',
            'é' : 'e',
            'í' : 'i',
            'ó' : 'o',
            'ú' : 'u',
            'ü' : 'u',
            'à' : 'a',
            'è' : 'e',
            'ì' : 'i',
            'ò' : 'o',
            'ù' : 'u',
            'â' : 'a',
            'ê' : 'e',
            'î' : 'i',
            'ô' : 'o',
            'û' : 'u',
            'ä' : 'a',
            'ë' : 'e',
            'ï' : 'i',
            'ö' : 'o'
            }
        return caracteres_acentados

    def _carga_contracciones(self):
        with open('data/contractions_english.txt','r') as arch:
            contractions = {part[0].strip():part[1].strip() for part in 
                             [line.strip().split('=') for line in arch if line.strip() and '=' in line]
                             if len(part)==2}
        return contractions

def _isDigit(value):
    try:
        value = int(value)
        return True
    except:
        return False


def _expansion(text, diccionary_instance):
    lines = text.split('\n')
    new_text = ''
    long_lines = len(lines)
    for i in range(long_lines):
        words = lines[i].split()
        long_words = len(words)
        for j in range(long_words):

            match words[j]:
                case c if j + 1 < long_words and c in diccionary_instance.contractions:
                    new_text += diccionary_instance.contractions[c]+' '
                case c if j + 1 < long_words:
                    new_text += c + ' '
                case c if j + 1 == long_words and c in diccionary_instance.contractions:
                    new_text += diccionary_instance.contractions[c] + '\n'
                case _:
                    new_text += c + '\n' 

    return new_text

def normalize(texto, language):
    
    diccionary_instance = _diccionary()
    texto = texto.lower()
    if language == 'en':
        texto = _expansion(texto)
    newTexto = ""
    largo = len(texto)
    for i in range(largo):
        char = texto[i]
        match char:

            case c if c in diccionary_instance.caracteres_acentados:
                newTexto += diccionary_instance.caracteres_acentados[c]
                print(diccionary_instance.caracteres_acentados[c])

            case ('.' | ',' | '-') if (i>0 and i+1 < largo and _isDigit(texto[i-1]) and _isDigit(texto[i+1])):

                newTexto += char

            case ' ' | '\n':

                newTexto += char
            
            case '-' if (i>0 and i+1 < largo and texto[i-1] != ' ' and texto[i+1] != ' '  and not _isDigit(texto[i-1]) and not _isDigit(texto[i+1])):

                newTexto +=  ' '

            case c if c in diccionary_instance.caracteres_especiales:

                newTexto += ''

            case _:
                newTexto += char
            

    return newTexto

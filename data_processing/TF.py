__all__ = ['CalculoDelTF']

def calcularTf(documento):
    dic_tf = {}
    for palabra in set(documento):
        dic_tf[palabra] = documento.count(palabra)/len(documento)
        
    return dic_tf
    

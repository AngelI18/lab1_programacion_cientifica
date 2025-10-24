__all__ = ['CalculoDelTF']


def OperacionTf(dic_data):
    dic_TF = {}
    for genero, lista_doc in dic_data.items():
        valor = 0
        dic_tf_documentos = {}
        for doc in lista_doc:
            dic_tf_documentos[str(valor)] = calcularTf(doc)
            valor += 1
        dic_TF[genero] = dic_tf_documentos
        
    return dic_TF

def calcularTf(documento):
    
    dic_tf = {}
    for palabra in set(documento):
        dic_tf[palabra] = documento.count(palabra)/len(documento)
        
    return dic_tf
    

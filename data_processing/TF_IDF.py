
def calcularTfIdf(dic_TF,dic_IDF):
    dic_TF_IDF = {}
    for genero, lista_doc_tf in dic_TF.items():
        idf_genero = dic_IDF[genero]  
        dic_tf_idf_documentos = {}
        
        for doc_id, tf_doc in lista_doc_tf.items():
            tf_idf_doc = {palabra: tf_val * idf_genero[palabra]
                        for palabra, tf_val in tf_doc.items()}
            dic_tf_idf_documentos[doc_id] = tf_idf_doc
        
        dic_TF_IDF[genero] = dic_tf_idf_documentos
    
    return dic_TF_IDF
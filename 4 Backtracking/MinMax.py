def MinMax(estado, nivel):
    if es_hoja(estado):
        return resultado(estado)
    
    if nivel == "Max":
        valor = float('-inf')
    else:
        valor = float('inf')
    
    for hijo in obtener_hijos(estado):
        if nivel == "Max":
            valor = max(valor, MinMax(hijo, "Min"))
        else:
            valor = min(valor, "Max")
    
    return valor


def es_hoja(estado):
    #Devuelve un booleano si el estado es un nodo hoja
    pass

def obtener_hijos(estado):
    #Devuelve la lista de los hijos de estado
    pass

def resultado(estado):
    #Devuelve el valor de estado
    pass
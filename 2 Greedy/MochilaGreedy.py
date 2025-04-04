def Mochila(objetos, peso_max):
    seleccionados = [0] * len(objetos)

    objetos.sort(valor/peso)

    peso_acumulado = 0
    i = 0

    while ((i < len(objetos)) and (peso_acumulado < peso_max)):
        seleccionados[i] = 1
        peso_acumulado += objetos[i].peso
        i += 1

def MochilaGreedy(pesos, valores, peso_max):
    seleccionados = [0] * len(pesos)

    # Ordenar manualmente los objetos según la relación valor/peso en orden descendente
    for i in range(len(pesos)):
        for j in range(i + 1, len(pesos)):
            if valores[i] / pesos[i] < valores[j] / pesos[j]:  
                
                pesos[i], pesos[j] = pesos[j], pesos[i]
                
                valores[i], valores[j] = valores[j], valores[i]

    peso_acumulado = 0
    i = 0

    while ((i < len(pesos)) and (peso_acumulado + pesos[i] <= peso_max)):
        seleccionados[i] = 1
        peso_acumulado += pesos[i]
        i += 1

    return seleccionados 

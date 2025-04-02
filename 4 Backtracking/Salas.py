#Se pide mediante un grafo direccionado, encontrar el camino más largo hacia la salida

def camino_mas_largo(salas, actual, salida, visitados, camino_actual, mejor_camino):
    visitados.add(actual)
    camino_actual.append(actual)

    if actual == salida:
        if len(camino_actual) > len(mejor_camino[0]):
            mejor_camino[0] = list(camino_actual)
    else:
        for vecino in salas.get(actual, []):
            if vecino not in visitados:
                camino_mas_largo(salas, vecino, salida, visitados, camino_actual, mejor_camino)
    
    visitados.remove(actual)
    camino_actual.pop()


def salas(salas, entrada, salida):
    mejor_camino = [[]]
    camino_mas_largo(salas, entrada, salida, set(), [], mejor_camino)
    return mejor_camino[0]

#Camino mas largo mediante Branch and Bound
def camino_mas_largo_BB(salas, actual, salida, visitados, camino_actual, mejor_camino):
    visitados.add(actual)
    camino_actual.append(actual)

    if actual == salida:
        if len(camino_actual) > len(mejor_camino[0]):
            mejor_camino = list(camino_actual)

    else:
        if len(camino_actual) + (len(salas) - len(visitados)) > len(mejor_camino[0]):
            vecinos_ordenados = sorted(salas.get(actual, []), key=lambda x: len(salas.get(x, [])), reverse=True)

            for vecino in vecinos_ordenados:
                if vecino not in visitados:
                    camino_mas_largo_BB(salas, vecino, salida, visitados, camino_actual, mejor_camino)

    visitados.remove(actual)
    camino_actual.pop()
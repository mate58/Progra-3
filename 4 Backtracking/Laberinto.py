#Dada una matriz, se nos pide llegar del 0,0 al n-1 m-1, pero solo se puede mover hacia la derecha o abajo
#siempre y cuando el numero sea 0, en caso de tener un 1 no se puede mover hacia ese lado

def encontrarCamino(matriz, i, j, camino_actual, mejor_camino):
    filas = len(matriz)
    columnas = len(matriz[0])

    if i >= filas or j >= columnas or matriz[i][j] == 1:
        return

    camino_actual.append((i, j))

    if i == filas - 1 and j == columnas - 1:
        if len(camino_actual) > len(mejor_camino[0]):
            mejor_camino[0] = list(camino_actual)
    else:
        encontrarCamino(matriz, i, j + 1, camino_actual, mejor_camino)
        encontrarCamino(matriz, i + 1, j, camino_actual, mejor_camino)

    camino_actual.pop()

def caminoMasLargo(matriz):
    mejor_camino = [[]]
    encontrarCamino(matriz, 0, 0, [], mejor_camino)
    return mejor_camino[0]

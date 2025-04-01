def PistaCilindrica(mat):
    filas = len(mat)
    columnas = len(mat[0])

    fila_actual = 0

    for i in range(filas):
        if mat[i][0] < mat[fila_actual][0]:
            fila_actual = i

    costo = mat[fila_actual][0]

    for j in range(1, columnas):
        if fila_actual == 0:
            opciones = [mat[fila_actual][j], mat[fila_actual + 1][j], mat[filas - 1][j]]
            if opciones[1] < opciones[0] and opciones[1] < opciones[2]:
                fila_actual += 1
            elif opciones[2] < opciones[0]:
                fila_actual = filas - 1

        elif fila_actual == filas - 1:
            opciones = [mat[fila_actual][j], mat[fila_actual - 1][j], mat[0][j]]
            if opciones[1] < opciones[0] and opciones[1] < opciones[2]:
                fila_actual -= 1
            elif opciones[2] < opciones[0]:
                fila_actual = 0

        else:
            opciones = [mat[fila_actual - 1][j], mat[fila_actual][j], mat[fila_actual + 1][j]]
            if opciones[0] < opciones[1] and opciones[0] < opciones[2]:
                fila_actual -= 1
            elif opciones[2] < opciones[1]:
                fila_actual += 1

        costo_total += mat[fila_actual][j]

    return costo_total



matriz_ejemplo = [
    [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 3, 2, 3],
    [0, 6, 1, 2]
]

print(PistaCilindrica(matriz_ejemplo))
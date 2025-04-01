def PistaCilindricaPro(mat):
    filas = len(mat)
    columnas = len(mat[0])

    dp = [[float('inf')] * columnas for _ in range(filas)]
    
    for i in range(filas):
        dp[i][0] = mat[i][0]

    for j in range(1, columnas):
        for i in range(filas):
            arriba = dp[(i-1) % filas][j-1]
            izquierda = dp[i][j-1]
            abajo = dp[(i+1) % filas][j-1]

            dp[i][j] = mat[i][j] + min(arriba, izquierda, abajo)
    
    costo_min = min(dp[i][-1] for i in range(filas))

    return costo_min


matriz_ejemplo = [
    [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 3, 2, 3],
    [0, 6, 1, 2]
]
print(PistaCilindricaPro(matriz_ejemplo))
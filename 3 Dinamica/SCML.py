def CrearMatriz(n, m):
    """Crea una matriz de n filas y m columnas, inicializada en 0."""
    matriz = [[0 for _ in range(m)] for _ in range(n)]
    return matriz

def MostrarMatriz(matriz):
    """Imprime la matriz en un formato legible."""
    for fila in matriz:
        print(" ".join(map(str, fila)))

def scml(x, y):
    """Calcula la longitud de la subsecuencia común más larga (LCS) entre dos cadenas."""
    n, m = len(x), len(y)
    mat = CrearMatriz(n + 1, m + 1)  # Matriz de (n+1) x (m+1) para manejar índices 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:  # Coincidencia de caracteres
                mat[i][j] = mat[i - 1][j - 1] + 1
            else:
                mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])  # Tomamos el máximo de arriba o izquierda
    
    return mat[n][m]  # El resultado está en la última celda de la matriz

# Ejemplo de uso:
cadena1 = "AGGTAB"
cadena2 = "GXTXAYB"
print(scml(cadena1, cadena2))  # Output esperado: 4 (GTAB)



def levenshtein(A, B):
    m, n = len(A), len(B)
    
    # Crear la tabla DP de tamaño (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Inicializar la primera fila y columna
    for i in range(m + 1):
        dp[i][0] = i  # Convertir A[0:i] a cadena vacía requiere i eliminaciones
    for j in range(n + 1):
        dp[0][j] = j  # Convertir cadena vacía a B[0:j] requiere j inserciones
    
    # Llenar la tabla DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:  # Si los caracteres son iguales, no hay costo
                dp[i][j] = dp[i - 1][j - 1]
            else:
                insert = dp[i][j - 1] + 1  # Insertar en A
                delete = dp[i - 1][j] + 1  # Eliminar en A
                replace = dp[i - 1][j - 1] + 1  # Reemplazar en A
                dp[i][j] = min(insert, delete, replace)  # Tomar la mejor opción
    
    return dp[m][n]  # La distancia óptima está en dp[m][n]

# Ejemplo de uso
A = "berna"
B = "berlín"
print("Distancia de Levenshtein:", levenshtein(A, B))

def MochilaDP(pesos, valores, peso_max):
    dp = [[0] * (peso_max + 1) for _ in range(len(pesos))]

    for i in range(len(pesos)):
        for j in range(peso_max + 1):
            if i == 0:
                if pesos[i] > j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = valores[i]
            else:
                if pesos[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j - pesos[i] + valores[i]])
    
    return dp[len(pesos)][peso_max]
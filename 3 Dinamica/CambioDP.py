def CambioDP(monedas, vuelto):
    dp = [[float('inf')] * (vuelto + 1) for _ in range(len(monedas))]

    for i in range(len(monedas)):
        for j in range(vuelto + 1):
            if i == 0:
                if j == 0:
                    dp[i][j] = 0
                elif monedas[i] > j:
                    dp[i][j] = float('inf')
                else:
                    dp[i][j] = dp[i][j-monedas[i]] + 1
            else:
                if monedas[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-monedas[i]] + 1)
    return dp[len(monedas) -1][vuelto]
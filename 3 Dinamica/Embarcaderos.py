
def Embarcaderos(n, costos):
    dp = [float('inf')] * n
    dp[0] = 0

    for j in range(1, n):
        for i in range(j):
            if costos[i][j] != -1:
                dp[j] = min(dp[j], dp[i] + costos[i][j])

    return dp[n-1]
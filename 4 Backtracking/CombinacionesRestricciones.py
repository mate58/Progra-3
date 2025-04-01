def ComRes(sol, usados, actual, n):
    if len(actual) == 2*n:
        print(sol)
        return
    
    for x in range(1, n+1):
        if usados[x] < 2:
            i = 0
            while i < 2*n and sol[i] != -1:
                i += 1
            if i < 2 * n and usados[x] == 0 and (i + x + 1 < 2 * n) and sol[i + x + 1] == -1:
                sol[i] = x
                sol[i + x + 1] = x
                usados[x] += 2
                ComRes(sol, usados, actual + 2, n)
                usados[x] -= 2
                sol[i] = -1
                sol[i + x + 1] = -1
            

def ejercicio(n):
    sol = [-1] * (n * 2)
    usados = [0] * (n + 1)
    ComRes(sol, usados, 0, n)    
    

ejercicio(3)
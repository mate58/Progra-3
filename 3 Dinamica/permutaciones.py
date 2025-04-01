def permutaciones(n, sol, usados):
    if len(sol) == n:
        print(sol)
        return
    
    for i in range(1, n+1):
        if i not in usados:
            sol.append(i)
            usados.add(i)
            permutaciones(n, sol, usados)

            sol.pop()
            usados.remove(i)


def problema(n):
    permutaciones(n,[], set())


problema(4)



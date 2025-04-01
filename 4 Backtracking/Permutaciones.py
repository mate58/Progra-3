#Dado un digito n, se pide hallar las permutaciones posibles tales que no se repita ningun numero y 
#la diferencia absoluta entre el digito y su precedente sea menor o igual a 2

def Permutaciones(n, usados, sol):
    if len(sol) == n:
        print(sol)
        return
    else:
        for i in range(1, n+1):
            if i not in usados:
                if not sol or abs(sol[-1] - i) <= 2:
                    sol.append(i)
                    usados.add(i)
                    Permutaciones(n, usados, sol)
                    sol.pop()
                    usados.remove(i)

def ejercicio(n):
    Permutaciones(n, set(), [])

ejercicio(4)
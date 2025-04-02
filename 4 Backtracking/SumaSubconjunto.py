#Algoritmo que mediante un parametro m, te devuelve los subconjuntos cuya suma sea igual a m

def SubSetSum(v,actSol, m, etapa, actSum):
    for i in range(2):
        actSol[etapa] = i
        newSum = actSum + v[etapa] * i
        if etapa == len(v) - 1:
            if newSum == m:
                print([v[j] for j in range(len(v)) if actSol[j] == 1])
        else:
            if newSum <= m:
                SubSetSum(v, actSol, m, etapa+1, newSum)



v = [3, 34, 4, 12, 5, 2]
m = 6
actSol = [0] * len(v)
print(f"Subconjuntos que suman {m}:")
SubSetSum(v, actSol, m, 0, 0)

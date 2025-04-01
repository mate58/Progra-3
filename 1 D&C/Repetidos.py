def Repetidos(p, i , f):

    if (i == f):
        return i
    mid = (i + f) // 2

    cont = 0
    
    for num in p:
        if i <= num <= mid:
            cont += 1

    if cont > (mid - i +1):
        return Repetidos(p, i, mid)
    else:
        return Repetidos(p, mid+1, f)
    
def Encontrar_repetido(P):
    return Repetidos(P, 0, len(P)-1)

def Repetidos_2(P, i):
    if P[i] == P.index(i):
        return Repetidos_2(P, i+1)
    else:
        return P[i]

lista = [0,1,2,3,3,4,5,6]

print(Encontrar_repetido(lista))
print(Repetidos_2(lista, 0))


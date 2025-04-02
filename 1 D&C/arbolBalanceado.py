#Dado un array con numeros ordenados de menor a mayor, devuelve un arbol balanceado

def arbolBalanceado(v, ini, fin, arbol):
    if ini > fin:
        return
    else:
        mid = (ini + fin) // 2
        arbol.agregar(v[mid])
        arbolBalanceado(v,ini, mid-1, arbol)
        arbolBalanceado(v, mid+1, fin, arbol)

def ejercicio(v):
    arbol = arbol.inicializarArbol()
    arbolBalanceado(v, 0, len(v), arbol)
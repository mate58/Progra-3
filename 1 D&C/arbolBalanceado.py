def arbolBalanceado(v, ini, fin):
    if (len(v) == 1):
        arbol.agregar(v[0])
    else:
        mid = (ini+fin) // 2
        arbol.agregar(v[mid])
        arbolBalanceado(v, 0, mid-1)
        arbolBalanceado(v. mid+1, len(v))
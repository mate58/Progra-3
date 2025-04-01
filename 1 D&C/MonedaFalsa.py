def MonedaFalsa(M, ini, fin):
    if ini == fin: 
        return ini

    n = fin - ini + 1 
    mitad = n // 2  

    grupo1 = M[ini:ini + mitad] 
    grupo2 = M[ini + mitad:ini + 2 * mitad]
    resto = M[ini + 2 * mitad:fin + 1]  

    if sum(grupo1) > sum(grupo2):  
        return MonedaFalsa(M, ini, ini + mitad - 1)
    elif sum(grupo1) < sum(grupo2):
        return MonedaFalsa(M, ini + mitad, ini + 2 * mitad - 1)
    else: 
        return MonedaFalsa(M, ini + 2 * mitad, fin)


monedas = [5, 5, 5, 6, 5, 5, 5, 5] 
indice = MonedaFalsa(monedas, 0, len(monedas) - 1)
print(f"La moneda falsa está en la posición: {indice}")

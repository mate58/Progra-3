def Piano(inicios, finales, actual, n):
    prox = actual + 1
    while prox < n and inicios[prox] >= finales[actual]:
        prox += 1
    
    if prox < n:
        return prox + Piano(inicios, finales, prox, n)
    return []


def ejercicio(inicios, finales):
    Piano(inicios, finales, 0, len(inicios))

 
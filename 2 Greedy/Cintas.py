#Es una especie de árbol huffman

def Cintas(cintas):
    total_movimientos = 0

    while (len(cintas) > 1):
        cintas.sort()
        c1 = cintas.pop(0)
        c2 = cintas.pop(0)

        movimiento = c1 + c2
        total_movimientos += movimiento
        cintas.append(movimiento)

    return total_movimientos

n = [30,20,10]

print(Cintas(n))
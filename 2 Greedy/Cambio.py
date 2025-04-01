def Cambio(monedas, pago):
    cambio = [0] * len(monedas)
    for i in range(len(monedas)):
        while pago >= monedas[i]:
            pago -= monedas[i]
            cambio[i] += 1
    print(pago)
    return cambio

def CambioPro(monedas, pago):
    cambio = [0] * len(monedas)
    for i in range(len(monedas)):
        if pago >= monedas[i]:
            cambio[i] = pago // monedas[i]
            pago = cambio[i] * monedas[i]

    return cambio

monedas = [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.01]

print(Cambio(monedas, 8.78))
print(CambioPro(monedas, 8.78))
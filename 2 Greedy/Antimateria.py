def Antimateria(k):
    cont = 0
    while k != 1:
        if k % 2 == 0:
            cont += 1
            k = k//2
        elif k < 1:
            k += 1
            cont += 1
        else:
            k -= 1
            cont += 1

    print(f"k es igual a {k} y el contador es {cont}")



def AntimateriaPro(k):
    cont = 0
    while k != 1:
        if k % 2 == 0:
            k //= 2
        elif k == 3 or k % 4 == 1:
            k -= 1
        else:
            k += 1
        cont += 1
    print(f"k es igual a {k} y el contador es {cont}")
    
Antimateria(7)
AntimateriaPro(7)
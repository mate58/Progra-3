def RaizEntera(n, ini, fin):
    if ini > fin:
        return fin
    else:
        mid = (ini + fin) // 2
        if (mid * mid) == n:
            return mid
        if (mid * mid) > n:
            return RaizEntera(n, ini, mid-1)
        else:
            return RaizEntera(n, mid+1, fin)

def ejercicio(n):
    print(RaizEntera(n, 0, n))

ejercicio(18)
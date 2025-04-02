def encontrarRaiz(p, b):
    mid = (p + b) // 2
    if (mid == 0):
        return mid
    else:
        if(mid > 0):
            return encontrarRaiz(mid + 1, b)
        else:
            return encontrarRaiz(p, mid-1)

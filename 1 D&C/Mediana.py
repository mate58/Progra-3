def mediana(iniX, finX, iniY, finY, x, y):
    if (finX - iniX == 1):
        return (max(x[iniX], y[iniY]) + min(x[finX], y[finY]) ) / 2

    else:
        midX = (iniX + finX) // 2
        midY = (iniY + finY) // 2

        if x[midX] == y[midY]:
            return x[midX]
        elif x[midX] > y[midY]:
            return mediana(iniX, midX, midY, finY)
        else:
            return mediana(midX, finX, iniY, midY)

    
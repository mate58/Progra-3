#Dado un vector con numeros v, devuelve los subconjuntos cuya suma sean iguales de ambos lados

def ParticionRec(v, s, e):
    for i in range(2):
        s[e] = i
        if e == len(v) -1:
            s1 = 0
            s2 = 0
            for j in range(len(v)):
                if s[j] == 0:
                    s1 += v[j]
                else:
                    s2 += v[j]
            if s1 == s2: #Condicion de printeo
                print(s)
        else:
            ParticionRec(v, s, e+1)


def ParticionSumaIguales(v):
    s = [0] * len(v)
    ParticionRec(v, s, 0)




vec = [1,2,3,4]

ParticionSumaIguales(vec)
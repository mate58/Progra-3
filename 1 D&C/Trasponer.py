#Dado un vector V, y un numero K, se pide trasponer los primeros k elementos a las posiciones n-k
def Trasponer(v, k):
    v[:k] = reversed(v[:k])
    v[k:] = reversed(v[k:])
    v.reverse()
    print(v)

#Tambien se podria hacer de un metodo "greedy"
def traponer_greedy(v, k):
    for i in range(k):
        v.append(v.pop(0)) #Agrega al final el que elimina al principio




k = 3
v = [1,2,3,4,5,6,7]

traponer_greedy(v,k)
print(v)    
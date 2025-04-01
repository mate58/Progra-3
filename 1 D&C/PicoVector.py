def PicoVector(V, ini, fin):
    if ini == fin:
        return V[ini]
    
    mid = (ini + fin) // 2

    if V[mid] >= V[mid-1] and V[mid] >= V[mid+1]:
        return V[mid]
    elif V[mid] < V[mid-1]:
        return PicoVector(V, ini, mid-1)
    else:
        return PicoVector(V, mid+1, fin)
    
def pico(arr):
    return PicoVector(arr, 0, len(arr) - 1)

# Ejemplo de uso
arr = [0, 1, 3, 2, 5, 1, 0]
print("Un pico encontrado:", pico(arr))
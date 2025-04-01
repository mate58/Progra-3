#PROGRAMACION DINAMICA, NOS DAN UNA VARILLA DE TAMAÑO N, CON UNA LISTA QUE DICE CUANTO VALE LA VARILLA EN UN TAMAÑO K

def cortar_varillas(tam_var, lista_p):
    tabla = [0] * (tam_var + 1)

    for va in range(1, tam_var + 1): #va -> varilla actual
        mejor_val = 0 #mejor valor
        for i in range(1, va + 1):
            val = lista_p[i] + tabla[va - i]
            if val > mejor_val:
                mejor_val = val
        tabla[va] = mejor_val

    return tabla[tam_var]


def cortar_varilla2(tam_var, lista_p, memory):
    if tam_var == 0:
        return 0
    if memory[tam_var] != -1:
        return memory[tam_var]
    mejor_val = 0
    for i in range(1, tam_var + 1):
        val = lista_p[i] + cortar_varilla2(tam_var - i, lista_p, memory)
        if val > mejor_val:
            mejor_val = val
    memory[tam_var] = mejor_val
    return mejor_val

# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    for e1 in lista_1:
        for e2 in lista_2:
            if e1 == e2:
                return True


# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
    a = set(lista_1) & set(lista_2)
    return len(a) > 0

assert superposicion_loop([1,2,3,4],[9,0,3,7]) == True
assert superposicion_set([1,2,13,4],[9,0,3,7]) == False
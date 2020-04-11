# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(a, b, c):
    if a>b:
        if a>c:
            return(a)
        else:
            return(c)
    elif b>c:
        return(b)
    else:
        return(c)

# si no falla es porque esta bien
assert mayor(1,10,5) == 10
assert mayor(4,9,18) == 18

# Si se piensa en la escalabilidad, como se pidió en el Pull Request:

vacio = "El arreglo está vacío."

def mayorLista(lista):
    return (
        max(lista, default = vacio)
    )

numeros = [12, 27, 32, 15, 2, 34, 7, 16, 8]

assert mayorLista(numeros) == 34
# Crea una funcion que devuelva 3 integers como parametros
# Si la suma de  los 3 numeros es  mayor a 15, va a devolver  el mayor numero
# Si la suma  de los 3 numeros  es menor a 10. Va a devolver  el numero menor
# Si la suma de los 3 numeros es un valor entre 10 y 15 va a devolver  el numero de valor intermedio
def devolver_distintos(num1: int, num2: int, num3: int) -> int:
    numeros = [num1, num2, num3]
    suma_numeros = sum(numeros)

    if suma_numeros > 15:
        return max(numeros)
    elif suma_numeros < 10:
        return min(numeros)
    else:  # entre 10 y 15 inclusive
        numeros.sort()
        return numeros[1]  # valor intermedio

# Ejemplo de uso
resultado = devolver_distintos(7, 10, 6)
print(f"Resultado: {resultado}")



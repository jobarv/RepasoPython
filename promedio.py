def reducir_lista():
    lista_numeros = [1, 2, 3, 4, 5, 343, 500, 12, 1, 3, 4, 5]
    mayor = max(lista_numeros)

    nueva_lista = []
    for num in lista_numeros:
        if num not in nueva_lista:
            nueva_lista.append(num)

    for num2 in lista_numeros:
        if num2 == mayor:
            nueva_lista.remove(num2)

    return nueva_lista


# Una funcion que pueda recibir como argumento la lista devuelta por la funcion anterior y calcule el promedio de valores de la misma, debe devolver el resultadi sin imprimirlo

def promedio():
    return sum(nueva_lista) / len(nueva_lista)


nueva_lista = reducir_lista()

resultado = promedio()
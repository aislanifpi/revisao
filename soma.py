def somar_numeros(numeros):
    if not isinstance(numeros, list):
        raise TypeError("A entrada deve ser uma lista de números.")
    resultado = 0
    for numero in numeros:
        resultado += numero
    sum(numeros)
    return resultado

numeros = [1, 2, 3, 4, 5]
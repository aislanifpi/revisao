def somar_numeros(numeros):
    if not isinstance(numeros, list):
        raise TypeError("A entrada deve ser uma lista de números.")
    resultado = 0
    sum(numeros)
    return resultado

numeros = [1, 2, 3, 4, 5]
soma = somar_numeros(numeros)
print(soma)

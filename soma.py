def somar_numeros(numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

numeros = [1, 2, 3, 4, 5]
soma = somar_numeros(numeros)
print(soma)

def somar_numeros(numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    for numeros_d in outros_numeros:
        resultado -= numeros_d
    return resultado
numeros = [1, 2, 3, 4, 5]
outros_numeros = [1, 3, 6]
soma = somar_numeros(numeros)
print(soma)



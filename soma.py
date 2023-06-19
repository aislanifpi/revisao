def somar_numeros(numeros):
    resultado = 0
    for numero in numeros:
        if type(numero) == int or type(numero) == float:
            resultado += numero
        else:
            print("Não é um número")
            return False
    return resultado

numeros = [1, 2, 3, 4, 5]
soma = somar_numeros(numeros)
print(soma)

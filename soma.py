def somar_numeros(numeros = [int or float]):
    if(type(numeros) != list):
        raise TypeError('O argumento deve ser uma lista')
    
    resultado = 0
    for numero in numeros:
        if type(numero) != int and type(numero) != float:
            raise TypeError('O argumento deve ser uma lista de números')
        else:
            resultado += numero

    return resultado

numeros = [1, 2, 3, 4, 5]
soma = somar_numeros(numeros)

print(soma)
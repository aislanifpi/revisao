def somar_numeros(numeros):
    resultado = sum (numeros)
    return resultado

def multiplicar_numeros(numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

numeros = [1, 2, 3, 4, 5]
soma = somar_numeros(numeros)
print("Soma:", soma)

produto = multiplicar_numeros(numeros)
print("Produto:", produto)

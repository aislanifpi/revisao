def somar_numeros(numeros):
    if not numeros:
        raise ValueError("A lsita de números não pode estar vazia")
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

numeros = [0]
try:
    soma = somar_numeros(numeros)
except ValueError as e:
    print("Erro:", str(e))
else:
    print(soma)

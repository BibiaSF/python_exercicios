# Criando a lista "numeros" com os números de 1 a 10
numeros = list(range(1, 11))

# Criando a lista "dobro" com o dobro de cada número da lista "numeros"
dobro = [x * 2 for x in numeros]

# Imprimindo as duas listas
print("Lista 'numeros':", numeros)
print("Lista 'dobro':", dobro)
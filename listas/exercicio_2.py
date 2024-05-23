# Criando uma lista vazia chamada "números"
numeros = []

# Pedindo ao usuário para digitar 5 números inteiros e adicionando-os à lista
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

# Imprimindo a lista de números
print("Lista de números:", numeros)

# Calculando a soma de todos os números da lista
soma = sum(numeros)

# Encontrando o maior número da lista
maior_numero = max(numeros)

# Encontrando o menor número da lista
menor_numero = min(numeros)

# Calculando a média dos números da lista
media = soma / len(numeros)

# Imprimindo os resultados
print("Soma dos números:", soma)
print("Maior número:", maior_numero)
print("Menor número:", menor_numero)
print("Média dos números:", media)
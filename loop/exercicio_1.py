# Solicita ao usuário que informe um número inteiro positivo N
n = int(input("Informe um número inteiro positivo N: "))

# Verifica se o número informado é positivo
while n <= 0:
    n = int(input("Por favor, informe um número inteiro positivo N: "))

# Inicializa a variável soma
soma = 0

# Solicita ao usuário que digite N números e os soma
for i in range(n):
    numero = float(input("Digite um número: "))
    soma += numero

# Calcula a média aritmética dos N números digitados
media = soma / n

# Imprime a média
print("A média dos números digitados é:", media)
# Inicializa a contagem de números pares
contagem_pares = 0

# Solicita que o usuário insira 5 números
print("Digite 5 números inteiros positivos:")
for i in range(5):
    numero = int(input())
    if numero % 2 == 0:
        contagem_pares += 1

# Exibe o resultado
print("A quantidade de números pares é:", contagem_pares)
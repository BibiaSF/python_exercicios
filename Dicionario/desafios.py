# Inicializando um dicionário vazio
produtos = {}

# Solicitando ao usuário que informe 4 pares de chave-valor
for i in range(4):
    chave = input(f"Digite o nome do produto {i+1}: ")
    while True:
        try:
            valor = float(input(f"Digite o preço do produto '{chave}': "))
            break
        except ValueError:
            print("Preço inválido. Por favor, digite um número válido.")
    produtos[chave] = valor

# Calculando a soma total dos preços
total = sum(produtos.values())

# Exibindo o dicionário final e a soma total dos preços
print("O dicionário criado é:")
for chave, valor in produtos.items():
    print(f"{chave}: R$ {valor:.2f}")

print(f"O total dos preços dos produtos é: R$ {total:.2f}")
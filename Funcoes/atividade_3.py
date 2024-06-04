# Função para calcular a média aritmética de 4 notas
def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

# Função para verificar se o aluno foi aprovado ou reprovado
def verificar_aprovacao(media):
    if media >= 5:
        return f"Aprovado com média {media:.2f}"
    else:
        return f"Reprovado com média {media:.2f}"

# Solicitando o nome do aluno e suas notas
nome_aluno = input("Digite o nome do aluno: ")
notas = []
for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

# Calculando a média
media = calcular_media(notas)

# Verificando se o aluno foi aprovado ou reprovado
resultado = verificar_aprovacao(media)

# Apresentando o resultado
print(f"O aluno {nome_aluno} está {resultado}")
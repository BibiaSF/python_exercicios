# Função para calcular a média aritmética de 4 notas
def calcular_media(nota1, nota2, nota3, nota4):
    soma = nota1 + nota2 + nota3 + nota4
    media = soma / 4
    return media

# Função para verificar se o aluno foi aprovado ou reprovado
def verificar_aprovacao(media):
    if media >= 5:
        return f"Aprovado com média {media:.2f}"
    else:
        return f"Reprovado com média {media:.2f}"

# Solicitando as notas do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calculando a média
media = calcular_media(nota1, nota2, nota3, nota4)

# Verificando se o aluno foi aprovado ou reprovado
resultado = verificar_aprovacao(media)

# Apresentando o resultado
print(resultado)
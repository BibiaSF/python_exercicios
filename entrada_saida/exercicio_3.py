def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Solicita a entrada do usuário para a base e altura do triângulo
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

# Chama a função para calcular a área e exibe o resultado
area_do_triangulo = calcular_area_triangulo(base, altura)
print("A área do triângulo é:", area_do_triangulo)
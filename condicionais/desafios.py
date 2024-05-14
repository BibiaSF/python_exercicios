# Função para calcular a tensão
def calcular_tensao(resistencia, corrente):
    return resistencia * corrente

# Função para calcular a resistência
def calcular_resistencia(tensao, corrente):
    return tensao / corrente

# Função para calcular a corrente
def calcular_corrente(tensao, resistencia):
    return tensao / resistencia

# Função para mostrar o menu
def menu():
    print("calculadora de Grandezas Elétricas")
    print("1. Tensão (em Volts)")
    print("2. Resistência (em Ohms)")
    print("3. Corrente (em Ampères)")

# Função principal do programa
def main():
    menu()  # Chama a função para mostrar o menu
    escolha = int(input("qual a grandeza deseja calcular? (1/2/3): "))  # Solicita a escolha do usuário

    if escolha == 1:
        resistencia = float(input("digite o valor da resistência (em Ohms): "))
        corrente = float(input("digite o valor da corrente (em Ampères): "))
        resultado = calcular_tensao(resistencia, corrente)
        print("a tensão é:", resultado, "Volts")

    elif escolha == 2:
        tensao = float(input("digite o valor da tensão (em Volts): "))
        corrente = float(input("digite o valor da corrente (em Ampères): "))
        resultado = calcular_resistencia(tensao, corrente)
        print("a resistência é:", resultado, "Ohms")

    elif escolha == 3:
        tensao = float(input("digite o valor da tensão (em volts): "))
        resistencia = float(input("digite o valor da resistência (em ohms): "))
        resultado = calcular_corrente(tensao, resistencia)
        print("a corrente é:", resultado, "ampères")

    else:
        print("escolha inválida. por favor, escolha 1, 2 ou 3.")

# Chama a função principal do programa se este arquivo for executado diretamente
if __name__ == "__main__":
    main()

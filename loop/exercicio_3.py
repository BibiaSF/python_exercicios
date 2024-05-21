# Definição da senha correta e tentativas restantes
senha_correta = "123456"
tentativas_restantes = 3

# Solicita o nome do correntista
nome = input("Digite seu nome: ")

# Loop para tentativas de senha
while tentativas_restantes > 0:
    # Solicita a senha do usuário
    senha_digitada = input("Digite sua senha: ")
    
    # Verifica se a senha está correta
    if senha_digitada == senha_correta:
        print(f"Olá, {nome}, seja bem-vindo ao nosso banco.")
        break
    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Você ainda tem {tentativas_restantes} {'tentativa' if tentativas_restantes == 1 else 'tentativas'}.")
        else:
            print(f"Senha incorreta. {nome}, sua conta foi bloqueada. Por favor, dirija-se aos nossos caixas.")
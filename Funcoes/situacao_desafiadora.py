def menu():
    print("\nMenu:")
    print("1. Cadastrar notas de um aluno")
    print("2. Mostrar notas cadastradas")
    print("3. Sair")

def cadastrar_notas(alunos):
    nome = input("Digite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1} do aluno {nome}: "))
        notas.append(nota)
    alunos[nome] = notas

def mostrar_notas(alunos):
    if not alunos:
        print("Nenhuma nota cadastrada.")
    else:
        for nome, notas in alunos.items():
            print(f"\nAluno: {nome}")
            for i, nota in enumerate(notas, 1):
                print(f"Nota {i}: {nota}")
            media = sum(notas) / len(notas)
            situacao = "Aprovado" if media >= 6 else "Reprovado"
            print(f"Média: {media:.2f} - Situação: {situacao}")

def main():
    alunos = {}
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_notas(alunos)
        elif opcao == '2':
            mostrar_notas(alunos)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
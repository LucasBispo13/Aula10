def meunu_opcoes(): 
    print("===Sistema Escolar===")
    print("1- Cadastrar Aluno\n2- Listar alunos \n3- Quantidade de Cadastrados \n4- Sair")

def cadastro_aluno():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1+nota2)/2

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
        
    alunos.append(f"{nome} - {situacao}")

    print("Aluno cadastrados com sucesso")

def listar_alunos():
    if len(aluno) > 0:
        for aluno in alunos:
         print(aluno)
    else:
        print("A lista está vazia")

def quantidade():
    quantia = len(alunos)
    print(f"A quantidade de cadastrados é {quantia}")

alunos = []

while True:
    meunu_opcoes()

    opcao = input("Escolher uma opção: ")

    match opcao:
        case "1":cadastro_aluno()
            
        case "2":listar_alunos()

        case "3":quantidade()
            
    
        case "4":
            print("Encerrando ")
            break
        case _:
            print("Opção inválida!")





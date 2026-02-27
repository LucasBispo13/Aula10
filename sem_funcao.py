#montar um sistema de cadastro de alunos e notas

'''
Menu de opções:

1- Cadastrar Alunos
2- Listar alunos 
3- Sair



'''

#lista de alunos 

alunos = []

while True:
    #Meu de opções:
    print("===Sistema Escolar===")
    print("1- Cadastrar Aluno\n2- Listar alunos \n3- Sair")

    opcao = input("Escolher uma opção: ")

    match opcao:
        case "1":
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
        case "2":
            for aluno in alunos:
                print(aluno)     
        case "3":
            print("Encerrando ")
            break
        case _:
            print("Opção inválida!")





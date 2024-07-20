import json


def mostrar_menu_principal():
    print("MENU PRINCIPAL")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")


def mostrar_menu_secundario(opcao):
    print(f"MENU - {opcao}")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("0. Voltar ao menu principal")


def incluir(arquivo, opcao1):
    try:
        if opcao1 == 1 or opcao1 == 3: # estudantes ou professores
            cadastro = {
                "Código": int(input("Código: ")),
                "Nome": input("Nome completo: "),
                "CPF": input("CPF: ")
            }
        elif opcao1 == 2: # disciplinas
            cadastro = {
                "Código": int(input("Código: ")),
                "Nome": input("Nome da disciplina: ")
            }
        elif opcao1 == 4: # turmas
            cadastro = {
                "Código": int(input("Código da turma: ")),
                "Código Professor": int(input("Código do professor(a): ")),
                "Código Disciplina": int(input("Código da disciplina: "))
            }
        elif opcao1 == 5: # matrículas
            cadastro = {
                "Código": int(input("Código da matrícula: ")),
                "Código Turma": int(input("Código da turma: ")),
                "Código Estudante": int(input("Código do estudante: "))
            }
        lista = ler_arquivo(arquivo)
        lista.append(cadastro)
        escrever_arquivo(lista, arquivo)
        print("Cadastro realizado com sucesso!")
        return
    except ValueError:
        print("Digite apenas números. Tente novamente.")
        return


def listar(arquivo, opcao1):
    lista = ler_arquivo(arquivo)
    for cadastro in lista:
        if opcao1 == 1 or opcao1 == 3: # estudantes ou professores
            print(f"#{cadastro["Código"]} {cadastro["Nome"]}  CPF:{cadastro["CPF"]}")
        elif opcao1 == 2: # disciplinas
            print(f"#{cadastro["Código"]} {cadastro["Nome"]}")
        elif opcao1 == 4: # turmas
            print(f"#{cadastro["Código"]} Professor:#{cadastro["Código Professor"]} Disciplina:#{cadastro["Código Disciplina"]}")
        elif opcao1 == 5: # matrículas
            print(f"#{cadastro["Código"]} Estudante:#{cadastro["Código Estudante"]} Turma:#{cadastro["Código Turma"]}")
    if not lista:
        print("Não há cadastros.")


def atualizar(arquivo, opcao1):
    lista = ler_arquivo(arquivo)
    try:
        codigo_antigo = int(input("Digite o código do cadastro que deseja atualizar: "))
        for cadastro in lista:
            if codigo_antigo == cadastro["Código"]:
                if opcao1 == 1 or opcao1 == 3: # estudantes ou professores
                    cadastro["Código"] = int(input("Atualizar Código: "))
                    cadastro["Nome"] = input("Atualizar Nome completo: ")
                    cadastro["CPF"] = input("Atualizar CPF: ")
                elif opcao1 == 2: # disciplinas
                    cadastro["Código"] = int(input("Atualizar Código: ")),
                    cadastro["Nome"] = input("Atualizar Nome da disciplina: ")
                elif opcao1 == 4: # turmas
                    cadastro["Código"] = int(input("Atualizar Código da turma: ")),
                    cadastro["Código Professor"] = int(input("Atualizar Código do professor(a): ")),
                    cadastro["Código Disciplina"] = int(input("Atualizar Código da disciplina: "))
                elif opcao1 == 5:  # matrículas
                    cadastro["Código"] = int(input("Atualizar Código da matrícula: ")),
                    cadastro["Código Estudante"] = int(input("Atualizar Código do estudante: ")),
                    cadastro["Código Turma"] = int(input("Atualizar Código da turma: "))
                print("Atualizado com sucesso!")
                escrever_arquivo(lista, arquivo)
                return
        print("Esse código não existe.")
    except ValueError:
        print("Digite apenas números. Tente novamente.")


def excluir(arquivo):
    lista = ler_arquivo(arquivo)
    try:
        codigo = int(input("Digite o código do cadastro que deseja excluir: "))
        for cadastro in lista:
            if codigo == cadastro["Código"]:
                if input("Tem certeza que deseja remover (s/n)? ") == "s":
                    print("Removido com sucesso!")
                    lista.remove(cadastro)
                    escrever_arquivo(lista, arquivo)
                    return
        print("Esse código não existe")
    except ValueError:
        print("Digite apenas números. Tente novamente.")


def escrever_arquivo(lista, arquivo):
    with open(arquivo, "w", encoding='utf-8') as arquivo_aberto:
        json.dump(lista, arquivo_aberto, ensure_ascii=False)


def ler_arquivo(arquivo):
    try:
        with open(arquivo, "r", encoding='utf-8') as arquivo_aberto:
            lista = json.load(arquivo_aberto)
        return lista
    except FileNotFoundError:
        return[]


arquivo_estudantes = "estudantes.json"
arquivo_disciplinas = "disciplinas.json"
arquivo_professores = "professores.json"
arquivo_turmas = "turmas.json"
arquivo_matrículas = "matriculas.json"

# Apresentando o Menu Principal
while True:
    mostrar_menu_principal()
    # Coletando a informação escolhida pelo usuário
    opcao1 = input("Digite uma opção: ")
    if opcao1 == "1" or opcao1 == "2" or opcao1 == "3" or opcao1 == "4" or opcao1 == "5":
        print(f"Você digitou a opção {opcao1}.")
        # Apresentando o Menu Secundário
        while True:
            mostrar_menu_secundario(opcao1)
            # Coletando a segunda informação escolhida pelo usuário
            opcao2 = input("Digite uma opção: ")
            if opcao2 == "1" or opcao2 == "2" or opcao2 == "3" or opcao2 == "4":
                print(f"Você digitou a opção {opcao2}.")
                # Se o usuário quiser incluir estudantes
                if opcao1 == "1" and opcao2 == "1":
                    print("INCLUIR ESTUDANTES")
                    incluir(arquivo_estudantes, 1)
                # Se o usuário quiser listar estudantes
                elif opcao1 == "1" and opcao2 == "2":
                    print("LISTA DE ESTUDANTES")
                    listar(arquivo_estudantes, 1)
                # Se o usuário quiser editar estudantes
                elif opcao1 == "1" and opcao2 == "3":
                    print("ATUALIZAR ESTUDANTES")
                    atualizar(arquivo_estudantes, 1)
                # Se o usuário quiser excluir estudantes
                elif opcao1 == "1" and opcao2 == "4":
                    print("EXCLUIR ESTUDANTES")
                    excluir(arquivo_estudantes)
                # Se o usuário quiser incluir diciplinas
                elif opcao1 == "2" and opcao2 == "1":
                    print("INCLUIR DISCIPLINAS")
                    incluir(arquivo_disciplinas, 2)
                # Se o usuário quiser listar disciplinas
                elif opcao1 == "2" and opcao2 == "2":
                    print("LISTA DE DISCIPLINAS")
                    listar(arquivo_disciplinas, 2)
                # Se o usuário quiser editar disciplinas
                elif opcao1 == "2" and opcao2 == "3":
                    print("ATUALIZAR DISCIPLINAS")
                    atualizar(arquivo_disciplinas, 2)
                # Se o usuário quiser excluir disciplinas
                elif opcao1 == "2" and opcao2 == "4":
                    print("EXCLUIR DISCIPLINAS")
                    excluir(arquivo_disciplinas)
                # Se o usuário quiser incluir professores
                elif opcao1 == "3" and opcao2 == "1":
                    print("INCLUIR PROFESSORES")
                    incluir(arquivo_professores, 3)
                # Se o usuário quiser listar professores
                elif opcao1 == "3" and opcao2 == "2":
                    print("LISTA DE PROFESSORES")
                    listar(arquivo_professores, 3)
                # Se o usuário quiser editar professores
                elif opcao1 == "3" and opcao2 == "3":
                    print("ATUALIZAR PROFESSORES")
                    atualizar(arquivo_professores, 3)
                # Se o usuário quiser excluir professores
                elif opcao1 == "3" and opcao2 == "4":
                    print("EXCLUIR PROFESSORES")
                    excluir(arquivo_professores)
                # Se o usuário quiser incluir turmas
                elif opcao1 == "4" and opcao2 == "1":
                    print("INCLUIR TURMAS")
                    incluir(arquivo_turmas, 4)
                # Se o usuário quiser listar turmas
                elif opcao1 == "4" and opcao2 == "2":
                    print("LISTA DE TURMAS")
                    listar(arquivo_turmas, 4)
                # Se o usuário quiser editar um turmas
                elif opcao1 == "4" and opcao2 == "3":
                    print("ATUALIZAR TURMAS")
                    atualizar(arquivo_turmas, 4)
                # Se o usuário quiser excluir um turmas
                elif opcao1 == "4" and opcao2 == "4":
                    print("EXCLUIR TURMAS")
                    excluir(arquivo_turmas)
                # Se o usuário quiser incluir matrículas
                elif opcao1 == "5" and opcao2 == "1":
                    print("INCLUIR MATRÍCULAS")
                    incluir(arquivo_matrículas, 5)
                # Se o usuário quiser listar matrículas
                elif opcao1 == "5" and opcao2 == "2":
                    print("LISTA DE MATRÍCULAS")
                    listar(arquivo_matrículas, 5)
                # Se o usuário quiser editar matrículas
                elif opcao1 == "5" and opcao2 == "3":
                    print("ATUALIZAR MATRÍCULAS")
                    atualizar(arquivo_matrículas, 5)
                # Se o usuário quiser excluir matrículas
                elif opcao1 == "5" and opcao2 == "4":
                    print("EXCLUIR MATRÍCULAS")
                    excluir(arquivo_matrículas)
            elif opcao2 == "0":
                print("Voltando ao menu principal...")
                break
            else:
                print("Você digitou uma opção inválida.")
    elif opcao1 == "0":
        print("Saindo...")
        break
    else:
        print("Você digitou uma opção inválida.")
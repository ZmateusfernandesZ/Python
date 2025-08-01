def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {
        "tarefa": nome_tarefa,
        "Completada": False
        }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")
    return

def listar_tarefas(tarefas):
    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["Completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")

def atualizar_tarefa(tarefas, indice, novo_nome_tarefa):
    if indice < 0 or indice >= len(tarefas):
        print("Índice inválido. Tarefa não encontrada.")
        return
    tarefas[indice]["tarefa"] = novo_nome_tarefa
    print(f"Tarefa {indice} atualizada para '{novo_nome_tarefa}'")
    return

def completar_tarefa(tarefas, indice):
    if indice < 0 or indice >= len(tarefas):
        print("Índice inválido. Tarefa não encontrada.")
        return
    tarefas[indice]["Completada"] = True
    print(f"Tarefa {indice} marcada como completada.")
    return

def deletar_tarefa(tarefas, indice):
    if indice < 0 or indice >= len(tarefas):
        print("Índice inválido. Tarefa não encontrada.")
        return
    tarefa_removida = tarefas.pop(indice)
    print(f"Tarefa '{tarefa_removida['tarefa']}' deletada com sucesso!")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["Completada"]:
            tarefas.remove(tarefa)
            print(f"Tarefa '{tarefa['tarefa']}' deletada por estar completada.")
            return
 

        

tarefas = []

while True:
    print("\nGerenciador de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")  
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefa")
    print("6. Deletar tarefas completadas")
    print("7. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        listar_tarefas(tarefas)

    elif escolha == "3":
        listar_tarefas(tarefas)
        indice = int(input("Digite o número da tarefa a ser atualizada: ")) - 1
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, indice, novo_nome_tarefa)

    elif escolha == "4":
        listar_tarefas(tarefas)
        indice = int(input("Digite o número da tarefa a ser completada: ")) - 1
        completar_tarefa(tarefas, indice)

    elif escolha == "5":
        listar_tarefas(tarefas)
        indice = int(input("Digite o número da tarefa a ser deletada: ")) - 1
        deletar_tarefa(tarefas, indice)

    elif escolha == "6":
        deletar_tarefas_completadas(tarefas)

    elif escolha == "7": 
        break

print("Programa finalizado.")
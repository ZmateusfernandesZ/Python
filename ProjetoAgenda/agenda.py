# Sistema de agenda de contatos

def adicionar_contato(agenda, nome_contato, telefone_contato, email_contato):
    agenda.append({
        "nome": nome_contato,
        "telefone": telefone_contato,
        "email": email_contato,
        "favorito": False
    })
    print(f"\nContato {nome_contato} adicionado com sucesso!")
    return

def listar_contatos(agenda):
    print("\nLista de Contatos:")
    for indice, contato in enumerate(agenda, start=1):
        favorito = "❤" if contato['favorito'] else "Não"
        print(f"{indice}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Favorito: {favorito}")

def editar_contato(indice,agenda, novo_nome, novo_telefone, novo_email):
    for indice, contato in enumerate(agenda):
        if indice == indice:
            agenda[indice] = {
                "nome": novo_nome,
                "telefone": novo_telefone,
                "email": novo_email,
                "favorito": contato['favorito']
            }
            print(f"\nContato {novo_nome} editado com sucesso!")
            return
def favoritar_contato(indice, agenda):
    if 0 <= indice < len(agenda):
        agenda[indice]['favorito'] = True
        print(f"\nContato {agenda[indice]['nome']} favoritado com sucesso!")
    else:
        print("\nÍndice inválido!")
        

def remover_contato(indice, agenda):
    if 0 <= indice < len(agenda):
        del agenda[indice]
        print("\nContato removido com sucesso!")
    else:
        print("\nÍndice inválido!")
    


agenda = []


while True:

    print("\nBem-vindo ao sistema de agenda de contatos!")
    print("Selecione uma opção:")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Favoritar contato")
    print("5. Remover contato")
    print("6. Sair")

    opcao = int(input("\nDigite o número da opção desejada: "))

    if opcao == 1:
        nome_contato = input("Digite o nome do contato: ")
        telefone_contato = input("Digite o telefone do contato: ")
        email_contato = input("Digite o email do contato: ")  
        adicionar_contato(agenda, nome_contato, telefone_contato, email_contato)

    elif opcao == 2:
        listar_contatos(agenda)

    elif opcao == 3:
        indice = int(input("Digite o índice do contato a ser editado: ")) - 1
        if 0 <= indice < len(agenda):
            novo_nome = input("Digite o novo nome do contato: ")
            novo_telefone = input("Digite o novo telefone do contato: ")
            novo_email = input("Digite o novo email do contato: ")
            editar_contato(indice, agenda, novo_nome, novo_telefone, novo_email)
        listar_contatos(agenda)

    elif opcao == 4:
        indice = int(input("Digite o índice do contato a ser favoritado: ")) - 1
        favoritar_contato(indice, agenda)
        listar_contatos(agenda)

    elif opcao == 5:
        indice = int(input("Digite o índice do contato a ser removido: ")) - 1
        if 0 <= indice < len(agenda):
            del agenda[indice]
            print("\nContato removido com sucesso!")
        else:
            print("\nÍndice inválido!")
        listar_contatos(agenda)

    elif opcao == 6:
        break
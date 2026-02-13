usuarios = []
def adicionar_usuario():
    nome = input("Nome do usuário: ")
    idade = input("idade: ")
    usuarios.append({"nome": nome, "idade": idade})
    print("Usuário cadastrado com sucesso!\n")

    def listar_usuarios():
        if not usuarios:
            print("Nenhum usuário cadastrado.\n")
            return
        for i, usuario in enumerate(usuarios, start=1):
            print( f"{i} - nome: {usuario['nome']} - idade: {usuario['idade']}")
            print()
            def menu():
                while True:
                    print("1 - Adicionar usuário")
                    print("2 - Listar usuários")
                    print("3 - Sair")
                    opcao = input("Escolha uma opção: ")
                    if opcao == "1":
                        adicionar_usuario()
                    elif opcao == "2":
                        listar_usuarios()
                    elif opcao == "3":
                        print("Saindo...")
                        break
                    else:
                        print("Opção invalida!\n")
        if __name__ == "__main__":
            menu()
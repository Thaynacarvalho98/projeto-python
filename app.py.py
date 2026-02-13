def saudacao(nome):
    return f"Olá, {nome}!\nBem-vindo ao meu projeto em python."
def menu():
    nome = input("Digite seu nome: ")
    print(saudacao(nome))
    if __name__ == "__main__":
        menu()
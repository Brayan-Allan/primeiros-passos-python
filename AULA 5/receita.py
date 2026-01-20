import os

ingredientes = []

def titulo():
    print("""
░█▀▀█ ░█▀▀▀ ░█▀▀█ ░█▀▀▀ ▀█▀ ▀▀█▀▀ ─█▀▀█ 　 ░█▀▀▄ ░█▀▀▀ 　 ░█▀▀█ ░█▀▀▀█ ░█─── ░█▀▀▀█ 
░█▄▄▀ ░█▀▀▀ ░█─── ░█▀▀▀ ░█─ ─░█── ░█▄▄█ 　 ░█─░█ ░█▀▀▀ 　 ░█▀▀▄ ░█──░█ ░█─── ░█──░█ 
░█─░█ ░█▄▄▄ ░█▄▄█ ░█▄▄▄ ▄█▄ ─░█── ░█─░█ 　 ░█▄▄▀ ░█▄▄▄ 　 ░█▄▄█ ░█▄▄▄█ ░█▄▄█ ░█▄▄▄█""")
    print("\n")

def exibir_menu():
    print("--------------------")
    print("1 - Adicionar ingredientes")
    print("2 - Exibir ingredientes")
    print("3 - sair")
    print("--------------------")
    print("\n")

def adicionar_ingredientes():
    os.system("cls")
    while True:
        os.system("cls")
        ingrediente = input("Digite o ingrediente desejado: ")
        ingredientes.append(ingrediente)
        print("--------------------")
        print("Ingrediente adicionado com sucesso!")
        print("\n")

        while True:
            resposta = input("Incluir outro ingrediente? (s/n?)")
            if resposta.lower() == "n" or resposta.lower() == "s":
                break
            else:
                print("Resposta inválida!")
        if resposta.lower() == "n":
            break
    menu_principal()

def final():
    os.system("cls")
    print("--------------------")
    print("ATÉ A PRÓXIMA")
    print("--------------------")
    print("\n")

def menu_principal():
    input("Aperte ENTER para voltar ao menu principal")
    main()

def exibir_ingredientes():
    if len(ingredientes) == 0:
        print("--------------------")
        print("Nenhum ingrediente cadastrado!")
        print("--------------------")
    else:
        print("--------------------")
        print("INGREDIENTES:")
        print("--------------------")
        for ingrediente in ingredientes:
            print(ingrediente)
            print("--------------------")
    menu_principal()

def opcao_invalida():
    print("--------------------")
    print("OPÇÃO INVÁLIDA")
    print("--------------------")
    (input("Aperte ENTER para voltar ao menu principal"))
    main()

def escolha_menu():
    escolha = int(input("O que deseja fazer hoje?"))
    match escolha:
        case 1:
            adicionar_ingredientes()
        case 2:
            exibir_ingredientes()
        case 3:
            final()
        case _:
            opcao_invalida()

def main():
    os.system("cls") # Função para limpar a tela a cada vez que é executado
    titulo()
    exibir_menu()
    escolha_menu()

if __name__ == "__main__":
    main()
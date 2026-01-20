import os

pizzas = [
    {"nome_pizza":"Portuguesa","ingredientes":"queijo, massa de tomate, cebola","vendida":False},
    {"nome_pizza":"Margherita","ingredientes":"queijo, massa de tomate, rucula","vendida":False},
    {"nome_pizza":"Peperoni","ingredientes":"queijo, massa de tomate, peperoni","vendida":False},
    {"nome_pizza":"Calabresa","ingredientes":"queijo, massa de tomate, calabresa","vendida":False}
]

def titulo(): # FUNÇÃO CHAMADA TÍTULO
    print("""
█▀█ █ ▀█ ▀█ ▄▀█ █▀█ █ ▄▀█   █▀▄▀█ ▄▀█ █▀█ █▀█ █░█ █▀▀ █▀ 
█▀▀ █ █▄ █▄ █▀█ █▀▄ █ █▀█   █░▀░█ █▀█ █▀▄ ▀▀█ █▄█ ██▄ ▄█ """)


def voltar_menu_principal():# FUNÇÃO VOLTA MENU
    input("\n Aperte ENTER para voltar ao menu principal")
    menu()


def menu(): # FUNÇÃO CHAMADA MENU
    print("\n")
    print("--------------------")
    print("1 - Cadastrar pizza")
    print("2 - Listar pizzas")
    print("3 - Alterar estados da pizza")
    print("4 - Saír")
    print("--------------------")


def subtitulo(sub): # CRIAR SUB-TITULOS
    os.system("cls")
    print("--------------------")
    print(sub.center(20))
    print("--------------------")
    print("\n")


def cadastrar_pizza(): # FUNÇÃO CADASTRO DE PIZZA

    while True:
        subtitulo("CADASTRO DE PIZZAS:")
        nome_pizza = input("Digite o nome da nova pizza: ")
        ingredientes = input("Quais os ingredientes desejados?: ")

        dic_pizza = { # Dicionario recebedor de dados da pizza
            "nome_pizza": nome_pizza,
            "ingredientes": ingredientes,
            "vendida": False
        }

        pizzas.append(dic_pizza)
        print("Pizza cadastrada com sucesso!")

        while True:
            resposta = input("Incluir outra pizza? (s/n) ")
            if resposta.lower() == "s":
                os.system("cls")
                break
            elif resposta.lower() == "n":
                return
            else:
                print("Resposta inválida! Digite novamente...")

def listar_pizza(): # FUNÇÃO LISTAR PIZZAS
    subtitulo("PIZZAS CADASTRADAS:")
    nome = "Nome da pizza"
    ingredientes = "Ingredientes"

    disp_venda = True # VERIFICA SE TEVE VENDA

    for pizza in pizzas:
        if pizza["vendida"] == False:
    
            if not disp_venda:
                print(f"|  {"NOME PIZZA".center(20)}  |  {"INGREDIENTES:".center(40)}  |")
                print(f"-"*71)

                disp_venda = False
        
            print(f"|  {pizza ["nome_pizza"].center(20)}  |  {pizza ["ingredientes"].center(40)}  |")    

    if not disp_venda:
        print("NENHUMA PIZZA CADASTRADA")
    
    voltar_menu_principal() # RETORNO PARA MENU PRINCIPAL


def alterar_pizza(): #FUNÇÃO ALTERAR ALGUMA PIZZA
    subtitulo("ALTERAR STATUS DE PIZZA CADASTRADA")

    cont = 0
    for pizza in pizzas:
        print(f"| {pizza["nome_pizza"].center(20)} | {pizza["ingredientes"].center(40)} | {pizza["vendida"]} |")

    while True:
        print("\n")
        nome_pizza = input("Digite o nome da Pizza que deseja Alterar: ")
        for pizza in pizzas:
            if pizza["nome_pizza"].lower() == nome_pizza.lower():
                pizza["vendida"] = not pizza["vendida"]
                cont = 1
        if cont == 1:
            os.system("cls")
            print(f"Status da pizza de {nome_pizza} foi alterado com Sucesso!")
            break
        else:
            print("Não existe pizza com esse nome, tente novamente...")
       
    voltar_menu_principal() # RETORNO PARA MENU PRINCIPAL


def escolha_opcao(): # FUNÇÃO ESCOLHA DE OPÇÃO
    print("\n")
    while True:
        opcao = int(input("Escolha uma opção: "))
        if opcao > 0 and opcao < 5:
            break
        else:
            print("Opção inválida")
            print("--------------------")
    match opcao:
        case 1:
            cadastrar_pizza()
        case 2:
            listar_pizza()
        case 3:
            alterar_pizza()
        case 4:
            print("ATÉ A PRÓXIMA!")


def inicial(): # FUNÇÃO CHAMADA INICIAL
    while True:
        os.system("cls")
        titulo()
        menu()
        escolha_opcao()

# Ponto de entrada
if __name__ == "__main__":
    inicial()
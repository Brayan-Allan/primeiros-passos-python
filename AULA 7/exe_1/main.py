from contaBancaria2 import ContaBancaria

def titulo():   # NOME DO BNCO
    print("""
▒█▄░▒█ ▒█░▒█ 　 ▒█▀▀█ ░█▀▀█ ▒█▄░▒█ ▒█▀▀█ ▒█▀▀▀█ 
▒█▒█▒█ ▒█░▒█ 　 ▒█▀▀▄ ▒█▄▄█ ▒█▒█▒█ ▒█░░░ ▒█░░▒█ 
▒█░░▀█ ░▀▄▄▀ 　 ▒█▄▄█ ▒█░▒█ ▒█░░▀█ ▒█▄▄█ ▒█▄▄▄█""")

contas = {}

def menu():     # FUNÇÃO CHAMADA MENU
    print("\n")
    print("--------------------")
    print("1 - Cadastro títular")
    print("2 - Consulta de saldo")
    print("3 - Depósito em conta")
    print("4 - Saque")
    print("5 - Saír")
    print("--------------------")


def escolha_opcao():
    while True:  # loop principal do menu
        menu()  # mostra o menu
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números de 1 a 5.")
            continue

        if opcao not in range(1, 6):
            print("Opção inválida. Digite de 1 a 5.")
            continue

        match opcao:
            case 1:  # CADASTRO
                nome = input("Digite o nome do titular: ")
                if nome in contas:
                    print("Conta já existe! Voltando ao menu")
                    continue
                else:
                    contas[nome] = ContaBancaria(nome)
                    print(f"Conta de {nome} criada com sucesso!")

            case 2:  # CONSULTA SALDO
                nome = input("Digite o nome do titular: ")
                if nome in contas:
                    contas[nome].consultar_saldo()
                else:
                    print("Conta não encontrada.")

            case 3:  # DEPÓSITO
                nome = input("Digite o nome do titular: ")
                if nome in contas:
                    valor = float(input("Digite o valor do depósito: "))
                    contas[nome].depositar(valor)
                else:
                    print("Conta não encontrada.")

            case 4:  # SAQUE
                nome = input("Digite o nome do titular: ")
                if nome in contas:
                    valor = float(input("Digite o valor para saque: "))
                    contas[nome].saque(valor)
                else:
                    print("Conta não encontrada.")

            case 5:  # SAIR
                print("ATÉ A PRÓXIMA!")
                break

def main():
    titulo()
    menu ()
    escolha_opcao()

if __name__ == "__main__":
    main()
from contaBancaria import contaBancaria

def main():
    nome = input("Qual é o seu nome? ")
    usuario_1 = contaBancaria(nome)

    deposito = float(input("Qual valor deseja depositar? "))
    usuario_1.depositar(deposito)

    saque = float(input("Qual valor deseja sacar? "))
    usuario_1.saque(saque)

if __name__ == "__main__":
    main()
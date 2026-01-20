class contaBancaria:

    #construtor
    def __init__(self, nome):
        self.__nome = nome
        self.__saldo = 0
    
    def depositar(self, valor):
        while True:
            if valor > 0:
                self.__saldo += valor
                print(f"Prezado(a) {self.__nome}: Seu depósito de R$ {valor} foi efetuado com sucesso")
                break
            else:
                print(f"Sr. {self.__nome}, o depósito deve ser maior que R$ 0,00")
                valor = float(input("Revise o valor do despósito"))
        self.consultar_saldo()

    def consultar_saldo(self):
        print(f"{self.__nome}, seu saldo é de R$ {self.__saldo}")

    def saque(self, valor):
        while True:
            if valor <= self.__saldo and valor > 0:
                self.__saldo += valor
                print(f"Prezado(a) {self.__nome} seu saque de R$ {valor} foi efetuado com sucesso!")
            elif valor < 0:
                print("O valor o saque não pode ser negativo")
                valor = float(input("Revise o valor desejado"))
            else:
                print(f"{self.__nome} seu saldo é inferior ao valor solicitado")
                valor = float(input("Revise o valor desejado"))
        self.consultar_saldo()
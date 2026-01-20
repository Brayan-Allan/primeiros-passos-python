class ContaBancaria2:

    #CADSTRO CLENTE
    def __init__(self, titular_conta, saldo = 0):
        self.titular_conta = titular_conta
        self.saldo = saldo

    #CONSULTAR
    def consultar_saldo(self):
        print(f"{self.titular_conta}, seu saldo é de R$ {self.saldo}")

    # DEPOSITAR
    def depositar(self, valor):
        while True:
            if valor > 0:
                self.saldo += valor
                print(f"Prezado(a) {self.titular_conta}: Seu depósito de R$ {valor} foi efetuado com sucesso")
                break
            else:
                print(f"Sr. {self.titular_conta}, o depósito deve ser maior que R$ 0,00")
                valor = float(input("Revise o valor do despósito"))
        self.consultar_saldo()

    
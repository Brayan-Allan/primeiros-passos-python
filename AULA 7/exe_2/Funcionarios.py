class Funcionario:

    def __init__(self, n, c, s):
        self.__nome = n
        self.__cargo = c
        self.__salario = s
        
        def exibir_informacoes(self):
            print("--------------------")
            print(f"Funcionario: {self.__nome}")
            print(f"Cargo: {self.__cargo}")
            print(f"Salário: {self.__salario}")
            print("--------------------")

        def aplicar_aumento(self):
            while True:
                if porcentagem >= 0:
                    self.__salario *=(1+porcentagem/100)
                    print(f"{self.__nome}, seu novo salário é de R$ {self.__salario}")
                    break
                else:
                    print("O percentual de aumento não pode ser negativo")
                    porcentagem = float(input("Digite o percentual: "))
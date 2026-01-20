from Funcionarios import Funcionario

def principal():
    nome = input("Qual é seu nome? ")
    cargo = input("Qual é seu cargo? ")
    salario = float(input("Qual é o seu salário? "))

    func_1 = Funcionario(nome, cargo, salario)
    func_1.exibir_informacoes()
    func_1.aplicar_aumento(20)

if __name__ == "__main__":
    principal()
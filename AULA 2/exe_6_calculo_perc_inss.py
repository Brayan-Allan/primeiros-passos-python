# Pergunta o salário para o usuário
# até R$ 2.000,00 ele paga INSS de 12%
# acima de R$ 2.000,00 ele paga INSS de 15%
# Imprima o imposto a pagar

salario = float(input("Qual é o seu salário?"))

if salario <= 2000:
    inss = salario * 12/100
else:
    inss = salario * 15/100

print(f"O valor mensal do seu INSS é: R$ {inss:.2f}")
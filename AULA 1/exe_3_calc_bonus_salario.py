# Pergunte para o usuário:
# salário e percentual de bônus que deseja receber
# realize o cálculo do salário somado ao bônus
# imprima em tela o resultado do salário somado ao percentual de bônus

salario = int(input("Qual seu salário? "))
percBonus = int(input("Qual o percentual de aumento que você deseja: "))

valorFinal = salario + (salario * percBonus / 100)

print(f"O salário de: {salario} somado ao bônus de: {percBonus} é igual a: {valorFinal}")
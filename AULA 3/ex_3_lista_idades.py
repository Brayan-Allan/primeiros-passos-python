# Crie um programa que permita ao usuário inserir idades em uma lista.
# O programa deve continuar a solicitar idades até que o usuário insira um valor negativo,
# que será usado como sinal para encerrar a entrada de dados.
# Evite incluir na lista valores acima de 110
# Ao fim exiba o título "Lista:"
# E a baixo liste os conteúdos da lista separados por níveis de idades e no fim uma lista geral com todas as idades inseridas


lista_idades = []
crianca = []
adolescente = []
adulto = []
idoso = []

while True:
    # COLETA DE DADOS
        idade = int(input("Isira uma idade: "))
    # PARADA
        if idade < 0:
            break
    # INVÁLIDO
        elif idade > 110:
            print("O número inserido é inválido. Tente novamente")
            continue
    # SEPARAÇÃO IDADES
        elif idade <= 12:
            crianca.append(idade)
        elif idade <= 18:
            adolescente.append(idade)
        elif idade <= 40:
            adulto.append(idade)
        else:
            idoso.append(idade)
    # PREENCHIMENTO LISTA GERAL
            lista_idades.append(idade)
    # RETORNO
print("LISTA:")

if len(crianca) == 0:
    print("Na lista não existe crianças")
else:
    print(f"Crianças: {crianca}")

if len(adolescente) == 0:
    print("Na lista não existe adolescentes")
else:
    print(f"Adolescentes: {adolescente}")

if len(adulto) == 0:
    print("Na lista não existe adultos")
else:
    print(f"Adultos: {adulto}")

if len(idoso) == 0:
    print("Na lista não existe idosos")
else:
    print(f"Idosos: {idoso}")

if len(lista_idades) == 0:
    print("ATENÇÃO")
    print("A lista geral de idades ficou vazia")
else:
    print(f"A lista geral é: {lista_idades}")
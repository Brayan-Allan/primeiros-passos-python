

# Definindo uma função:
# def + nome_funcao + (variaveis)
# Dentro: programação da funcao

def soma (num_1, num_2):
    soma = num_1 + num_2
    print(f"A soma de {num_1} e {num_2} é {soma}")

# Chamando a função
# nome função + (valores para as variaveis)

soma(3, 4)
soma(999, 765)
soma (56, 78)

# Função com retorno:

def soma_com_retorno (num_1, num_2):
    soma = num_1 + num_2
    print(f"A soma de {num_1} e {num_2} é {soma}")
    return soma

# Função com default
# variaveis declaradas com valores

def soma (num_1 = 0, num_2 = 1):
    soma = num_1 + num_2
    print(f"A soma de {num_1} e {num_2} é {soma}")

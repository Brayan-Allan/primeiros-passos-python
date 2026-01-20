# variavel: espaço de memória
# existem tipos de memória

# TIPOS DE VARIAVEIS(dados)
    # Exemplos:
        # int = inteiro (1)
        # float = decimal (10.1)
        # string = texto (nome)

# Python tipifica as variaveis dinamicamente.
nome = "Brayan"
idade = 29
mensagem = "Meu nome é {} e eu tenho {} anos".format(nome,idade)

# função => palavra (argumentos)
print(mensagem)

# constantes
# Variavel que uma vez criada, não pode ser alterada
# Exemplo:
# pi = 3,14

PI = 3.14

# Entrada

valor_1 = int(input("Entre com um número inteiro: "))
valor_2 = int(input("Entre com outro número inteiro: "))

# Processamento

soma = valor_1 + valor_2

# Saída de dados

print(f"A soma de {valor_1} e {valor_2} é = {soma}")
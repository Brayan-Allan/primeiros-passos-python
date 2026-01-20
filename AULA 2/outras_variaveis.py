# Variaveis
nome = "Brayan" # texto (string)
num_int = 1500 # inteiro (sem virgula)
num_float = 15.30 # decimais (com vírgula)
var_booleana = True # ou False

# Outras variaveis
# Em python se chamam "listas"
# Em outras se chamam "vetor ou array"

# Declaração

lista = ["Brayan", 1500, 15.30]

# Exibindo minha lista completa

print(f"Aqui está minha lista: {lista}")

# Exibição de somente um item da lista

print(f"Aqui somente um item da minha lista: {lista[0]}")

# Imprimindo algo específico da minha lista

print(f"Aqui somente um item da minha lista: {0}")
if lista [0] == "Brayan":
    print ("sim")

# Matriz => no Python => Lista de listas
# Exemplo:
# 12 56 76
# 23 45 90
# 11 32 96

matriz = [[12, 56, 76],[23, 45, 90],[11, 32, 96]]

# Exibindo matriz completa

print(matriz)

# Exibindo item específico da matriz

print(matriz[2][2]) # primeiro ref. a linha e seg. ref. a coluna

# Outras variaveis
# Em python se chamam "dicionarios"
# dependente de uma linguagem intermediaria
# nesse caso, o mais usado é o JSON

#Declaração

dicionario = {"nome":"valor", "nome_1":"valor_1"}

# Exemplo:
aluno = "Brayan"
idade = 29
altura = 1.84
peso = 71

alunos = {"nome":"Brayan", "idade":29, "altura":1.84, "peso":71}

# Achando nome do aluno

print(alunos["nome"])

# Juntando os casos através de uma lista de dicionários

lista_dic = [
    {"nome":"Brayan", "idade":29, "altura":1.84, "peso":71},
    {"nome":"Alice", "idade":8, "altura":1.09, "peso":29},
    {"nome":"Ludmila", "idade":31, "altura":1.53, "peso":49},
]

# Exibindo idade da Alice

print(lista_dic[1]["idade"])

# Mais profundo

turma_1_2025 = {"aluno":{
    "cod_aluno":123,
    "nome":"Brayan",
    "cpf":12345578910
    },
    "disciplina":{
        "cod_disciplina":123,
        "nome_disciplina":"Python Intermediário"
    }
}
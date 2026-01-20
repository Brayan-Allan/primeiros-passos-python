# Funções lower & upper
# validação se a inserção foi minuscula ou maiuscula

# lower => minusculo
# upper => maiusculo

#Exemplo:

while True:
    print("imprimindo...")
    while True:
        resposta = input("Deseja continuar? (s/n) ")
        if resposta.upper() != "N" and resposta.upper() != "S":
            print("Não entendi sua resposta...")
        else:
            break
    if resposta.lower() == "n":
        break
    else:
        print("Ok, vamos continuar...")
        
print("Aqui acabou o exemplo de While (enquanto)...")
import random

NUMERO_SECRETO = random.randint(1,100)
palpites = []

print("JOGO DOS PALPITES!!!")

tentativa = 0

while True:
        tentativa += 1
        palpite = int(input("Qual seu palpite? "))
        palpites.append(palpite)
        if palpite < NUMERO_SECRETO:
            print(f"Seu palpite é MENOR!")
            print(f"Tente novamente...")
        elif palpite > NUMERO_SECRETO:
            print(f"Seu Palpite é MAIOR!")
            print(f"Tente novamente...")
        else:
            break
print("VOCÊ ACERTOU!!!")

print(f"O número SECRETO é: {palpite}")

print(f"Seus palpites foram {palpites}")

if tentativa <= 3:
    print("Você é um GÊNIO(a) da advinhação")
    print(f"Você acertou com: {tentativa} tentativas")
else:
    print(f"Você acertou com {tentativa} tentativas")
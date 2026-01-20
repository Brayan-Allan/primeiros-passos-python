from Pessoas import Pessoa

def principal():
    #criação de objeto
    pessoa_1 = Pessoa("Brayan","Allan","04/04/1996")
    print(pessoa_1.nome)
    print(pessoa_1.sobrenome)
    print(pessoa_1.nascimento)

    pessoa_2 = Pessoa("Alice","Kurowski","04/05/2017")
    print(pessoa_2.nome)
    print(pessoa_2.sobrenome)
    print(pessoa_2.nascimento)

if __name__ == "__main__":
    principal()
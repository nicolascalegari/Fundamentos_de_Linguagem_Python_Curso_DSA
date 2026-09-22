import random

def jogo():
    numero_secreto = random.randint(1, 20)
    tentativas = 5
    print("___Adivinhe o numero de 1 a 20.___")
    print("___5 Tentativas___")

    while tentativas > 0:
        print(f"\nVoce tem {tentativas} restante(s)!")
        palpite = int(input("Digite o seu palpite: "))

        if palpite == numero_secreto:
            print("Parabéns, Você acertou!")
            break
        elif palpite < numero_secreto:
            print("Muito baixo!")
        else:
            print("Muito alto!")
        tentativas -= 1

    else:
        print(f"\nFim de jogo! O numero secreto era: {numero_secreto}")

jogo()
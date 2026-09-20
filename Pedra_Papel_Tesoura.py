import os

# Apresentação
print("--- Jogo Pedra, Papel e Tesoura ---")
print()
print("Cada jogador deve escolher umas das opções.")

# Uso de tuplas (imutaveis)
opcoes_validas = ("pedra", "papel", "tesoura")
print(f"Opções válidas: {opcoes_validas}")
print()

# Coleta de dados
while True:

    # Coleta de dados
    jogador_1 = input("Jogador 1, digite a sua jogada: ")
    os.system('clear')
    print(f"Opções válidas: {opcoes_validas}")
    print()
    jogador_2 = input("Jogador 2, digite a sua jogada: ")
    os.system('clear')

    # Tratamento dos dados
    jogador_1 = jogador_1.lower().strip()
    jogador_2 = jogador_2.lower().strip()

    if jogador_1 in opcoes_validas and jogador_2 in opcoes_validas:
        break
    else:
        if jogador_1 not in opcoes_validas:
            print("Jogador 1 digitou uma opção inválida!")
        else:
            print("Jogador 2 digitou uma opção inválida!")

# Logica do jogo
# Empate
if jogador_1 == jogador_2:
    resultado = "Empate!"
# Jogador 1 Vencedor    
elif (jogador_1 == "pedra" and jogador_2 == "tesoura") or \
     (jogador_1 == "tesoura" and jogador_2 == "papel") or \
     (jogador_1 == "papel" and jogador_2 == "pedra"):
    resultado = "Jogador 1 é o VENCEDOR!"
# Jogador 2 Vencedor
else:   
    resultado = "Jogador 2 é o VENCEDOR!"

print(resultado)
print()
print("--Fim do Jogo---")
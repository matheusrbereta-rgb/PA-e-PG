import random

while True:
    numero = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Digite um número entre 1 e 100: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        tentativas += 1

        if palpite < numero:
            print("Maior!")
        elif palpite > numero:
            print("Menor!")
        else:
            print("\nParabéns! Você acertou!")
            print(f"Você precisou de {tentativas} tentativa(s).")
            break

    jogar = input("\nQuer jogar novamente? (sim/não): ").lower()

    if jogar != "sim":
        print("Até a próxima!")
        break
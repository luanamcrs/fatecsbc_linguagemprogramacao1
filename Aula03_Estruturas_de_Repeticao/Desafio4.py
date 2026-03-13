numero_secreto = 7
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número: "))

    if palpite > numero_secreto:
        print("Tente um número menor!")
    elif palpite < numero_secreto:
        print("Tente um número maior!")

print("Parabéns! Você acertou!")
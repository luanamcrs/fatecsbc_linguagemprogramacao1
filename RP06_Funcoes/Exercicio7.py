# Versão 1

def classificar_nota(n):
    if n >= 90:
        return "A"
    elif n >= 80:
        return "B"
    elif n >= 70:
        return "C"
    elif n >= 60:
        return "D"
    else:
        return "E"

nota = int(input("Nota: "))
print(classificar_nota(nota))

# Versão 2

def classificar_nota(n):
    if n >= 90:
        return "A"
    elif n >= 80:
        return "B"
    elif n >= 70:
        return "C"
    elif n >= 60:
        return "D"
    else:
        return "E"

nota = int(input("Nota: "))
print(classificar_nota(nota))
# VERSÃO 1 - PROCEDURAL

a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))

if a == b and b == c:
    print("Equilátero")
elif a == b or a == c or b == c:
    print("Isósceles")
else:
    print("Escaleno")

# VERSÃO 2 - COM FUNÇÃO

def classificar_triangulo(a, b, c):
    if a == b and b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))

print(classificar_triangulo(a, b, c))  
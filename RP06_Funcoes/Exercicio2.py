# Versão 1

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: ")) 
area = (base * altura)
print(f"A área do retângulo é: {area}")

# Versão 2
def calcular_area_retangulo(base, altura):
    return base * altura

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
print(f"A área do retângulo é: {calcular_area_retangulo(base, altura)}")
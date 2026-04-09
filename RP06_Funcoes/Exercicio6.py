# Versão 1

valor = float(input("Valor: "))
desc = float(input("Desconto (%): "))

final = valor - (valor * desc / 100)
print("Final:", final)

# Versão 2

def aplicar_desconto(valor, desc):
    return valor - (valor * desc / 100)

valor = float(input("Valor: "))
desc = float(input("Desconto (%): "))

print("Final:", aplicar_desconto(valor, desc))
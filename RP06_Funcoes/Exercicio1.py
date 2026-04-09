# Versão 1 (procedural)

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")

# Versão 2 (com função)
def verificar_paridade(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero = int(input("Digite um número: "))
print(verificar_paridade(numero))
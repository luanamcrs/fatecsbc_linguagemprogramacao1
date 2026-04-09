# VERSÃO 1 - PROCEDURAL

n = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# VERSÃO 2 - COM FUNÇÃO

def gerar_tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

n = int(input("Digite um número: "))
gerar_tabuada(n)   
# Versão 1

nome = input("Nome: ")
idade = int(input("Idade: "))

print(f"Bem-vindo {nome}, você tem {idade} anos!")

# Versão 2

def gerar_mensagem(nome, idade):
    return f"Bem-vindo {nome}, você tem {idade} anos!"

nome = input("Nome: ")
idade = int(input("Idade: "))

print(gerar_mensagem(nome, idade))
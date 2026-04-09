# Versão 1

senha = ""

while len(senha) < 8:
    senha = input("Digite uma senha: ")
print("Senha válida!")

# Versão 2

def validar_senha(s):
    return len(s) >= 8

senha = ""

while not validar_senha(senha):
    senha = input("Digite uma senha: ")
print("Senha válida!")

# WHILE (menu simples)

opcao = 0

while opcao != 3:
    print("\n1 - Olá")
    print("2 - Outra opção")
    print("3 - Sair")
    opcao = int(input("Escolha: "))

# FOR (contagem)

for i in range(1, 6):
    print("Número:", i)

# FOR (lista)

sabores = ["Chocolate", "Morango", "Baunilha", "Uva", "Limão"]

for sabor in sabores:
    print("Sabor:", sabor)

# DESAFIO 1

for i in range(1, 11):
    print(i)

nomes = ["Ana", "João", "Carlos", "Maria", "Luana"]
for nome in nomes:
    print(nome)


# DESAFIO 2

num = 0
while num <= 10:
    num = int(input("Digite um número: "))

print("Obrigado!")

# DESAFIO 3 (média)

soma = 0

for i in range(5):
    nota = float(input("Digite a nota: "))
    soma += nota

media = soma / 5
print("Média:", media)

# DESAFIO 4 (jogo)

segredo = 7
palpite = 0

while palpite != segredo:
    palpite = int(input("Adivinhe o número: "))
    
    if palpite > segredo:
        print("Menor!")
    elif palpite < segredo:
        print("Maior!")

print("Parabéns!")

# DESAFIO 5 (senha)

senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")

print("Bem-vindo!")

# MVP FINAL (menu estoque)

produtos = []

while True:
    print("\n1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    op = int(input("Escolha: "))

    if op == 1:
        nome = input("Nome: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))

        if quantidade < 0:
            print("Erro: quantidade negativa!")
        else:
            produtos.append((nome, quantidade, preco))

    elif op == 2:
        for p in produtos:
            print(p)

    elif op == 3:
        break
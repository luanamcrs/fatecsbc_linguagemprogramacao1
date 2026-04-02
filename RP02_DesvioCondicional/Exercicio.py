# PARTE 1 - Desvio Simples (if)

quantidade = 3

if quantidade < 5:
    print("Atenção: Estoque baixo!")

# PARTE 2 - Desvio Composto (if-else)

quantidade = 7

if quantidade < 5:
    print("Atenção: Estoque baixo!")
else:
    print("Estoque OK!")

# PARTE 3 - Desvio Múltiplo

quantidade = 2

if quantidade < 1:
    print("Em falta")
elif quantidade < 5:
    print("Alerta")
else:
    print("OK")

# TAREFA FINAL - VALIDAÇÃO

print("\n=== Cadastro de Produto ===")

nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço: "))

if quantidade < 0:
    print("Erro: A quantidade não pode ser negativa.")
else:
    print("\nProduto cadastrado com sucesso!")
    print("Nome:", nome)
    print("Quantidade:", quantidade)
    print("Preço:", preco)
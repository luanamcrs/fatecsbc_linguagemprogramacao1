# FUNÇÃO: EXIBIR MENU

def exibir_menu():
    print("\n1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

# FUNÇÃO: VERIFICAR ESTOQUE

def verificar_estoque_critico(quantidade):
    if quantidade < 5:
        return "Estoque baixo!"
    else:
        return "Estoque OK"

# FUNÇÃO: CABEÇALHO

def exibir_cabecalho():
    print("=== SORVETERIA DO DENER ===")

# PROGRAMA PRINCIPAL

produtos = []

while True:
    exibir_cabecalho()
    exibir_menu()

    op = int(input("Escolha: "))

    if op == 1:
        nome = input("Nome: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))

        if quantidade < 0:
            print("Erro: quantidade inválida!")
        else:
            produtos.append((nome, quantidade, preco))

    elif op == 2:
        for p in produtos:
            nome, quantidade, preco = p
            status = verificar_estoque_critico(quantidade)

            print("\nNome:", nome)
            print("Quantidade:", quantidade)
            print("Preço:", preco)
            print("Status:", status)

    elif op == 3:
        break
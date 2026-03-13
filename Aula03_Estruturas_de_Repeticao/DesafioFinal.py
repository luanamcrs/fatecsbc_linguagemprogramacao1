produtos = []

while True:
    print("\nMENU")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))

        while quantidade < 0:
            print("Quantidade não pode ser negativa.")
            quantidade = int(input("Digite novamente: "))

        preco = float(input("Preço do produto: "))

        produto = {
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco
        }

        produtos.append(produto)

    elif opcao == "2":
        print("\nProdutos em estoque:")

        for produto in produtos:
            print("Nome:", produto["nome"])
            print("Quantidade:", produto["quantidade"])
            print("Preço:", produto["preco"])
            print("----------------------")

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")
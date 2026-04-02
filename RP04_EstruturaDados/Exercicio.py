# LISTA DINÂMICA

produtos = []

produtos.append(("Chocolate", 10, 5.0))
produtos.append(("Morango", 3, 6.0))
produtos.append(("Baunilha", 0, 4.5))

# LISTANDO PRODUTOS

for produto in produtos:
    nome, quantidade, preco = produto

    if quantidade == 0:
        status = "Em falta"
    elif quantidade < 5:
        status = "Alerta"
    else:
        status = "OK"

    print("Nome:", nome)
    print("Quantidade:", quantidade)
    print("Preço:", preco)
    print("Status:", status)
    print("-------------------")
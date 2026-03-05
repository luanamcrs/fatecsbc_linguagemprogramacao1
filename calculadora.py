valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação: ")

if opcao == "1":
    print("Resultado:", valor1 + valor2)

elif opcao == "2":
    print("Resultado:", valor1 - valor2)

elif opcao == "3":
    print("Resultado:", valor1 * valor2)

elif opcao == "4":
    if valor2 != 0:
        print("Resultado:", valor1 / valor2)
    else:
        print("Erro: divisão por zero!")

else:
    print("Opção inválida.")
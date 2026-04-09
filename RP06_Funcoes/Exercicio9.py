# VERSÃO 1 - PROCEDURAL

texto = input("Digite uma palavra ou frase: ")
contador = 0

for letra in texto.lower():
    if letra in "aeiou":
        contador += 1

print("Quantidade de vogais:", contador)

# VERSÃO 2 - COM FUNÇÃO

def contar_vogais(texto):
    contador = 0
    for letra in texto.lower():
        if letra in "aeiou":
            contador += 1
    return contador

texto = input("Digite uma palavra ou frase: ")
print("Quantidade de vogais:", contar_vogais(texto))
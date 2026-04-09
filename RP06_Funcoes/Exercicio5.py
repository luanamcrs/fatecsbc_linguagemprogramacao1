# Versão 1

c = float(input("Celsius: "))
f = (c * 9/5) + 32

print("Fahrenheit:", f)

# Versão 2

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

c = float(input("Celsius: "))
print("Fahrenheit:", celsius_para_fahrenheit(c))
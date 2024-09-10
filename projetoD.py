contador = 0 
soma = 0 
print("Digite [0] para sair")
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break 
    contador += 1 
    soma += numero 
media = soma / contador 
print(f"A quantidade de valores digitados foi: {contador} ") 
print(f"A soma dos valores digitados é: {soma} ")
print(f"A média dos valores é: {media} ")
print(f"{contador} > 20")

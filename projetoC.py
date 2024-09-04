contador = 0 
soma = 0 
print("Digite o número [0] para sair.")
while True: 
    numero = int(input("Digite os números: "))
    if numero == 0:
        break
    resto = numero % 2 
    if resto == 0: 
        soma += numero 
        contador += 1 
media = soma / contador 
print(f"A média de todos os pares é: {media:.4f}")
print(f"A quantidade de números é : {contador}")


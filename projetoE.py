menor_valor = float("inf")
maior_valor = float("-inf")
contador = 0 
soma = 0 
print("Digite [0] pra sair.")
while True:
    valor = int(input("Digite um número: "))
    if valor == 0:
        break 
    contador += 1
    soma += valor  
    if valor < menor_valor: 
        menor_valor = valor 
    if valor > maior_valor: 
        maior_valor = valor 
media = soma / contador
print(f"O maior valor é:  {maior_valor }") 
print(f"O menor valor é: {menor_valor }")
print(f"A quantidade dos valores é: {contador }")
print(f"A soma dos valores é: {soma} ")
print(f"A média dos números é: {media} ")



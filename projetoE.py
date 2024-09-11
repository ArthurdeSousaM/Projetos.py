menor_valor = float("inf")
maior_valor = float("-inf")
print("Digite [0] pra sair.")
while True:
    valor = int(input("Digite um número: "))
    if valor == 0:
        break 
    if valor < menor_valor: 
        menor_valor = valor 
    if valor > maior_valor: 
        maior_valor = valor 
print(f"O maior valor é:  {maior_valor }") 
print(f"O menor valor é : {menor_valor }")

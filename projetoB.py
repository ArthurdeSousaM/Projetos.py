menor_valor = float("inf") # valor inicial da variável. float("inf") é o maior valor em python  
print("Digite o valor [0] para sair.") # sair do programa 
while True: # código que roda o programa várias vezes 
    valor = int(input("Digite o valor: ")) # digite o valor inteiro 
    if valor == 0: 
        break # sai do while , encerra o programa 
    if valor < menor_valor: 
        menor_valor = valor  #Atualiza a variável menor valor 
print(f"O menor valor é: {menor_valor}") #executar 


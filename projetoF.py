contador_par = 0
soma_par = 0 
contador_impar = 0
soma_impar = 0 
print("Digite [0] para sair. ")
while True:
    numero = int(input("Digite os números: "))
    if numero == 0: 
        break 
    resto = numero % 2 
    if resto == 0:
        soma_par += numero  
        contador_par += 1 
    else:
        soma_impar += numero 
        contador_impar += 1 
media_par = soma_par / contador_par
media_impar = soma_impar / contador_impar
print(f"A média dos números pares é: {media_par} ")
print(f"A média dos números ímpares é: {media_impar} ")

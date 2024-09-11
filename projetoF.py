maior_altura = float("-inf")
menor_altura = float("inf") 
homens = 0 
mulheres = 0
print("Dgite [0] para sair.")
while True: 
    genero = input("Digite seu gênero [M] ou [F]: ")
    altura = float(input("Digite a sua altura: "))
    if altura == 0:
        break 
    if altura > maior_altura: 
        maior_altura = altura 
    if altura < menor_altura: 
        menor_altura = altura 
    if genero == 'f':
        mulheres += 1
    if genero =='m':
        homens += 1 
print(f"Maior altura do grupo é: {maior_altura:.2f} ")
print(f"Meor altura do grupo é: {menor_altura:.2f} ")
print(f"A quantidade de homens é: {homens} ")
print(f"A quantidade de mulheres é: {mulheres}")

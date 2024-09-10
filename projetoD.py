def media_soma_valores_digitados():
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
    print(f"{contador} > 20 ")
    avaliacao()


def aprovados_reprovados():
    aluno = 0 
    aprovados = 0
    reprovados = 0   
    print("Digite [0] para sair. ")
    while True: 
        nota = int(input("Digite a nota: "))
        if nota == 0: 
            break
        aluno += 1 
        if nota >=5:
            aprovados += 1 
        else: 
            reprovados += 1
    print(f"A quantidade de alunos que fizeram a prova foram: {aluno} ")
    print(f"A quantidade de alunos aprovados foram: {aprovados} ")
    print(f"A quantidade de alunos reprovados foram: {reprovados} ")
    avaliacao()


def impar_par():
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
    avaliacao()


def avaliacao():
    print("/n Qual programa deseja executar?: ")
    print("a) Calcular a média e a soma dos valores: ")
    print("b) Calcular alunos aprovados e reprovados: ")
    print("c) Calcular a média de números ímpares e pares: ")
    
    escolha = input("Qual programa deseja executar (a, b, c): ")
    if escolha == "a":
        media_soma_valores_digitados()
    elif escolha == "b":
        aprovados_reprovados()
    elif escolha == "c": 
        impar_par()
    else: 
        print("Escolha inválida. ")

avaliacao()

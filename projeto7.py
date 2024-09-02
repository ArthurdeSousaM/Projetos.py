def maior_numero_sem_operadores():
    # Programa para calcular o maior número entre três fornecidos pelo usuário sem usar operadores lógicos 
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))
    c = float(input("Digite o terceiro valor: "))
    maior_ab = (a + b + abs(a - b)) / 2
    maior_abc = (maior_ab + c + abs(maior_ab - c)) / 2
    print(f"O maior valor é: {maior_abc}")
    avaliacao()
    



def maior_numero_com_operadores():
    # Programa para calcular o maior número entre três fornecidos pelo usuário usando operadores lógicos 
    valor1 = float(input("Digite o valor 1: "))
    valor2 = float(input("Digite o valor 2: "))
    valor3 = float(input("Digite o valor 3: "))
    if (valor1 > valor2 and valor1 > valor3):
        print(f"O {valor1} é o maior número.")
    elif (valor2 > valor1 and valor2 > valor3):
        print(f"O {valor2} é o maior número.")
    elif (valor3 > valor1 and valor3 > valor2):
        print(f"O {valor3} é o maior número.")
    else:
        valor1 == valor2 or valor1 == valor3 
        print("Os números são iguais.")
        avaliacao()
        


def calculadora():
    # Um programa que simula uma calculadora com as quatro operações aritméticas básicas.
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    print("Escolha sua operação: ")
    print("+ : adição")
    print("- : subtração")
    print("* : multiplicação")
    print("/ : divisão")

    operacao = input("Tecle a operação de sua escolha: ")
    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            resultado = "Erro: não se pode dividir por zero."
    else:
        resultado = "Operação inválida."

    print(f"O resultado da operaçao é: {resultado}")
    avaliacao()



def avaliacao():
    # Forma do usuário escolher qual programa ele deseja executar 
    print("\nEscolha qual programa deseja executar: ")
    print("a) Selecionar o maior valor entre três números (Sem operador lógico) ")
    print("b) Selecionar o maior valor entre três números (Com operador lógico)")
    print("c) Selecionar calculadora com as quatro operações aritméticas básicas")

    escolha = input("Digite a letra correspondente ao exercício que deseja (a, b, c,): ")
    if escolha == "a": 
        maior_numero_sem_operadores()
    elif escolha == "b":
        maior_numero_com_operadores()
    elif escolha == "c":
        calculadora()
    else:
        print("Escolha inválida")
    print("\nVoltando ao menu principal...")
    avaliacao()


avaliacao()

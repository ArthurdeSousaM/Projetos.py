def converter_medidas():
    medida = input("Selecione a unidade de medida [M] ou [KM]: ")
    numero = float(input("Digite o valor que deseja converter: "))
    km_m = numero * 1000 
    m_km = numero / 1000 
    if medida == 'km':
        km_m 
        print(f"O valor {numero:.0f} em quilômetros convertido para metros é: {km_m:.0f} ")
    elif medida == 'm':
        m_km 
        print(f"O valor {numero:.0f} em metros convertido para quilômetros é: {m_km:.0f} ")
    else:
        print("Escolha inválida.")
    treino()


def operacoes():
    operacao = input("Digite a operação que deseja executar [+], [-], [/], [*]: ") 
    print("Digite [0] na seleção (valor1) para sair do programa. ")
    while True: 
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        if valor1 == 0: 
            break 
        if operacao == '+':
            soma = valor1 + valor2 
            print(f"A soma entre {valor1} e {valor2} é igual a {soma}. ")
        if operacao == '-': 
            subtracao = valor1 - valor2 
            print(f"A subtração entre {valor1} e {valor2} é igual a {subtracao}. ")
        if operacao == '/':
            divisao = valor1 / valor2
            print(f"A divisão entre {valor1} e {valor2} é igual a {divisao:.0f}. ")
        if operacao == '*':
            multiplicacao = valor1 * valor2
            print(f"A multiplicação entre {valor1} e {valor2} é igual a {multiplicacao}. ")
    treino()


def classificar_idade():
    print("Digite [0] para sair.") 
    while True:
        idade = int(input("Digite a idade que deseja classificar: "))
        if idade == 0:
            break
        if idade <= 17:
            print(f"Se você tem {idade} anos, você é menor de idade.")
        if idade >= 18 and idade <= 64:
            print(f"Se você tem {idade} anos, você é adulto.")
        if idade >= 65:  
            print(f"Se você tem {idade} anos, você é idoso. ")
    treino()


def treino():
    print("\nEscolha qual programa deseja executar: ")
    print("a) Selecionar programa que converte medidas entre KM e M: ")
    print("b) Selecionar programa que executa a operação que o usuário escolher: ")
    print("c) Selecionar programa que classifica idade digitada pelo usuário: ")

    escolha = input("Digite a letra correspondente ao programa que deseja (a, b, c,): ")
    if escolha == "a": 
        converter_medidas()
    elif escolha == "b":
         operacoes()
    elif escolha == "c":
        classificar_idade()       
    else:
        print("Escolha inválida")
    print("\nVoltando ao menu principal...")
    treino()


treino()

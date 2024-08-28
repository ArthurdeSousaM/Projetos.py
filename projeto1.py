import math


def calcular_volume_da_esfera():
    raio = float(input("digite o raio da esfera: "))
    volume = (4 / 3) * math.pi * (raio ** 3)
    print(f"O volume da esfera é: {volume}")
    print("\nSelecione sua escolha...")
    Avaliacao_pratica()


def calcular_distancia_entre_pontos():
    x1 = float(input("digite o valor de x1: "))
    y1 = float(input("digite o valor de y1: "))
    x2 = float(input("digite o valor de x2: "))
    y2 = float(input("digite o valor de x2: "))
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"A distância dos pontos é: {distancia}")
    print("\nSelecione sua escolha...")
    Avaliacao_pratica()


def classificando_valores():
    a = int(input("digite o valor de a: "))
    b = int(input("digite o valor de b: "))

    if a < b:
        print(f"Os números em ordem crescente são: {a} e {b}")
    elif a > b:
        print(f"Os números em ordem crescente são: {b} e {a}")
    else:
        print(f"Os números são igual: {a} e {b}")
        print("\nSelecione sua escolha...")
    Avaliacao_pratica()


def calcular_peso_ideal():
    genero = input("digite seu gênero (homem/mulher): ").lower()
    altura = float(input("digite sua altura: "))

    if genero == "homem":
        peso_ideal = (72.7 * altura) - 58
        print(f"O peso ideal de um homem de {altura:.2f} metros é: {peso_ideal:.2f} kg")
    elif genero == "mulher":
        peso_ideal == (62.1 * altura) - 44.7
        print(f"O peso ideal de uma mulher de {altura:.2f} metros é: {peso_ideal:2f} kg")
    else:
        print("gênero invalido.")
        print("\nSelecione sua escolha...")
        Avaliacao_pratica()


def Avaliacao_pratica():
    print("\nEscolha o que deseja executar:")
    print("a) Calcular o volume da esfera")
    print("b) Calcular a distância entre dois pontos")
    print("c) Classificar dois valores inteiros em ordem crescente")
    print("d) Calcular peso ideal")

    escolha = input("digite qual delas deseja executar (a, b, c, d): ")
    if escolha == "a":
        calcular_volume_da_esfera()
    elif escolha == "b":
        calcular_distancia_entre_pontos()
    elif escolha == "c":
        classificando_valores()
    elif escolha == "d":
        calcular_peso_ideal()
    else:
        print("Escolha inválida.")
Avaliacao_pratica()

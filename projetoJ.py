import random 


def valor_final_fornecido_pelo_usuario():
    contador = 0
    valor_final = int(input("Digite o valor final: "))
    for numero in range (1, valor_final):
        contador += 1
        print(numero)
    print(f"A quantidade de números na sequência foi {contador}") 
    print("\nSelecione sua escolha...")
    Avaliacao_pratica()


def sequencia_do_dobro():
    soma = 0 
    contador = 0
    print("A sequência do dobro dos números naturais até dez.")
    for numero in range (1,11):
        dobro = numero * 2
        print(dobro)
        contador += 1
        soma += dobro
        
    media = soma / contador 
    print(f"A soma dos valores é {soma}")
    print(f"A média dos valores é {media:.0f}")
    print("\nSelecione sua escolha...")
    Avaliacao_pratica()


def turma_com_50_alunos():
    soma_notas = 0
    for numero in range (1,51):
        nota = float(input(f"Digite a nota do aluno {numero}: "))
        soma_notas += nota 
    media = soma_notas / 50
    print(f"A média dessa turma é: {media:.2f} ")
    print("\nSelecione sua escolha...")
    Avaliacao_pratica()


def fahrenheit_para_celsius():
    print(f"{'Fahrenheit':<12}{'Celsius':<10}")
    for fahrenheit in range(45,81):
        celsius = 5 * (fahrenheit - 32) / 9
        print(f"{fahrenheit:<12.1f}{celsius:<10.3f}")
    print("\nSelecione sua escolha...")
    Avaliacao_pratica()


def cinco_numeros_aleatorios():
    for numero in range(1,6):
        numero_sorteado = random.randint(1,95)
        print(numero_sorteado)
    print("\nSelecione sua escolha...")
    Avaliacao_pratica()
    

def Avaliacao_pratica():
    print("\nEscolha o que deseja executar:")
    print("a) Sequência dos números naturais até um valor final fornecido pelo usuário")
    print("b) Sequência do dobro dos números naturais até dez. Calculando também a soma e a média.")
    print("c) Média aritmética de uma turma com cinquenta alunos. Onde cada aluno realizou uma avaliação.")
    print("d) A conversão de graus Fahrenheit para graus Celsius.")
    print("e) Programa que gere cinco números inteiros aleatórios sorteados pelo computador. Em intervalo de 0 a 95.")


    
    escolha = input("digite qual delas deseja executar (a, b, c, d, e): ")
    if escolha == "a":
        valor_final_fornecido_pelo_usuario()
    elif escolha == "b":
        sequencia_do_dobro()
    elif escolha == "c":
        turma_com_50_alunos()
    elif escolha == "d":
        fahrenheit_para_celsius()
    elif escolha == "e":
        cinco_numeros_aleatorios()
    else:
        print("Escolha inválida.")
Avaliacao_pratica()




   

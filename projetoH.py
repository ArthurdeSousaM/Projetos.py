import random

def casa_harry_potter():
    #Programa no qual o usuário responde pergunta e de acordo com suas respostas é definida uma casa no universo de harry potter.
    grifinoria = 0
    corvinal = 0
    lufa_lufa = 0
    sonserina = 0
    print("Q1) Você gosta do amanhecer ou do anoitecer? ")
    print("1) Amanhecer. ")
    print("2) Anoitecer. ")
    q1 = int(input("Digite [1] ou [2]: "))

    
    print("Q2) Quando eu morrer, quero que as pessoas se lembrem de mim como?")
    print("1) O Bom.")
    print("2) O Grande.")
    print("3) O Sábio.")
    print("4) O Audacioso.")
    q2 = int(input("Digite [1], [2], [3] ou [4]: "))
    
    
    print("Q3) Que tipo de instrumento mais agrada seus ouvidos?")
    print("1) O violino")
    print("2) O trompete")
    print("3) O piano")
    print("4) O tambor")
    q3 = int(input("Digite [1], [2], [3] ou [4]: "))
    
    
    if q1 == 1:
      grifinoria += 1
      corvinal += 1 
    elif q1 == 2:
      lufa_lufa += 1
      sonserina += 1
      
    
    if q2 == 1:
      lufa_lufa += 2
    elif q2 == 2:
      sonserina += 2
    elif q2 == 3:
      corvinal += 2
    elif q2 == 4:
      grifinoria += 2
      
      
    if q3 == 1:
      sonserina += 4
    elif q3 == 2: 
      lufa_lufa += 4
    elif q3 == 3:
      corvinal += 4
    elif q3 == 4:
      grifinoria += 4
      
      
    if grifinoria > corvinal and grifinoria > lufa_lufa and grifinoria > sonserina:
      print("Você é da casa Grifinória!")
    elif corvinal > grifinoria and corvinal > lufa_lufa and corvinal > sonserina:
      print("Você é da casa Corvinal!")
    elif lufa_lufa > grifinoria and lufa_lufa > corvinal and lufa_lufa > sonserina:
      print("Você é da casa Lufa-Lufa!")
    elif sonserina > grifinoria and sonserina > corvinal and sonserina > lufa_lufa:
      print("Você é da casa Sonserina!")
    else: 
      print("Escolha inválida.")
    inicial_codedex()



def resposta_aleatoria():
    #Programa no qual o usuário fornece uma pergunta de sim ou não e recebe uma resposta aleátoria.
    
    pergunta = input("Digite qualquer pergunta de sim ou não: ")
    resposta_1 = "Definitivamente."
    resposta_2 = "Melhor nao te contar agora."
    resposta_3 = "Minhas fontes dizem que não."
    resposta_4 = "Muito duvidoso." 
    numero = random.randint(1, 4)
    if numero == 1:
        print(resposta_1)
    elif numero == 2:
        print(resposta_2)
    elif numero == 3:
       print(resposta_3)
    elif numero == 4:
       print(resposta_4)
    inicial_codedex()



def altura_creditos(): 
    #Programa no qual o usuário fornece sua altura e seus créditos á um parque de diversões para ser permitido ou não a ir na montanha russa.
    altura = float(input("Digite sua altura em cm: "))
    creditos = int(input("Digite a quantidade de créditos que você tem: "))
    if altura >= 137 and creditos >= 10:
       print("Aproveite o passeio!")
    elif creditos >= 10 and altura < 136: 
       print("Você não tem altura suficiente para o brinquedo.")
    elif altura >= 137 and creditos < 9: 
       print("Você não tem crédios o suficiente.")
    else: 
       print("Você não atende os requisitos.")
    inicial_codedex()



def inicial_codedex():
    print("\nEscolha o que deseja executar:")
    print("a) Sortear a casa do universo de harry potter.")
    print("b) Escrever uma resposta aleatória para uma pergunta de sim ou não.")
    print("c) Requisitos para ir ou não na montanha russa.")

    escolha = input("Escolha o que deseja executar [a], [b] ou [c]: ")
    if escolha == "a":
        casa_harry_potter()
    elif escolha == "b":
       resposta_aleatoria()  
    elif escolha == "c":
        altura_creditos()
    else: 
       print("Escolha inválida.")


inicial_codedex()

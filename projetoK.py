variavel2 = 20
variavel4= int(input("Digite um valor: "))
variavel5 = int(input("Digite um valor: "))


def mostrar_valor(Variavel):
    print(f"O valor é: {Variavel}")



def mostrar_valor2(variavel2):
    print(f"O valor é: {variavel2}")


def mostrar_valor3():
    input("O valor é: ")


def mostrar_valor4(variavel4, variavel5):
    print(f"O valor é: {variavel4}")
    print(f"O valor é: {variavel5}")


def calcular_dobro(valor):
    dobro = valor * 2
    return dobro


def calcular_triplo(valor2):
    triplo = valor1 * 3
    return triplo


def somar_valores(a, b):
    return a + b


valor = int(input("Digite um valor: "))
valor1 = int(input("Digite um valor: "))
a = 10
b = 60 
print(somar_valores(a, b))
print("Inicio do programa")
mostrar_valor(10)
mostrar_valor(10.5)
mostrar_valor(-10)
mostrar_valor2(variavel2)
mostrar_valor3()
mostrar_valor4(variavel4, variavel5)
calcular_dobro(valor)
calcular_triplo(valor1)
print(f"O dobro do valor é: {calcular_dobro(valor)}")
print(f"O triplo do valor é: {calcular_triplo(valor1)}")
print("Fim do programa")

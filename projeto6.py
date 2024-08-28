#programa para calcular raízes quadradas de uma equação do segundo grau onde o usuário fornece os dados das variantes
import math 

a = float(input("Digite o valor da variante a: "))
b = float(input("Digite o valor da variante b: "))
c = float(input("Digite o valor da variante c: "))

delta = b**2 - 4*a*c 
print(delta)
if (a == 0 or b == 0 or c == 0):
    print("A variavel não pode ser zero.")
elif delta > 0:
    raiz1 = (-b + math.sqrt(delta)) / (2*a) 
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"As raízes da equação são: {raiz1} e {raiz2}")
elif delta == 0: 
    raiz = -b / (2*a)
    print(f"A equação possui uma raiz dupla: {raiz}")
else: 
    print("A equação não possui raízes reais. ")

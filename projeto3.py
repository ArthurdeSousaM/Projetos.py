nota1 = float(input("Insira a nota1 "))
nota2 = float(input("Insira a nota2 "))
media = (nota1 + nota2) /2
if media >= 5:
    print(f"Aluno aprovado {media:.2f}")
else:
    print(f"Aluno reprovado {media:.2f}")  
#if será executado quando a media for >= 5
# else será executado quando a media for qualquer valor diferente de >= 5
# .2f é usado para atribuir duas casas decimais ao resultado  

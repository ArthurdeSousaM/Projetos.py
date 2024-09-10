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

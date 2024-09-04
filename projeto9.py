aluno = 0 
soma = 0
print("Digite [-1] para sair ")
while True: 
    nota = float(input("Digite a nota "))
    if nota == -1:
        break
    aluno = aluno + 1  
    soma = soma + nota  
media = soma / aluno 
print(f"A quantidade de alunos é: {aluno} e a média da turma é: {media}")

    

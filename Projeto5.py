Ano_Nascimento = int(input("Digite o ano do seu nascimento: "))
idade = 2024 - Ano_Nascimento
print(f"Sua idade é: {idade}")
if (idade >= 16 and  idade <=17):
    print("Pode votar")
elif idade >= 18:
    print("Pode votar e tirar CNH")    
else: 
    print("Não pode votar e não pode tirar CNH")  
print(f"Sua data de nascimento é: {Ano_Nascimento}")

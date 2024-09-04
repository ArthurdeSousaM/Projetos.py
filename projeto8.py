contador =0 #valor inicial da váriavel 
soma = 0 
print("Digite [-1] para sair ")
while True: #comando que sempre faz o programa rodar se a condição for verdadeira 
    numero = int(input("Digite os números: "))  #INDENTAÇÃO OBRIGATÓRIA
    if numero == -1:
        break #comando para sair da repetição feita pelo while
    contador = contador + 1 #contador +1 sempre que rodar o programa e um número for adicionado, o programa guarda quantos números rodou na repetição 
    #fim da estrutura de repetição feita pelo while 
    soma = soma + numero
print(f"A quantidade de números foram: {contador}")
print(f"A soma dos valores é: {soma}")

compra = float(input("Digite o valor  da compra: "))
venda = float(input("Digite o valor da venda: "))
diferenca = venda - compra 
if compra < venda:
    print(f"Teve lucro {diferenca}")
elif compra > venda:
    print(f"Teve prejuízo {diferenca}")
else:
    print("Os valores são iguais")
print(f"Valor da compra: {compra:.21200f}")
print(f"Valor da venda: {venda:.2f}")

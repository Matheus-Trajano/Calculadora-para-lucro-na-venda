Varvendedor = str(input("olá, digite sua credencial de vendedor: "))
Varproduto = float(input("digite o valor total da venda: "))

Var1 = Varproduto * 0.1
Var2 = Varproduto / 3
Var3 = Varproduto * 0.05
Var4 = Varproduto * 0.05

print("Olá,", Varvendedor)
print("O total a pagar com desconto é : R$", Var1)
print("O valor de cada parcela, em caso de parcelamento em 3 vezes é: R$", Var2)
print("A comissão do vendendor, caso a venda seja à vista é: R$", Var3)
print("A comissão do vendedor, caso a venda seja parcelada é: R$", Var4)

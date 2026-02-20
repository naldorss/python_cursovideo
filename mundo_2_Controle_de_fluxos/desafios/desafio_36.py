'''
Escreva um programa para aprovar um emprestimo bancário para a compra de uma casa. 
O programa deve perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
valor_casa = float(input('Qual o valor do imóvel? '))
salário_comprador = float(input('Qual o seu salário? '))
quantos_meses = int(input('Quantos mêses de financiamento? '))

prestacao = valor_casa / quantos_meses
valor_max_prestacao = salário_comprador * 0.3

print(f"O imóvel vale {valor_casa}, o comprador tem um salário de {salário_comprador}")
print(f"Dividido em {quantos_meses} mêses, o valor de cada parcela será {prestacao} R$")

if valor_max_prestacao / salário_comprador >= 0.3:
    print("Esse valor não cabe no seu bolso")
else:
    print("Vamos fechar negócio")


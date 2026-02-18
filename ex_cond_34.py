salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    aumento = salario + (salario * 0.15)
else:    aumento = salario + (salario * 0.10)
print(f"O novo salário do funcionário é R${aumento:.2f}")

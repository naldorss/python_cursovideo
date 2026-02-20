distancia = float(input('Qual é a distância da viagem em km? '))

if distancia <= 200:
    preço = distancia * 0.50
else:    preço = distancia * 0.45
print(f"O preço da passagem é R${preço:.2f}")
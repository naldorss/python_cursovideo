# Conversão de moedas:

real = float(input('Digite o valor em reais: R$ '))
dolar = float(input('Digite a cotação do dólar: US$ '))
conversão = real / dolar
print(f'Com R$ {real:.2f} você pode comprar US$ {conversão:.2f}.')
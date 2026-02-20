# qual a idade do meu carro?
from datetime import date


data_fabricacao = date(int(input("Digite o ano de fabricação do seu carro: ")), 1, 1)
ano_atual = date.today().year
idade_carro = ano_atual - data_fabricacao.year
print(f"O seu carro tem {idade_carro} anos.")

if idade_carro < 3:
    print("O seu carro é novo.")
elif idade_carro < 10:
    print("O seu carro é usado.")
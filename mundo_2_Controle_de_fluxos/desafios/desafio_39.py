'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
    - Se ele ainda vai se alistar ao serviço militar.
    - Se é a hora de se alistar.
    - Se ja passou do tempo de alistamento.
O programa deve mostrar quanto tempo falta até o alistamento ou quanto tempo já se passou
desde do periodo de alistamento.
'''
from datetime import date, datetime
data_nascimento = date(input("Digite sua data de nascimento:" ))
data_atual = date.today()
idade = data_atual - data_nascimento

print("Voce tem:", idade)


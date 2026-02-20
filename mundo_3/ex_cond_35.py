'''
Desenvolva um programa que leia o comprimento de três retas e diga 
ao usuário se elas podem ou não formar um triângulo.

Regra: A soma de um dos lados deve ser menos que a soma dos outros dois lados.
'''
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("As retas podem formar um triângulo.")
else:    print("As retas não podem formar um triângulo.")

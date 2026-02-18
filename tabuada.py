# Faça um programa que leia um número inteiro e mostre a sua tabuada.

num = int(input("Digite um número inteiro para ver a sua tabuada: "))
print(f"A tabuada de {num} é: ")
for i in range(1,11):
    print(f'{num} X {i} = {num * i}')


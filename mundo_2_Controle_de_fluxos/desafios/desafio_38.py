'''Escreva um programa que leia dois numeros inteiros e compare-os,
    mostrando na tela uma mensagem:
        O primeiro valor é maior
        O segundo valor é maior
        Os dois valores são iguais'''

valor_1 = int(input('O valor 1 é: '))
valor_2 = int(input('O valor 2 é: '))

if valor_1 > valor_2:
    print("O valor 1 é maior")
elif valor_2 > valor_1:
    print("O valor 2 é maior")
else:
    print("Os valores são iguais")
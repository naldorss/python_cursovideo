'''
Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
    - Média abaixo de 5.0: Reprovado
    - Média entre 5.0 e 6.9: Recuperação
    - Média 7.0 ou superior: Aprovado
'''

nota_1 = int(input("Nota 1: "))
nota_2 = int(input("Nota 2: "))

media = (nota_1 + nota_2) / 2
if media < 5.0:
    print(f'Sua média foi {media}, vc está reprovado')
elif media > 5.0 or media <= 6.9:
    print(f'Sua média foi {media}, vc está em recuperação')
elif media >= 7.0:
    print(f'Sua média foi {media}, vc está aprovado')
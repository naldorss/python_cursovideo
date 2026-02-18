import random

Aluno_1 = str(input("Digite o nome do primeiro aluno: "))
Aluno_2 = str(input("Digite o nome do segundo aluno: "))        
Aluno_3 = str(input("Digite o nome do terceiro aluno: "))
Aluno_4 = str(input("Digite o nome do quarto aluno: "))
Lista = [Aluno_1, Aluno_2, Aluno_3, Aluno_4]
Escolhido = random.choice(Lista)
print(f"O aluno escolhido foi: {Escolhido}")

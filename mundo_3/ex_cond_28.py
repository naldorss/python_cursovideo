from random import randint
from time import sleep

computador = randint(0, 5)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
jogador = int(input("Em que número eu pensei? "))
print("Processando...")
sleep(2)
if jogador == computador:
    print("Parabéns! Você acertou!")
else:    print(f"Que pena! Eu pensei no número {computador}. Tente novamente!")

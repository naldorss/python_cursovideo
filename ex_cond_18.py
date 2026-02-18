import math

angulo = float(input("Digite o ângulo que vc deseja: "))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"O seno de {angulo} é igual a {seno:.2f}")
print(f"O coseno de {angulo} é igual a {coseno:.2f}")
print(f"A tangente de {angulo} é igual a {tangente:.2f}")

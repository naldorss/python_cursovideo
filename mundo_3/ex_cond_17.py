import math
# o quadrado da hipotenusa é igual a soma dos quadrados dos catetos
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
#hipotenusa = (cateto_adjacente ** 2 + cateto_oposto ** 2)** (1/2)
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f"O valor da hipotenusa é {hipotenusa:.2f}.")


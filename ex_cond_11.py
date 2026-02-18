altura = float(input("Digite a altura de sua parede: "))
largura = float(input("Digite a largura de sua parede: "))
area = altura * largura
print(f"A altura da parede é {altura}m, a Largura é {largura}m, e a área é {area}m².")

Qtd_tinta = area / 2
print(f"Você precisará de {Qtd_tinta} litros de tinta para pintar a parede.")
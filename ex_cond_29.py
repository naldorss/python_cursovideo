velocidade = float(input('Qual é a velocidade atual do carro? '))
print("Tenha um bom dia! Dirija com segurança!")

if velocidade > 80:
    print("Você foi multado por excesso de velocidade!")
    multa = (velocidade - 80) * 7
    print(f"O valor da multa é R${multa:.2f}")

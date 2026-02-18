nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")

média = (float(nota1) + float(nota2)) / 2
print(f"A média das notas é: {média}")

if média >= 7:
    print("Parabéns, você foi aprovado!")
elif média >= 5:
    print("Você está de recuperação.") 
else:    
    print("Infelizmente, você foi reprovado.")


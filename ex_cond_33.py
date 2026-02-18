num_a = int(input('Digite o primeiro número: '))
num_b = int(input('Digite o segundo número: '))
num_c = int(input('Digite o terceiro número: '))
# quem é o menor número?
if num_a < num_b and num_a < num_c:
    print(f"O menor número é {num_a}.")
elif num_b < num_a and num_b < num_c:
    print(f"O menor número é {num_b}.")

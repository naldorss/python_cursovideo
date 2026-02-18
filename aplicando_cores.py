print('\033[31m' + 'Vermelho' + '\033[0m')
print('\033[32m' + 'Verde' + '\033[0m')
print('\033[33m' + 'Amarelo' + '\033[0m')
print('\033[34m' + 'Azul' + '\033[0m')          
print('\033[35m' + 'Roxo' + '\033[0m')
print('\033[36m' + 'Ciano' + '\033[0m')
print('\033[37m' + 'Branco' + '\033[0m')
print('\033[30m' + 'Preto' + '\033[0m')

# Cores de fundo
print('\033[41m' + 'Vermelho' + '\033[0m')
print('\033[42m' + 'Verde' + '\033[0m')     
print('\033[43m' + 'Amarelo' + '\033[0m')
print('\033[44m' + 'Azul' + '\033[0m')
print('\033[45m' + 'Roxo' + '\033[0m')
print('\033[46m' + 'Ciano' + '\033[0m') 
print('\033[47m' + 'Branco' + '\033[0m')
print('\033[40m' + 'Preto' + '\033[0m')

# Cores de fundo e texto
print('\033[31;43m' + 'Vermelho com fundo amarelo' + '\033[0m')
print('\033[32;44m' + 'Verde com fundo azul' + '\033[0m')
print('\033[33;45m' + 'Amarelo com fundo roxo' + '\033[0m')
print('\033[34;46m' + 'Azul com fundo ciano' + '\033[0m')
print('\033[35;47m' + 'Roxo com fundo branco' + '\033[0m')
print('\033[36;40m' + 'Ciano com fundo preto' + '\033[0m')
print('\033[37;41m' + 'Branco com fundo vermelho' + '\033[0m')
print('\033[30;42m' + 'Preto com fundo verde' + '\033[0m')  


a = input("Digite algo: ")
b = input("Digite algo: ")
c = input("Digite algo: ")

print(f'Os valores são \033[32;44m{a}\033[0m, \033[32;44m{b}\033[0m e \033[32;44m{c}\033[0m.')

#nome = input('Qual é o seu nome? ')
#print(f'A informação armazenada foi {nome=}')

print('---------------------')
print('CALCULADORA DE PYTHON')
print('---------------------')
print('CÁLCULOS COMPÁTIVEIS')
print()
print('-ADIÇÃO-')
print()
print('-SUBTRAÇÃO-')
print()
print('-MULTIPLICAÇÃO-')
print()
print('-DIVISÃO-')
print()
print('-POTENCIAÇÃO-')
print()
print('---------------------')
numero_1 = input('Digite um número inteiro: ')
numero_2 = input('Digite outro número inteiro: ')

soma = int(numero_1)+int(numero_2)
print(f'A soma de {numero_1}+{numero_2} é {soma}.')

sub = int(numero_1)-int(numero_2)
print(f'A subtração de {numero_1}-{numero_2} é {sub}')

multi = int(numero_1)*int(numero_2)
print(f'A multiplicação de {numero_1}*{numero_2} é {multi}')

div = float(numero_1)/float(numero_2)
print(f'A divisão de {numero_1}/{numero_2} é {div}')

exp = float(numero_1)**float(numero_2)
print(f'A potenciação de {numero_1}**{numero_2} é {exp}')

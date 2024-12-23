
print('------------------------')
print('---INÍCIO DO REGISTRO---')
print('------------------------')
# nome
nome = input('Qual o seu nome? ')
# idade
idade = int(input('Qual a sua idade? '))
# altura (m)
altura = float(input('Qual a sua altura (NÃO MINTA RS)?  '))
# peso (kg)
peso = float(input('Qual o seu peso? '))

print(f'Olá {nome}')
# if condicao idade>18 altura 1.60 peso entre 50kg e 100kg
if idade>=18 and altura>=1.60 and peso>=50 and peso<=100:
    print('Você foi colocado na competição!')
# elif idade>16 altura>=1.75 peso<80
elif idade>16 and altura>=1.75 and peso<80:
    print('Por pouco que não atende aos requisitos')
    print('Você foi colocado na Competição da Nova Geração!')
# else o programa deve informar que {nome} não está apto a participar da competição
else:
    print('Infelizmente você não atende os requisitos')
    print('Tente ano que vem...')

print('------------------------')
print('ENCERRAMENTO DO REGISTRO')
print('------------------------')

# my imc
nome = 'Augusto'
altura = 1.64
peso = 49.50
imc = peso / altura**2

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'Ele pesa {peso}kg e seu imc é'
linha_3 = f'{imc:.2f}'

# Augusto tem 1.64 de altura,
# pesa 49 quilos e seu imc é
# 18,21832242712671
print(linha_1)
print(linha_2)
print(linha_3)
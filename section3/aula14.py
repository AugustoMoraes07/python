a = 'Augusto'
b = 'Moraes'
dia = 10
mes = 11
ano = 2007
c = f'{dia}/{mes}/{ano}'
string = 'nome={nome}   sobrenome={sobrenome} data={data}'
formato = string.format(nome=a,sobrenome=b,data=c)

print(formato)
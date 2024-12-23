# if/else/elif
# se/senao/senaose
entrada = input('Você quer "entrar" ou "sair" ? ')

if entrada == 'entrar':
    print('Você entrou no programa! <3')
    input('Quer "continuar" ou "sair" do programa ? ')
    print('[ERRO] Tente novamente mais tarde...')
elif entrada == 'sair':
    print('Você saiu do programa! TCHAU ')  
else:
    print('[ERRO] Finalizando programa...')  

# EASTER EGG HACK 
if entrada == 'HACKEAR':
    print('Você foi hackeado com sucesso!')


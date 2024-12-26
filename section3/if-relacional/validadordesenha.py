import string

#FUNÇÃO PARA VERIFICAR SE A SENHA TEM OS REQUISITOS
def validar_senha(nome,senha): 
    senha = senha.strip()
    caracteres_especiais = string.punctuation # Conjunto De caracteres especiais

    # Verificar se há pelo menos 4 caracteres
    if len(senha) < 4:
        return 'Senha deve conter pelo menos 4 caracteres' 
    
    # Verificar se há 1 letra maiúscula
    if not any(char.isupper() for char in senha):
        return 'Senha deve conter pelo menos uma letra maiúscula.'
    
    # Verificar se há 1 letra minúscula
    if not any(char.islower() for char in senha):
        return 'Senha deve conter pelo menos uma letra minúscula.'
    
    # Verificar se há 1 número
    if not any(char.isdigit() for char in senha):
        return 'Senha deve conter pelo menos um número.'
    
    # Verificar se há 1 caracter especial
    if not any(char in caracteres_especiais for char in senha):
        return 'Senha deve conter pelo menos um caracter especial'

    if senha.lower() == nome.lower():
        return 'Senha não pode ser o nome'

    return 'Senha válida!'

#  CÓDIGO PRINCIPAL
# PEDIR O NOME E SENHA
nome = input('NOME:')
senha = input('SENHA:')
resultado = validar_senha(nome,senha)

# IMPRIMIR NA TELA O ERRO OU VALIDAÇÃO
if resultado == 'Senha válida!':
    print(f'{resultado} Bem-vindo(a), {nome}!')
else:
    print(resultado)    

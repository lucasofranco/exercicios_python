#validacao de dados
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu sexo: ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Dados inválidos. Por favor, ', end='')
print(f'Sexo {sexo} registrado com sucesso.') 

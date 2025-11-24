#conversor de bases numéricas
n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

op = int(input('Sua opção: '))

if op == 1:
    b = str(bin(n))    
    print(f'{n} convertido para BINÁRIO é igual a: {b[2:]}')
elif op == 2:
    o = str(oct(n))
    print(f'{n} convertido para OCTAL é igual a: {o[2:]}')
elif op == 3:
    h = str(hex(n))
    print(f'{n} convertido para HEXADECIMAL é igual a: {h[2:].upper()}')
else:
    print('\033[31mERRO\033[m')
    print('Você não escolheu nenhuma opção. Tente Novamente.')

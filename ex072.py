#numero por extenso
numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

r = ''
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if n < 0 or n > 20:
            print('Tente novamente.', end=' ')
        else:
            break
    print(f'Você digitou o número {numeros[n]}')
    r = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    if r == 'N':
        break
print('FIM DO PROGRAMA')
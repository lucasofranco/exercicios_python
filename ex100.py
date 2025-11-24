from random import sample

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    numeros.append(sample(range(1, 11), 5))
    for n in numeros:
        print(f'{n} ', end='')
    print('PRONTO!', end='')
    
def somaPar():
    soma = 0
    for n in numeros[0]:
        if n % 2 == 0:
            soma += n
    print(f'\nSomando os valores pares de {numeros[0]} temos: {soma}')

numeros = []
sorteia()
somaPar()
#números primos
t = 0 #variavel para contar o numero de vezes que foi dividido

n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        print(f'\033[32m{c}\033[m', end=' ')
        t = t + 1
    elif n % c != 0:
        print(f'\033[31m{c}\033[m', end=' ')

print(f'\nO número {n} foi divisível {t} vezes.')
if t == 2:
    print('Portanto, ele é PRIMO!')
elif t != 2:
    print('Portanto, ele é NÃO PRIMO!')

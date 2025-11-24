#progressao aritmetica
texto = '10 TERMOS DE UMA PA'
print('=' * 36)
print(texto.center(35))
print('=' * 36)

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range(1, 11):
    print(pt + (c - 1) * r, end=' ')
print('ACABOU', end=' ')
    
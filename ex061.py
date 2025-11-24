#progressao aritmetica 2.0
print('----- 10 TERMOS DE UMA PA -----')
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

c = 1
while c < 11:
    print(pt + (c - 1) * r, end=' ')
    c += 1
print('ACABOU')

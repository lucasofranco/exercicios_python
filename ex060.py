#calculo de fatorial
print('----  Cálculo de Fatorial ----')
n = int(input('Digite um número: '))
nf = n
print('-=-' * 15)

# while
print(f'Calculando {n}! = ', end='')
f = 1
while n > 0:
    if n != 1:
        print(f'{n} x', end=' ')
    elif n == 1:
        print(f'{n} =', end=' ')
    f = n * f
    n -= 1
print(f)

#for
ff= 1
print('-=-' * 15)
print(f'Calculando {nf}! = ', end='')
for c in range(nf, 0, -1):
    if c != 1:
        print(f'{c} x', end=' ')
    elif c == 1:
        print(f'{c} =', end=' ')
    ff = c * ff 
print(ff)

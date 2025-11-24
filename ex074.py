#maior e menor valores com tupla
from random import randrange, randint

sorteado = []

maior = 0
menor = 0
for c in range(0, 5):
    n = randrange(11)
    if c == 0:
        menor = n
        maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    sorteado.append(n)

print('Os valores sorteados foram: ', end='')
for c in range(0,5):
    print(sorteado[c], end=' ')

print()
print(f'O menor valor sorteado foi: {menor}')
print(f'O maior valor sorteado foi: {maior}')

print('-=' * 25)
n = (randint(1,10), randint(1,10), randint(1,10),
     randint(1,10), randint(1,10))

print(f'Os valores sorteados foram: {n}')
print(f'O menor valor sorteado foi {min(n)}')
print(f'O maior valor sorteado foi {max(n)}')
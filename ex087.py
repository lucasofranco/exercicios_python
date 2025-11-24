#matriz em python 2.0
matriz = [[], [], []]
soma_pares = soma_3 = maior_2 = 0

print('-=' * 25)
for l in range(0, 3):
    for c in range(0, 3):
        v = int(input(f'Digite um valor para {[l, c]}: '))

        if v % 2 == 0:
            soma_pares += v

        if l == 1:
            if v > maior_2:
                maior_2 = v

        if c == 2:
            soma_3 += v
        
        matriz[l].append(v)

print('-=' * 25)
for cont in range(0, 3):
    print(matriz[cont])
print('-=' * 25)

print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_3}')
print(f'O maior valor da segunda linha é: {maior_2}')
print('-=' * 25)

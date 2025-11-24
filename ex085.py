#lista com pares e ímpares
lista = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}o. valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print('-=' * 25)
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Ps valores ímpares digitados foram: {sorted(lista[1])}')
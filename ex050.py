#soma dos pares
s = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}. valor: '))
    if n % 2 == 0:
        s += n
print(f'A soma entre os pares foram: {s}')

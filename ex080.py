#lista ordenada sem sort
lista = []

print('=-' * 25)

for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if c == 0 or v > lista[-1]:
        lista.append(v)
        print('Valor adicionado...')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                break

for valor in lista:
    print('=-' * 25)
    print(f'Os valores digitados em ordem foram: {lista}')

#listas compostas e analise de dados
galera = []
dados = []
nomemaior = []
nomemenor = []
pesos = []
totp = 0

print('-=' * 25)
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pesos.append(peso)
    dados.append(nome)
    dados.append(peso)
    for p in pesos:
        if peso >= max(pesos):
            pesomaior = max(pesos)
        elif peso <= min(pesos):
            pesomenor = min(pesos)
    galera.append(dados[:])
    dados.clear()   
    totp += 1

    while True:
        r = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if r not in 'SN':
            print('Ops! Opção inválidada! Tente novamente...')
        else:
            break
    if r in 'N':
        break

print('-=' * 25)
print(f'Total de pessoas cadastradas: {totp}')
print(f'O maior peso foi de {pesomaior}Kg. Peso de:', end=' ')
for p in galera:
    if p[1] == pesomaior:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi de {pesomenor}Kg. Peso de:', end=' ')
for p in galera:
    if p[1] == pesomenor:
        print(f'[{p[0]}]', end=' ')

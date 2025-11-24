futebol = {}
gols = []
lista_completa = []

while True:
    tot = 0
    print('-=' * 30)
    nome = str(input('Nome do jogador: '))
    part = int(input(f'Quantas partidas {nome} jogou? '))
    for c in range(part):
        g = int(input(f'  Quantos gols na partida {c+1}? '))
        tot += g
        gols.append(g)
    futebol['nome'] = nome
    futebol['gols'] = (gols[:])
    futebol['total'] = tot
    lista_completa.append(futebol.copy())
    gols.clear()

    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if resp not in 'SN':
            print('Ops! Tente novamente...')
        else:
            break
    if resp == 'N':
        break

print('-=' * 25)
print(f'{"cod.":<4}{"nome":>5}{"gols":>15}{"total":>15}')
print('-' * 50)

for i, v in enumerate(lista_completa):
    print(f'{i:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    if busca == 999:
        break
    if busca > len(lista_completa) or busca < 0:
        print(f'ERRO! Não existe esse jogador com o código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista_completa[busca]["nome"]}:')
        for i, g in enumerate(lista_completa[busca]['gols']):
            print(f'  No jogo {i+1} fez {g} gols.')
    print('-' * 50)
print('VOLTE SEMPRE')
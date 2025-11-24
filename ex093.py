#cadastro de jogador de futebol
futebol = {}
gols = []

print('-=' * 30)
futebol['nome'] = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas {futebol["nome"]} jogou? '))
for c in range(part):
    g = int(input(f'Quantos gols na partida {c}? '))
    gols.append(g)
futebol['gols'] = gols[:]
futebol['total'] = sum(gols)

print('-=' * 30)
print(futebol)

print('-=' * 30)
for k, v in futebol.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 30)
print(f'O jogador {futebol["nome"]} jogou {part} partidas.')

for i, g in enumerate(gols):
    print(f'--> Na partida {i}, fez {g} gols.')
print(f'Foi um total de {sum(gols)} gols.')

print('-=' * 30)
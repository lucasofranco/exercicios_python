#jogos de dados em python
from random import randint
from time import sleep
from operator import itemgetter

jogos = {'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)}

ranking = []

print('VALORES SORTEADOS:')
for k, v in jogos.items():
    sleep(1)
    print(f'O {k} tirou {v}')

print('-=' * 30)
print('RANKING DOS JOGADORES:')
ranking = sorted(jogos.items(), key=itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f'{i+1}. lugar: {v[0]} com {v[1]}')
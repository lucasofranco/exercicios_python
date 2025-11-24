#tuplas com time do brasileirao
brasileirao = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Botafogo', 
               'Mirassol', 'São Paulo', 'Bragantino', 'Fluminense', 'Internacional', 
               'Ceará', 'Corinthians', 'Grêmio', 'Atlético Mineiro', 'Vasco', 
               'Santos', 'Vitória', 'Juventude', 'Fortaleza', 'Sport')

tabela = 'TABELA BRASILEIRÃO'
print('-=-' * 15)
print(f'{tabela:^43}')
print('-=-' * 15)
print(f'Os 5 primeiros são: {brasileirao[0:5]}')
print('-=-' * 15)
print(f'Os 4 últimos são: {brasileirao[16:20]}')
print('-=-' * 15)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-=-' * 15)
print(f'O Palmeiras está na {brasileirao.index('Palmeiras') + 1}. posição')
print('-=-' * 15)

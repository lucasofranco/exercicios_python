#palpites para a Mega Sena  
from random import sample
from time import sleep
lista_jogos = []
teste = []

print('-' * 30)
print(f'{'JOGUE NA MEGA SENA':^30}')
print('-' * 30)

while True:
    try:
        quant_str = str(input('Quantos jogos você deseja sortear? '))
        quant = int(quant_str)
        break
    except ValueError:
        print('Ops! Digite um valor válido.')

for c in range(quant):
    sorteio = sorted(sample(range(1, 61), 6))
    lista_jogos.append(sorteio)

print('-' * 30)
print(f'{'SORTEANDO JOGOS':^30}')
print('-' * 30)

for i, jogos in enumerate(lista_jogos):
    sleep(1)
    print(f'Jogo {i+1}: {jogos}')
print('-' * 30)

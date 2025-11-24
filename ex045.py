#jokenpo
from random import choice
from time import sleep

#jogador escolhe oq jogar
print('Suas opções: ')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
op = int(input('Qual é a sua jogada? ')) 

#opcao escolhida para jogador
if op == 1:
    j = 'PEDRA'
elif op == 2:
    j = 'PAPEL'
elif op == 3:
    j = 'TESOURA'
else:
    j = '\033[31mJOGADA INVÁLIDA\033[m'

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')

#pc escolhe oq jogar
pc = choice(['PEDRA', 'PAPEL', 'TESOURA'])

print('-=' * 15)
print(f'Computador jogou {pc}')
print(f'Jogador jogou {j}')
print('-=' * 15)

#resultado da partida
if j == pc:
    print('EMPATE')
elif j != pc:
    if j == 'PEDRA' and pc == 'TESOURA':
        print('JOGADOR VENCE!')
    elif j == 'PAPEL' and pc == 'PEDRA':
        print('JOGADOR VENCE!')
    elif j == 'TESOURA' and pc == 'PAPEL':
        print('JOGADOR VENCE!')
    elif j == '\033[31mJOGADA INVÁLIDA\033[m' and pc == ('TESOURA', 'PAPEL', 'PEDRA'):
        print('COMPUTADOR VENCE!')
    else:
        print('COMPUTADOR VENCE!')

print('-=' * 15)
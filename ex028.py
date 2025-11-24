#adivinhar o número que o pc "pensou"
import time
import random
print('=' * 65)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=' * 65)
num_pc = random.randint(0, 5) #o numero que o pc pensou
num_us = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
time.sleep(2)
if num_us == num_pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {num_pc} e não no {num_us}!')
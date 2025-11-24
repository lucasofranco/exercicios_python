#jogo da adivinhação 2.0
from random import randint
from time import sleep

print('Sou seu computador...')
sleep(2)
print('Será que você consegue adivinhar em qual número vou pensar?')
sleep(2)
print('HUUUM')
sleep(2)
print('HUUUUUM')
sleep(2)
pc = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')

p = -1
s = 0
while p != pc:
    p = int(input('Qual é o seu palpite? '))
    s += 1
    if p > pc:
        print('Menos... Tente mais uma vez.')
    elif p < pc:
        print('Mais... Tente mais uma vez.')
print(f'Acertou com {s} tentativas. Parabéns!')

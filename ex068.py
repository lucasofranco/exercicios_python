#par ou impar
from random import randint

pc_n = soma = tot = 0
op_pc = ''

print('=-' * 25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 25)

while True:
    n = int(input('Diga um valor: '))
    op = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]

    if op != 'P' and op != 'I':
        while op != 'P' and op != 'I':
            print('-' * 50)
            print('Opção desconhecida!')
            op = str(input('Digite uma opção correta [P/I]: ')).upper().strip()[0]

    if op == 'P':
        op_pc = 'I'
    elif op == 'I':
        op_pc == 'P'

    pc_n = (randint(1, 10))
    soma = n + pc_n

    print('-' * 50)
    print(f'Você jogou {n} e o computador {pc_n}.')
    if soma % 2 == 0:
        print(f'Total: {soma} [PAR]')
        if op == 'P' and op_pc == 'I':
            print('VOCÊ GANHOU!')
            print('Vamos jogar novamente...')
            tot += 1
        else:
            print('VOCÊ PERDEU!')
            break
    if soma % 2 != 0:
        print(f'Total: {soma} [ÍMPAR]')
        if op == 'I' or op_pc == 'P':
            print('VOCÊ GANHOU!')
            print('Vamos jogar novamente...')
            tot += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('-' * 50)

print('=-' * 25)
print(f'GAME OVER! Você venceu {tot} vezes.')
print('=-' * 25)

from time import sleep

def maior(*valor):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for v in valor:
        print(f'{v} ', end='', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(valor)} valores ao todo.')
    if len(valor) == 0:
        print('O maior valor informado foi 0')
    else:
        print(f'O maior valor informado foi {max(valor)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
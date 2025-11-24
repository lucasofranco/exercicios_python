from time import sleep

def lin():
    print('-=' * 15)

def contagem(a, b, c):
    if c == 0:
        c = 1
    if a < b:
        c = abs(c)
        print(f'Contagem de {a} até {b} de {c} em {c}')
        sleep(2)
        for cont in range(a, b+1, c):
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
        print('FIM!', end=' ')
    if a > b:
        c = abs(c)
        print(f'Contagem de {a} até {b} de {c} em {c}')
        sleep(2)
        for cont in range(a, b-1, -c):
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
        print('FIM!', end=' ')

lin()
contagem(1, 10, 1)
print()
lin()
contagem(10, 0, -2)
print()
lin()

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
lin()
contagem(inicio, fim, passo)
print()
lin()

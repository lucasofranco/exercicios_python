#menu de opções
from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

op = 0
while op != 5:
    print('-=-' * 15)
    print('''    [MENU DE OPÇÕES  
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    print('-=-' * 15)
    op = int(input('>>> Qual é a sua opção? '))
    print('-=-' * 15)

    if op == 1:
        print(f'A soma entre {n1} e {n2} é: {n1 + n2}')
    elif op == 2:
        print(f'A multiplicação entre {n1} e {n2} é: {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            print(f'O número {n1}  é maior do que o número {n2}')
        elif n2 > n1:
            print(f'O número {n2} é maior do que o número {n1}')
        else:
            print(f'O número {n1} e {n2} possuem o mesmo valor.')
    elif op == 4:
        n1 = int(input('Digite o novo valor para o primeiro número: '))
        n2 = int(input('Digite o novo valor para o segundo número: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente...')
    sleep(2)
print('-=-' * 15)
print('Fim do programa! Volte sempre!')
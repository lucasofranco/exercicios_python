# Extraindo dados de uma lista
valores = []

print('-=' * 25)
while True:
    while True:
        try:
            v_str = str(input('Digite um valor: '))
            v = int(v_str)
            valores.append(v)
            break
        except ValueError:
            print('Ops! Algo deu errado. Tente novamente.', end=' ')

    while True:
        r = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
        if r != 'S' and r != 'N':
            print('Ops! Algo deu errado. Tente novamente.')
        else:
            break
    if r == 'N':
        break
print('-=' * 25)

valores.sort(reverse=True)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
elif 5 not in valores:
    print('O valor 5 não faz parte da lista.')

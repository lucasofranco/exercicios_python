#valores unicos em uma lista
valores = []

print('-=' * 25)
while True:
    while True:
        try:
            v_str = str(input('Digite um valor: '))
            v = int(v_str)
            break
        except ValueError:
            print('Ops! Algo deu errado! Tente novamente.')

    if v not in valores:
        print('Adicionado com sucesso!')
        valores.append(v)
    elif v in valores:
        print('Valor duplicado! Não adicionei a lista.')

    while True:
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if r != 'S' and r != 'N':
            print('Erro! Tente novamente!', end=' ')
        else:
            break
    if r == 'N':
        break
print('-=' * 25)
print(f'Você digitou os valores: {sorted(valores)}')
        
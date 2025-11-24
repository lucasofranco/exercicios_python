#estaticas em produtos
r = nome_barato = ''
soma = quant_mil = barato = 0

loja = 'LOJA DO LUKYNHAS'
print('-' * 30)
print(f'{loja:^30}')
print('-' * 30)

while True:
    produto = str(input('Nome do produto: ')).strip().lower()

    while True:
        try:
            valor_str = str(input('Preço: R$'))
            valor = float(valor_str)
            break
        except ValueError:
            print('Ops! Esse valor está incorreto. Por favor, tente novamente!')
            print('-' * 30)
    
    if valor > 1000:
        quant_mil += 1

    if barato == 0:
        barato = valor
        nome_barato = produto
    elif barato > valor:
        barato = valor
        nome_barato = produto

    while True:
        r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if r == 'S' or r == 'N':
            break
        elif r != 'S' and r != 'N':
            print('Ops! Algo deu errado. Por favor, tente novamente!')
    if r == 'N':
        break

    soma += valor

print('-' * 30)
print(f'Total da compra: R${soma}')
print(f'Temos {quant_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi a/o {nome_barato} custando: R${barato:.2f}')
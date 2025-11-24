#unindo dicionarios e lista
dados = {}
pessoas = []
tot = soma_idades = 0

while True:
    dados['nome'] = str(input('Nome: ')).strip().title()
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] not in 'MF':
            print('Ops! Tente novamente...')
        else:
            break
    idade = int(input('Idade: '))
    dados['idade'] = idade
    pessoas.append(dados.copy())
    tot += 1
    soma_idades += idade

    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp not in 'SN':
            print('Ops! Tente novamente...')
        else:
            break
    if resp in 'N':
        break

media = soma_idades / tot

print('-=' * 25)
print(f'- O grupo tem {tot} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')

print('- As mulheres cadastradas foram: ', end='')
for d in pessoas:
    for v in d.values():
        if v == 'F':
            print(f'{d["nome"]}', end=' ')

print('\n- Lista das pessoas que estão acima da média: ')
for d in pessoas:
    for k, v in d.items():
        if k == 'idade':
            if v > media:
                print(d)
print('->ENCERRADO<-')

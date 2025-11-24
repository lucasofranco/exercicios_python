ficha = []

print('-=' * 30)
while True:
    nome = str(input('Nome: ')).title().strip()
    while True:
        try:
            nota1_str = str(input('Nota 1: '))
            nota1 = float(nota1_str)
            break
        except ValueError:
            print('Ops! Tente novamente...')
    while True:
        try:
            nota2_str = str(input('Nota 2: '))
            nota2 = float(nota2_str)
            break
        except ValueError:
            print('Ops! Tente novamente...')
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if resp not in 'SN':
            print('Ops! Tente novamente...')
        else:
            break
    if resp in 'N':
        break
print('-=' * 30)

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
print('-' * 26)


while True:
    while True:
        try:
            r_str = str(input('Mostrar notas de qual aluno? (999 interrompe): '))
            r = int(r_str)
            break
        except ValueError:
            print('Ops! Tente novamente...')
    if r == 999:
        print('Finalizando...')
        break
    if r <= len(ficha) - 1:
        print(f'As notas de {ficha[r][0]} são {ficha[r][1]}')
    print('-' * 26)
print('Volte sempre!')
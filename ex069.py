sexo = r = ''
maior_de_idade = hom = mul_20 = 0

while True:
    print('-' * 26)
    print('   CADASTRE UMA PESSOA')
    print('-' * 26)

    while True:
        try:
            idade_str = str(input('Idade: '))
            idade = int(idade_str)
            break
        except ValueError:
            print('Ops! Isso não é um número. Por favor, tente novamente!')
            print('-' * 26)


    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        maior_de_idade += 1
    if sexo == 'M':
        hom += 1
    if sexo == 'F':
        if idade < 20:
            mul_20 += 1
    print('-' * 26) 

    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if r == 'N':
        break

print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {maior_de_idade}')
print(f'Total de homens cadastrados: {hom}')
print(f'Total de mulheres com menos de 20 cadastradas: {mul_20}')
print('-' * 26)
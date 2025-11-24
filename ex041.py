#classificando atletas
ano = int(input('Ano de nascimento do atleta: '))

idade = 2025 - ano
print(f'O atleta tem {idade} ano(s)')

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
    
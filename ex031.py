#custo da viagem
print('\033[36m-=-\033[m' * 15)
d = float(input('Qual a distância da sua viagem? '))
print('\033[36m-=-\033[m' * 15)
print(f'Você está prester a começar uma viagem de {d}Km.')
if d <= 200:
    print(f'O preço da sua passagem será de R${d * 0.50:.2f}')
else:
    print(f'O preço da sua passagem será de \033[32mR${d * 0.45:.2f}')
print('\033[36m-=-\033[m' * 15)
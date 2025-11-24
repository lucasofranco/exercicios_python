def area(l, c):
    area = l * c
    print(f'A área de um terreno {l}x{c} é de {area}m²')


print('-' * 26)
print('   Controle de Terrenos   ')
print('-' * 26)

larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)

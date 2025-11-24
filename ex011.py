#calcular quantidade de tinta necessário para pintar uma parede.
l = float(input('Largura da parede em metros: '))
al = float(input('Altura da parede em metros: '))
a = l * al
print(f'Área da parede: {a}m²')
#cada litro de tinta pinta uma área de 2m²
litros_necessarios = a/2
print(f'Será necessário {litros_necessarios} litros de tinta.')
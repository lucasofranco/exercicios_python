#Separando dígitos de um número
n = int(input(('Informe um número de 0 a 9999: ')))
num = str(10000 + n)
print(f'Unidade: {num[4]}')
print(f'Dezena: {num[3]}')
print(f'Centena: {num[2]}')
print(f'Milhar: {num[1]}')
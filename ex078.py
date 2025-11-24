#maior e menor valores
valores = []

print('=-' * 25)
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a POSIÇÃO {cont}: ')))
print('=-' * 25)

print(f'Você digitou os valores: {valores}')

print(f'O menor valor digitado foi {min(valores)} nas posições:', end=' ')
for p, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{p}...', end=' ')

print(f'\nO maior valor digitado foi {max(valores)} nas posições:', end=' ')
for p, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{p}...', end=' ')

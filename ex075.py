#análise de dados em uma tupla
lista = (int(input('Digite um número: ')), int(input('Digite outro número: ')), 
         int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores: {lista}')

print(f'O valor 9 apareceu: {lista.count(9)} vezes.')

if 3 in lista:
    print(f'O valor 3 apareceu na posição: {lista.index(3) + 1}.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')

print('Os valores pares digitados foram: ', end='')
for c in range(4):
    if lista[c] % 2 == 0:
        print(f'{lista[c]}, ', end=' ')
